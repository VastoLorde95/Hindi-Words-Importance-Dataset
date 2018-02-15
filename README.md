# Hindi Words Ranked By TF IDF 
This is a dataset of ~14000 Hindi words and their inverse document frequencies. The dataset was generated from a collection of 1476 news articles in Hindi from various websites. All news articles were on the topic "India".

The `generate_word_idf.py` script can be used to create similar datasets on other corpuses as well.

The file `word_value_pairs.txt` contains the actual data. The data is given in increasing order of idf score.

This dataset can be particularly useful to filter out stop words from Hindi sentences when trying to find the most revelant words in documents. For example - the tf-idf algorithm can be used to generate relevant tags on for various web articles which are written in Hindi.
