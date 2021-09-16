from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.metrics import classification_report,accuracy_score
import six.moves.cPickle as pickle
from imdbReview import extract_words


f = open('train.pkl', 'rb')
reviews = pickle.load(f)
f.close()

f = open('test.pkl', 'rb')
test = pickle.load(f)
f.close()

vectorizer = TfidfVectorizer(min_df=5, max_df=0.8, 
                            sublinear_tf=True, use_idf=True)
train_features = vectorizer.fit_transform(reviews[0])
test_features = vectorizer.transform(test[0])

classifier_liblinear = svm.LinearSVC()
classifier_liblinear.fit(train_features, reviews[1])
prediction_liblinear = classifier_liblinear.predict(test_features)
print(classification_report(test[1], prediction_liblinear))

def givePolarity(sentence):
    sentences = []
    sentences.append(sentence)
    input_features = vectorizer.transform(extract_words(sentences))
    prediction = classifier_liblinear.predict(input_features)
    return prediction[0]