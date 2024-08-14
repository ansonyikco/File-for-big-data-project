def word_retrieve(word,index):
  try:
    return index[word][0]
  except:
    return [[]]

pd.set_option('max_colwidth', None)
def word_index_service(df_representation,sparse_index):

    while True:
      paper_list_for_multi = []
      print ("_________________________________________________________")
      word = input ("Input Keyword or -9999 to end service: ").lower()
      if word == '-9999':break
      if word.isdigit():
        #search by ID
        word = int(word)
        print (df_representation.iloc[word])
      elif word not in  stopwords:

        word = word.split()
        if len(word)>1:

          for each in word:

            paper_list = word_retrieve(word[0],sparse_index)

            paper_list.sort(key = lambda x: x[1],reverse = True)
            output_list, rank = zip(*paper_list)
            print (df_representation.iloc[list(output_list[0:5])])



          print (df_representation.iloc[list(set(paper_list_for_multi))])
        else:
          paper_list = word_retrieve(word[0],sparse_index)

          paper_list.sort(key = lambda x: x[1],reverse = True)
          output_list, rank = zip(*paper_list)
          print (df_representation.iloc[list(output_list[0:5])])
      else:
        print ('Input is in stopword list, please be more specific.')

