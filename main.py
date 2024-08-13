import data_handler
import Stopwords
import MapReduce
if __name__== '__main__':
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
