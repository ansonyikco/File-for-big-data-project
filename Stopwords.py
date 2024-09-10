import requests
import string


def get_punctuation():
  #getting punctuation for removal of them
  return string.punctuation

def get_stopwords():
  #getting stopword from internet
  stopwords_list = requests.get("https://gist.githubusercontent.com/rg089/35e00abf8941d72d419224cfd5b5925d/raw/12d899b70156fd0041fa9778d657330b024b959c/stopwords.txt").content
  stopwords = set(stopwords_list.decode().splitlines())
  stopwords = list(stopwords)
  return stopwords
def add_custom_stopword(stopwords,custom_stopword):
  #combining stopwords from internet and our own input
  stopwords+=(custom_stopword)
  print ('added custom stopword')
  return (stopwords)

def construct_stopword_list():
  punctuation = get_punctuation()
  stopwords = get_stopwords()
  custom_stopword = ['t.','al.','study','studies','activity','based','±','patients','production','``',"''",'product','process','','total','follow','high','higher','levels',
                     'low','lower','included','including','include','months','month','year','years','day','days','global','local', 'cases','factor','factors', 'effective', 'data', 'enter',
                     'consumption', 'table', 'fig', 'sample', 'score','table', 'figure', 'sample', 'scores','reduces','reduce','analysis',"'s",'model','time','support','people',
                     'specific','addition','rate','compared','role','models','development','expression','case','effects','number','performed','groups','increase','potential','severe','values',
                     'considered','findings''type','provide','method','previous','current','result','approach', 'conditions','type','findings','observed','level','variables',"'",'"','’','”','“', '—','set','lot','called','enjoyed','input','output','things']
  stopwords = add_custom_stopword(stopwords,custom_stopword)
  return stopwords
