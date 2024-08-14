import data_handler
import Stopwords
import MapReduce
if __name__== '__main__':
  df = data_handler.prepare_data()
  Stopword_list = Stopwords.construct_stopword_list()
  
  
  i=0 # assign paper ID for map-reduce process
  process_amount = 10000
  mapped = []
  word_index= []
  for each_paper in df['text']:
    #content = df['body_text'][i]
    ids = i
    word_count = MapReduce.map(each_paper,ids,Stopword_list)
    word_index.append(get_representation(word_count))
  
    mapped+=(word_count)
  
    i+=1
    if i%100==0: # for developer to monitor progress
      print('Processed paper in map stage: {}'.format(i))
  
    if i>process_amount: # for developer to do early stop
      break
  sparse_index = MapReduce.reduce(mapped)
  top_50_list = MapReduce.get_top_50_list(sparse_index)



  i=0
  ID_list = []
  for each in word_index:
      ID_list.append (i)
      i+=1
  Link_list = list(df['link'])[0:process_amount+1]
  d = {'ID': ID_list,'title':list(df['title']),'Link': Link_list, 'Representation':word_index}
  df_representation = pd.DataFrame(data=d)



word_index_service.word_index_service(sparse_index,df_representation)

  
