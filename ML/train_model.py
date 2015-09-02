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

df = pandas.read_csv('data_exp.csv', encoding='utf_7').values
df = map(lambda x: map(lambda x: float(x), x), df)
df = numpy.array(df)

x = df[:, 1: -1]
x = numpy.delete(x, [3 + i * 11 for i in xrange(6)], axis=1)
#print x[0]
#x = normalize(x, axis=0)
#x = scale(x, axis=0)
y = df[:, -1]
y = map(lambda x: int(x), y)
def f6(x):
    if x == 6:
        return 2
    elif x == 7:
        return 6
    else:
        return x


y = map(f6, y)
y = numpy.array(y)

sm = SMOTE(kind='regular')
for i in xrange(10):
    x, y = sm.fit_transform(x, y)


clf = RandomForestClassifier(n_estimators=100, class_weight='auto')
#pr = cross_validation.cross_val_predict(clf, x, y, cv=10)
clf.fit(x,y)
#print metrics.accuracy_score(y, pr)
#print metrics.confusion_matrix(y, pr) 
joblib.dump(clf, 'rand_forest_model_1.pkl') 

