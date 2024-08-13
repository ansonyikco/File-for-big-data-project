def load_data():

  url = 'https://raw.githubusercontent.com/ansonyikco/File-for-big-data-project/main/articles.csv'
  import pandas as pd

  df = pd.read_csv(url, on_bad_lines='skip')
  print (df.head)

  df.dropna(inplace=True)
  print (df.info())
  return df

def clean_data(df):


  # set seed
  DetectorFactory.seed = 0

  # hold label - language
  languages = []

  # go through each text
  for ii in tqdm(range(0,len(df))):
      # split by space into list, take the first x intex, join with space
      text = df.iloc[ii]['text'].split(" ")

      lang = "en"
      try:
          if len(text) > 50:
              lang = detect(" ".join(text[:50]))
          elif len(text) > 0:
              lang = detect(" ".join(text[:len(text)]))
      # ught... beginning of the document was not in a good format
      except Exception as e:
          all_words = set(text)
          try:
              lang = detect(" ".join(all_words))
          # what!! :( let's see if we can find any text in abstract...
          except Exception as e:

              try:
                  # let's try to label it through the abstract then
                  lang = detect(df.iloc[ii]['title'])
              except Exception as e:
                  lang = "unknown"
                  pass

      # get the language
      languages.append(lang)
  from pprint import pprint
  languages_list = []
  languages_count_list = []
  languages_dict = {}
  for lang in set(languages):
      languages_dict[lang] = languages.count(lang)
      languages_list.append(lang)
      languages_count_list.append(languages.count(lang))

  print("Total: {}\n".format(len(languages)))
  pprint(languages_dict)
  df['language'] = languages
  df = df[df['language'] == 'en']

  df.info()
  return df

def prepare_data():
  df = load_data()
  return clean_data(df)
