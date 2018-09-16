import scipy.io
from scipy.signal import butter, lfilter

#Arguments
#data: A 2-D array of dimensions (channels x samples)
#lowcut: Float
#highcut: Float
#samplingRate: Integer
#order: Integer

def butter_bandpass_filter(data, lowcut = .1, highcut = 40, samplingRate = 500, order=4):
	nyq = 0.5 * samplingRate
	low = lowcut / nyq
	high = highcut / nyq
	b, a = butter(order, [low, high], btype='band')
	y = lfilter(b, a, data)
	return y