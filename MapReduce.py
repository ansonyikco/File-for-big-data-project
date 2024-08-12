import nltk
nltk.download('punkt')


def map(content,ids):
  #content = 'main body text in string format like this'
  #ids = ID of paper in int format
  #output = [(word 'abc', (title ID : 3, count: 2)),('alkaline', (5, 3))......]

  word_count = {}
  nltk_tokens = nltk.word_tokenize(content)
  for each_word in (nltk_tokens):
    each_word = each_word.lower() # turn all words to lower case
    if (each_word not in stopwords) and (each_word not in punctuation) and (not (each_word.isdigit())):
      #remove stopword and punctuation and integer

      if each_word in word_count:
        #seen before in this paper
        word_count[each_word]+=1
      else :
        #new word in this paper
        word_count[each_word] = 1

  output = []
  for each in word_count:

    output.append((each,(ids,word_count[each])))

  return (output)

def reduce(mapped):
  #mapped = [('abc', (3, 2)),('alkaline', (5, 3))......]
  #keyword_database = {'abc':((1,3,5,7),2500),'bbc':((1,3,5,7),2456)}
  print ('Starting reduce')
  mapped.sort()
  keyword_database = {}
  Last_word = ''

  for each in mapped:

    if  each[0]!=Last_word:# next new word

      keyword_database[each[0]]= [[(each[1])],each[1][1]]
      Last_word = each[0]

    else:

      keyword_database[each[0]][0].append(each[1])
      count = keyword_database[each[0]][1]+(each[1][1])
      keyword_database[each[0]][1]= count
      Last_word = each[0]



  return keyword_database

def get_top_50_list(sparse_index):
  #input = {'abc':((1,3,5,7),2500),'bbc':((1,3,5,7),2456)}
  #output = [('top1word',12345),('top2word',12344),('top1word',12343)]
  dense_list = []
  for key in sparse_index:


    dense_list.append((sparse_index[key][1],key))
  dense_list.sort(reverse=True)
  dense_list=dense_list[:50]
  i=0
  for each in dense_list:
    print (i,each)
    i+=1

  return dense_list


def get_representation(word_count):
  word_index = []
  lst = sorted(word_count, key=lambda x: x[1], reverse=True)
  word,info = zip(*lst)
  return (word[0:10])






i=0 # assign paper ID for map-reduce process
process_amount = 10000
mapped = []
word_index= []
for each_paper in df['text']:
  #content = df['body_text'][i]
  ids = i
  word_count = map(each_paper,ids)
  word_index.append(get_representation(word_count))

  mapped+=(word_count)

  i+=1
  if i%100==0: # for developer to monitor progress
    print('Processed paper in map stage: {}'.format(i))

  if i>process_amount: # for developer to do early stop
    break
sparse_index = reduce(mapped)
top_50_list = get_top_50_list(sparse_index)

