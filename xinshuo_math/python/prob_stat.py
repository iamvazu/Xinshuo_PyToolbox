# Author: Xinshuo Weng
# email: xinshuo.weng@gmail.com

# this file includes functions of basic probability and statistics
import math, cv2
import numpy as np
# import matplotlib.pyplot as plt

from private import safe_npdata
from xinshuo_miscellaneous import isnparray

def hist_equalization(input_data, num_bins=256, debug=True):
	'''
	convert a N-d numpy data (or list) with random distribution to a 1-d data with equalized histogram
	e.g., for the samples from a gaussian distribution, the data points are dense in the middle, the cdf increases fast
	in the middle so that the discrete cdf is sparse in the middle, the equalized data points are interpolated from cdf such
	that the density can be the same for the middle and the rest

	parameters:
		input_data:		a list or a numpy data, could be any shape, not necessarily a 1-d data, can be integer data (uint8 image) or float data (float32 image)
		num_bins:		bigger, the histogram of equalized data points is more flat

	output:
		equalized data with the same shape as input, it is float with [0, 1]
	'''
	np_data = safe_npdata(input_data)

	if debug:
		assert isnparray(np_data), 'the input data is not a numpy data'

	ori_shape = np_data.shape
	np_data = np_data.flatten()
	hist, xs = np.histogram(np_data, num_bins, density=True)	# return distribution and X's coordinates
	cdf = hist.cumsum()
	cdf = cdf / cdf[-1]			# sparse in the middle
	data_equalized = np.interp(np_data, xs[:-1], cdf)
	# plt.plot(xs[:-1], cdf, 'o')
	# plt.plot(np_data, data_equalized, 'o')
	# plt.show()

	return data_equalized.reshape((ori_shape))