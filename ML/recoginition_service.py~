from .utils.metrics import calculate_metrics
from sklearn.externals import joblib
from math import isnan
#from sklearn.preprocesssing import Imputer
class RecognitionService(object):
    
    def __init__(self, clf_filename, verbose):
        self.clf = joblib.load(clf_filename)  
        self.verbose = verbose

    def get_movement_class(self, preprocessed_data):
        if self.verbose:
            print '\nrecognition service: start recognition\ngot data={}'.format(preprocessed_data)
        if len(preprocessed_data) != 7 and int(preprocessed_data[0]):
            raise ValueError
  
        metrics = calculate_metrics(preprocessed_data)
        timestamp = metrics[-1]
        features = metrics[:-1]
        features = self._simple_impute(features)
        if self.verbose:
           print 'recognition service: calculated features={} for packet with timestamp={}'.format(features, timestamp)

        res_class = int(self.clf.predict(features)[0])
        if self.verbose:
           print 'recognition service: result class={}'.format(res_class)

        if self.verbose:
           print 'recognition service: stop recognition\n'

        return timestamp, res_class

    def _simple_impute(self, arr):
        def _replace_nan(value, replacer=0):
            if isnan(value):
                return replacer
            else:
                return value
        return map(_replace_nan, arr)
