'''
Python script to generate idf values for words in a corpus
'''

import os
import math

def remove_punctuation(word):
	word = word.replace('\xe0\xa5\xa4', '')
	word = word.replace(',', '')
	word = word.replace('.', '')
	word = word.replace('(', '')
	word = word.replace(')', '')
	word = word.replace('-', '')
	word = word.replace("'", '')
	word = word.replace('"', '')
	word = word.replace('`', '')
	word = word.replace('~', '')
	word = word.replace('%', '')
	word = word.replace('?', '')
	word = word.replace(':', '')
	word = word.replace('+', '')
	word = word.replace('=', '')
	word = word.replace('^', '')
	word = word.replace('&', '')
	word = word.replace('*', '')
	word = word.replace('#', '')
	word = word.replace('@', '')
	word = word.replace('!', '')
	word = word.replace('\\', '')
	word = word.replace('/', '')
	word = word.replace('\xe2\x80\x98', '')
	word = word.replace(';', '')
	word = word.replace('\xe0\xa4\x82', '')
	word = word.replace(' ', '')
	
	return word


	
def generate_idf():
	# Director that contains all news articles
	mypath = 'corpus'
	# This dictionary stores the number of documents a unique word appears in
	words  = {}
	# Number of documents read
	N = 0

	digits = [str(i) for i in xrange(10)]
	alpha = [chr(i) for i in xrange(97, 97+26)] + [chr(i) for i in xrange(65, 65+26)]

	for (dirpath, dirnames, filenames) in os.walk(mypath):
		for filename in filenames:	
			N += 1
		
			# Open a file
			f = open(mypath + '/' + filename, 'r').read()
			f = f.split()

			# Clean the words
			for i in xrange(len(f)):
				f[i] = remove_punctuation(f[i])
				
				
			tmp_dict = set()

			# Store all disinct words from the file
			for word in f:
				if len(word) == 0: continue
				
				flag = False
				for d in digits:
					if d in word:
						flag = True
						break
				
				if flag: continue
				
				for a in alpha:
					if a in word:
						flag = True
						break
						
				if flag: continue
				
				tmp_dict.add(word)

			# Update the number of documents that the words occur in
			for word in tmp_dict:
				if word in words:
					words[word] += 1
				else:
					words[word] = 1
		break

	lst = [(key, words[key]) for key in words]
	lst.sort()
	
	f = open('idf.txt', 'w')
	# Write out the idf values in a file for later use
	for key in lst:
		f.write(key[0] + ' ' + str(math.log(N * 1.0 / key[1]))+ '\n')
		
	lst = [(math.log(N * 1.0 / words[key]), key) for key in words]
	lst.sort()
	for i in lst:
		print i[1], i[0]
		
if __name__ == '__main__':
	generate_idf()
