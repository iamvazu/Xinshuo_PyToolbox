# Author: Xinshuo Weng
# email: xinshuo.weng@gmail.com

# this file define a set of functions which converting data type
import os
import numpy as np
import math
from itertools import islice

from check import *


######################################################### string related #########################################################
def character2onehot(character):
	'''
	In this function you need to output a one hot encoding of the ASCII character.
	'''
	assert isinteger(character) or isstring(character), 'input data type is not correct'
	
	# convert string to integer number
	if isstring(character):
		assert len(character) == 1, 'character should be a string with length 1'
		character = ord(character)

	one_hot_vec = np.zeros([self.nFeats, ], dtype='float32')
	one_hot_vec[character] = 1
	return one_hot_vec

def string2onehot(string):
	'''
	convert a string to a set of 2d one hot tensor
	'''
	assert isstring(string) and len(string) > 0, 'input should be a string with length larger than 0'
	
	one_hot_vec = [character2onehot(ord(string[0]))]
	for character in string[1:]:
		one_hot_vec = np.vstack((one_hot_vec, [character2onehot(ord(character))]))
	return one_hot_vec

def onehot2ord(onehot):
	'''
	convert one hot vector to a ord integer number
	'''
	assert isinstance(onehot, np.ndarray) and onehot.ndim == 1, 'input should be 1-d numpy array'
	assert sum(onehot) == 1 and np.count_nonzero(onehot) == 1, 'input numpy array is not one hot vector'
	return np.argmax(onehot)

def onehot2character(onehot):
	'''
	convert one hot vector to a character
	'''
	return chr(onehot2ord(onehot))

def onehot2string(onehot):
	'''
	convert a set of one hot vector to a string
	'''
	if isinstance(onehot, np.ndarray):
		onehot.ndim == 2, 'input should be 2-d numpy array'
		onehot = list(onehot)
	elif isinstance(onehot, list):
		assert CHECK_EQ_LIST([tmp.ndim for tmp in onehot]), 'input list of one hot vector should have same length'
	else:
		assert False, 'unknown error'

	assert all(sum(onehot_tmp) == 1 and np.count_nonzero(onehot_tmp) == 1 for onehot_tmp in onehot), 'input numpy array is not a set of one hot vector'
	ord_list = [onehot2ord(onehot_tmp) for onehot_tmp in onehot]
	return ord2string(ord_list)


def string2ord(string):
	'''
	convert a string to a list of ASCII character
	'''
	assert isstring(string) and len(string) > 0, 'input should be a string with length larger than 0'
	
	ord_list = []
	for character in string:
		ord_list.append(ord(character))
	return ord_list

def ord2string(ord_list):
	'''
	convert a list of ASCII character to a string
	'''
	assert isinstance(ord_list, list) and len(ord_list) > 0, 'input should be a list of ord with length larger than 0'
	assert all(isinteger(tmp) for tmp in ord_list), 'all elements in the list of ord should be integer'
	
	L = ''
	for o in ord_list:
		L += chr(o)
	
	return L

def str2float_from_list(str_list, debug=True):
	'''
	convert a list of string to a list of floating number
	'''
	if debug:
		assert islist(str_list), 'input is not a list'
		assert all(isstring(str_tmp) for str_tmp in str_list), 'input is not a list of string'
	if any(len(str_tmp) == 0 for str_tmp in str_list):
		if debug:
			print('warning: the list of string contains empty element which will be removed before converting to floating number')
		str_list = filter(None, str_list)
	return [float(str_tmp) for str_tmp in str_list]


def float2percent(number, debug=True):
	'''
	convert a floating number to a string representing percentage
	'''
	try:
		number = float(number)
	except ValueError:
		print('could not convert to a floating number')
	return '{:.1%}'.format(number)

######################################################### data structure related #########################################################
def get_subdict(dictionary, num, debug=True):	
	if debug:
		assert isdict(dictionary), 'dictionary is not correct'
		assert num > 0 and isinteger(num) and num <= len(dictionary), 'number of sub-dictionary is not correct'

	def take(num, iterable):
		return dict(islice(iterable, num))

	return take(num, dictionary.iteritems())



######################################################### data related #########################################################
def get_subdict(dictionary, num, debug=True):	
	if debug:
		assert isdict(dictionary), 'dictionary is not correct'
		assert num > 0 and isinteger(num) and num <= len(dictionary), 'number of sub-dictionary is not correct'

	def take(num, iterable):
		return dict(islice(iterable, num))

	return take(num, dictionary.iteritems())


