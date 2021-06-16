from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split

tfvect = TfidfVectorizer(stop_words='arabic', max_df=0.7)
tfvect = TfidfVectorizer(max_df=0.7)
loaded_model = pickle.load(open(r'C:\Users\elGhizi\Desktop\fakeNews\ProjetFinModule\backend\machineLearningModels\model.pkl', 'rb'))
dataframe = pd.read_csv(r'C:\Users\elGhizi\Desktop\fakeNews\ProjetFinModule\scrapping\FakeNews.txt', delimiter = ";")
x = dataframe['text']
y = dataframe['label']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

def fake_news_det(news):
    tfid_x_train = tfvect.fit_transform(x_train.values.astype('U'))
    tfid_x_test = tfvect.transform(x_test.values.astype('U'))
    input_data = [news]
    vectorized_input_data = tfvect.transform(input_data)
    prediction = loaded_model.predict(vectorized_input_data)
    return prediction