import pandas
import numpy
import math

from scipy.ndimage.filters import gaussian_filter1d

def   calculate_metrics(data):
    #def generateIntSequence(valString):
    #    return [int(x) for x in valString.split("_")]
    acc_x = gaussian_filter1d(data[1], 3)
    acc_y = gaussian_filter1d(data[2], 3)
    acc_z = map(lambda x: -x, gaussian_filter1d(data[3], 3))
    gyr_x = gaussian_filter1d(data[4], 3)
    gyr_y = gaussian_filter1d(data[5], 3)
    gyr_z = map(lambda x: -x, gaussian_filter1d(data[6], 3))
    tenSecDataFrame = pandas.DataFrame({"acc_x" : acc_x,
                                        "acc_y" : acc_y,
                                        "acc_z" : acc_z,
                                        "gyr_x" : gyr_x,
                                        "gyr_y" : gyr_y,
                                        "gyr_z" : gyr_z
                                        })
    means = tenSecDataFrame.mean()
    medians = tenSecDataFrame.median()
    vars_ = tenSecDataFrame.var()
    stds = tenSecDataFrame.std()
    corrs = tenSecDataFrame.corr()
    skews = tenSecDataFrame.skew()
    kurts = tenSecDataFrame.kurt()
    maxs = tenSecDataFrame.max()
    mads = tenSecDataFrame.mad()
    mins = tenSecDataFrame.min()

    def iqr(arr):
        return numpy.percentile(arr, 75) - numpy.percentile(arr, 25)
    iqrs = tenSecDataFrame.apply(iqr)

    def entropy(arr):
        arr = arr.tolist()
        probabilityArr = [ float(arr.count(x)) / float(len(arr)) for x in set(arr)]
        def logFunc(x):
            if x <> 0:
                return x * math.log(x)
            else:
                return 0
        probabilityArr[0] = logFunc(probabilityArr[0])
        return  -reduce(lambda x, y: x + logFunc(y), probabilityArr)
    entropys = tenSecDataFrame.apply(entropy)
        
    autocorrs = tenSecDataFrame.apply(lambda x: x.autocorr())
        
    def sma(seq_x, seq_y, seq_z):
        return (seq_x.abs().sum() + seq_y.abs().sum() + seq_z.abs().sum()) / seq_x.count()
    acc_sma = sma(tenSecDataFrame["acc_x"], tenSecDataFrame["acc_y"], tenSecDataFrame["acc_z"])
    gyr_sma = sma(tenSecDataFrame["gyr_x"], tenSecDataFrame["gyr_y"], tenSecDataFrame["gyr_z"])
    def energy(seq_x, seq_y, seq_z):
        return (float)(seq_x.pow(2).sum() + seq_y.pow(2).sum() + seq_z.pow(2).sum()) / (seq_x.count() * 65536)
    acc_energy = energy(tenSecDataFrame["acc_x"], tenSecDataFrame["acc_y"], tenSecDataFrame["acc_z"])
    gyr_energy = energy(tenSecDataFrame["gyr_x"], tenSecDataFrame["gyr_y"], tenSecDataFrame["gyr_z"])
    def maxInd(arr):
        arr = arr.tolist()
        return float (max([ arr.count(x) for x in set(arr)])) / len(arr)
    maxInds = tenSecDataFrame.apply(maxInd)
       
    return [means["acc_x"], maxs["acc_x"], mins["acc_x"],  medians['acc_x'], mads['acc_x'], 
            entropys['acc_x'], stds['acc_x'], skews["acc_x"], kurts["acc_x"], iqrs["acc_x"],
            means["acc_y"], maxs["acc_y"], mins["acc_y"],  medians['acc_y'], mads['acc_y'], 
            entropys['acc_y'], stds['acc_y'], skews["acc_y"], kurts["acc_y"], iqrs["acc_y"],
            means["acc_z"], maxs["acc_z"], mins["acc_z"], medians['acc_z'], mads['acc_z'], 
            entropys['acc_z'], stds['acc_z'], skews["acc_z"], kurts["acc_z"], iqrs["acc_z"],
            means["gyr_x"], maxs["gyr_x"], mins["gyr_x"],  medians['gyr_x'], mads['gyr_x'], 
            entropys['gyr_x'], stds['gyr_x'], skews["gyr_x"], kurts["gyr_x"], iqrs["gyr_x"],
            means["gyr_y"], maxs["gyr_y"], mins["gyr_y"],  medians['gyr_y'], mads['gyr_y'], 
            entropys['gyr_y'], stds['gyr_y'], skews["gyr_y"], kurts["gyr_y"], iqrs["gyr_y"],
            means["gyr_z"], maxs["gyr_z"], mins["gyr_z"], medians['gyr_z'], mads['gyr_z'], 
            entropys['gyr_z'], stds['gyr_z'], skews["gyr_z"], kurts["gyr_z"], iqrs["gyr_z"],
            data[0]
            ]

 
   
