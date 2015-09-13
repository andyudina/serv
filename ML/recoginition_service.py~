from .utils.metrics import calculate_metrics
from sklearn.externals import joblib
from math import isnan
from ghmm import *
from .utils.hmm import *
#from sklearn.preprocesssing import Imputer
class RecognitionService(object):
    
    def __init__(self, clf_filename, verbose):
        self.clf = joblib.load(clf_filename)  
        self.verbose = verbose
        self._train_hmm_model()
        self.observ = []

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
        self.observ.append(res_class)
        print 'Observations: ', self.observ
        print 'Emission sequence', EmissionSequence(self.sigma, self.observ)
        res_class =  self.m.viterbi(EmissionSequence(self.sigma,self.observ))[0][-1] + 1
        print 'viterby path:',  self.m.viterbi(EmissionSequence(self.sigma,self.observ))
        #print res_class 
 
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

    def _train_hmm_model(self):
        self.sigma = IntegerRange(1,9)
        self.m = HMMFromMatrices(self.sigma, DiscreteDistribution(self.sigma), A, B, pi)
        #obs_seq = self.m.sampleSingle(20)
        #print obs_seq
        #obs = map(self.sigma.external, obs_seq)
        #print obs
        self.m.baumWelch(EmissionSequence(self.sigma, train_seq))
        #obs_seq = self.m.sampleSingle(20)
        #print obs_seq
        #obs = map(self.sigma.external, obs_seq)
        #print obs

        
