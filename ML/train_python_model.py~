import pandas
import numpy
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, normalize, scale
from sklearn import cross_validation, metrics
from unbalanced_dataset import SMOTE
from sklearn.externals import joblib

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from utils.metrics import calculate_metrics

def generateIntSequence(valString):
    val = [float(x) for x in valString.split("_")]
    return val

df = pandas.read_csv('senia.csv').values
x = map(lambda x: map(lambda y: generateIntSequence(y), x), df[:, 1:-2])
#print x[0], x[-1]
y = map(lambda y: int(y), df[:,-1]) 
y = numpy.array(y)
#print y[0], y[-1]
x_metrics = []
for i, x_i in enumerate(x):
    timestamp = int(df[i, -2])
    data = [timestamp, ] + x_i
    #if i % 1000 == 0:
    #    print data
    x_metrics.append(calculate_metrics(data)[:-1])

#print x_metrics[0]
x_metrics = numpy.array(x_metrics) 
#x_metrics = normalize(x_metrics)
#x_metrics = scale(x_metrics)  

def f6(x):
    if x == 7:
        return 2
    elif x > 7:
        return x - 1
    else:
        return x


y = map(f6, y)

y = numpy.array(y)

sm = SMOTE(kind='regular')
for i in xrange(20):
    x_metrics, y = sm.fit_transform(x_metrics, y)


clf = RandomForestClassifier(n_estimators=100, class_weight='auto')
pr = cross_validation.cross_val_predict(clf, x_metrics, y, cv=10)
#print metrics.accuracy_score(y, pr)
#print metrics.confusion_matrix(y, pr)

delete_rows_indexes = [i for i, y_i in enumerate(pr) if y_i == 3 and y[i] == 2]
x_metrics = numpy.delete(x_metrics, delete_rows_indexes, axis=0)
y = numpy.delete(y, delete_rows_indexes, axis=0)
#clf.fit(x_metrics,y)
#joblib.dump(clf, 'rand_forest_model_3.pkl')

 
pr = cross_validation.cross_val_predict(clf, x_metrics, y, cv=10)
print metrics.accuracy_score(y, pr)
#print metrics.confusion_matrix(y, pr)

#sm = SMOTE(kind='regular')
#for i in xrange(30):
#    x_metrics, y = sm.fit_transform(x_metrics, y)

#clf.fit(x_metrics,y)
#pr = cross_validation.cross_val_predict(clf, x_metrics, y, cv=10)
#print metrics.accuracy_score(y, pr)
#print metrics.confusion_matrix(y, pr) 
#print cross_validation.cross_val_score(clf, x_metrics, y, cv=20)
#joblib.dump(clf, 'rand_forest_model_2.pkl') 

#print '\n##### SVC ####'
#from sklearn.svm import SVC
#x_metrics = normalize(x_metrics)
#x_metrics = scale(x_metrics)
#pr = cross_validation.cross_val_predict(clf, x_metrics, y, cv=10)
#print metrics.accuracy_score(y, pr)
#print metrics.confusion_matrix(y, pr) 
#print cross_validation.cross_val_score(clf, x_metrics, y, cv=20)

#print '\n#### DBSCAN ####'
#from sklearn.cluster import DBSCAN
#db = DBSCAN(eps=0.3, min_samples=10).fit(x_metrics)
#core_samples = db.core_sample_indices_
#labels = db.labels_
#n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
#print n_clusters_
#clusters = [x_metrics[labels == i] for i in xrange(n_clusters_)]
#print metrics.accuracy_score(y, pr)
#joblib.dump(clf, 'rand_forest_model_1.pkl') 

