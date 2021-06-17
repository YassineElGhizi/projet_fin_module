from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from gensim.models import Word2Vec



#======================  _Tokenization_
class Tokenization():
    def getData(self):
        pass
    
    @staticmethod
    def tokenizationProcess(example_sent):

        tokens = word_tokenize(example_sent)
        return tokens



#================= _stemming_
class Stemming():
    def getData(self):
        pass

    @staticmethod
    def defineStemming(example_sent):
        word_tokens = Tokenization.tokenizationProcess(example_sent)
        filtered_sentence = []
        ps = nltk.ISRIStemmer()
        for w in word_tokens:
            filtered_sentence.append(ps.stem(w))
        return filtered_sentence



#==================_Lemmatization_
class Lemmatization():
    
    @staticmethod
    def getLemmatization(example_sent):
        word_tokens = Tokenization.tokenizationProcess(example_sent)
        filtered_sentence = []

        for w in word_tokens:
            filtered_sentence.append(nltk.ISRIStemmer().suf32(w))
        return filtered_sentence



#=================_bag_of_words_
class BagOfWords():

    @staticmethod
    def bag_of_words(texts_arr):
        texts = texts_arr.split(';')
        words = []
        for i in range(len(texts)):
            for word in texts[i].split():
                if word.lower() not in words:
                    words.append(word.lower())

        bow = [dict().fromkeys(words, 0) for x in range(len(texts))]
        for i, sentence in enumerate(texts):
            sentence_words = word_tokenize(sentence.lower())
            # frequency word count
            bag = bow[i]
            for sw in sentence_words:
                for word in words:
                    if word == sw:
                        bag[word] += 1
        return bow



#==============_POST Tagging_
class PosTagging():
    
    @staticmethod
    def getpos(example_sent):
        stop_words = set(stopwords.words('arabic'))
        tokens = sent_tokenize(example_sent)
        for i in tokens:

            word_list = nltk.word_tokenize(i)
            word_list = [word for word in word_list if not word in stop_words]
            pos = nltk.pos_tag(word_list)
        return pos



#====================_TF-IDF_
class TFIDF():
    
    @staticmethod
    def gettf(example_sent):
        tokens = word_tokenize(example_sent)
        tfidf = TfidfVectorizer(tokenizer=tokens, stop_words=stopwords.words('arabic'))
        return tfidf



#===================_Word2Vect_
class Word2Vect:

    @staticmethod
    def word_to_vect(all_words):
        words = Tokenization.tokenizationProcess(all_words)
        print(words)
        word2vec = Word2Vec(words, min_count=2)
        vocabulary = word2vec.wv.index_to_key
        print(vocabulary)


