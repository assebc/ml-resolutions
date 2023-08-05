from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from nltk import sent_tokenize
from nltk.corpus import stopwords

def tldr(text_to_summarize):
    tokenize_sent = np.array(sent_tokenize(text=text_to_summarize))
    stop_words_list = list(set(stopwords.words('english')))
    l = len(tokenize_sent)
    tf_idf = TfidfVectorizer(stop_words=stop_words_list)
    a = tf_idf.fit_transform(np.array(tokenize_sent)).toarray()
    tf_idf_sent = np.sum(a,axis=1)
    sent_to_pick = tokenize_sent[np.where(tf_idf_sent > 3)[0]]
    summary = '.'.join(sent_to_pick)
    return summary