import os
from numpy import array
from matplotlib import pyplot as plt
from os.path import expanduser

class FastaParser(object):
'''A class that parses .fasta files '''
	def __init__(self, in_path):

		self.in_path = in_path
		self.count = 0
		self.key_dict = {}
		self.value_dict = {}
		
		if not os.path.exists(self.in_path):
			raise IOError("%s can not be found." % (self.in_path))
		else: self.parse_file()

	def parse_file(self):
		'''Parses the files and puts the results into the data structure. '''
		in_file = open(self.in_path,'r')
		current_key = ""
		for line in in_file:
			line = line.strip("\n")
			if '>' in line:
				self.count += 1
				current_key = line[1:len(line)]
				self.key_dict[current_key] = current_key
				self.key_dict[(self.count-1)] = current_key
				self.value_dict[current_key] = ''
			else: 
				self.value_dict[current_key] \
					= self.value_dict[current_key] + line

	def __len__(self):
		''' Returns the number of entries in the .fasta file.'''
		return len(self.value_dict)

	def __getitem__(self,key):
		''' Returns the speciefied item from the data structur'''
		if type(key) is int:
			if self.count < key:
				raise IndexError("%s is out of bounds." % (key))
		return self.value_dict[self.key_dict[key]]

	def extract_length(self,length):
		''' Extreacts the entries that are shorter than som user specified length. '''
		return [len(self.value_dict[key]) 
			for key in self.value_dict 
				if len(self.value_dict[key]) < length]

	def length_dist(self,path_to_pdf):
		''' Plots the length distribution of the entries of the .fasta file '''
		plt.hist(array([len(self.value_dict[key]) 
			for key in self.value_dict]))
		plt.savefig(expanduser(path_to_pdf))