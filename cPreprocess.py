#!/usr/bin/env python
import string, time, os, sys, random


class Preprocess():
	def __init__(self):
		pass

	def load(self,filename):
		f = open(filename, 'r')
		try:
		    content = f.readlines()
		finally:
			   f.close()
		return content		

	def save(self,data,filename):
		string = ''
		array = []
		f = open(filename,'w')
		try:
			if type(data) == type(string):
				f.write(data)
			if type(data) == type({}):
				for d in data.keys():
					# f.write("'" +str(d)+ "': " + str(data[d]) + ',' + '\n')
					f.write(str(d)+' ' + str(data[d])+ '\n')
			if type(data) == type([]):
				for d in data:
					f.write(str(d)+'\n')

		finally:
			f.close()

	def preprocess(self,data,flag):
		count  = 0
		if (flag == '9+ranked'):
			count  = 0
			cleandata = ''
			errorList = []
			for record in data:
				record = record.split()

				try:
					record[0] = record[0].replace('-','') #format date
					# remove records without ranks or gametype isn't 9*9
					if record[2] == '-' or record[4] == '-' or record[6] != 'ranked' or  record[7] != '9' : 
						continue
					else:
						count = count + 1
						record = record[0] + ' ' +record[1] + ' ' +record[2] + ' ' +record[3] + ' ' \
					           +record[4] + ' ' +record[5] + ' ' +record[6] + ' ' +record[7] + ' ' \
					           +record[8] + ' ' +record[9] + ' ' +record[10] + ' ' +record[11] + '\n'
					cleandata =cleandata+ record
				except IndexError:
					errorList.append(count)
					print 'Find IndexError in: ' + str(count)
					print record
			print 'process ' + str(count) + ' records!'
			print 'Find ' + str(len(set(errorList))) +' error records in processing!'
			print errorList
			return cleandata

		elif (flag == '9+free'):

			cleandata = ''
			errorList = []
			for record in data:
				record = record.split()

				try:
					record[0] = record[0].replace('-','') #format date
					# remove records without ranks or gametype isn't 9*9
					if record[2] == '-' or record[4] == '-' or record[6] != 'free' or  record[7] != '9' : 
						continue
					else:
						count = count + 1
						record = record[0] + ' ' +record[1] + ' ' +record[2] + ' ' +record[3] + ' ' \
					           +record[4] + ' ' +record[5] + ' ' +record[6] + ' ' +record[7] + ' ' \
					           +record[8] + ' ' +record[9] + ' ' +record[10] + ' ' +record[11] + '\n'
					cleandata =cleandata+ record
				except IndexError:
					errorList.append(count)
					print 'Find IndexError in: ' + str(count)
					print record
			print 'process ' + str(count) + ' records!'
			print 'Find ' + str(len(set(errorList))) +' error records in processing!'
			print set(errorList)
			return cleandata

		elif (flag == '19+ranked'):
			count  = 0
			cleandata = ''
			errorList = []
			for record in data:
				record = record.split()

				try:
					record[0] = record[0].replace('-','') #format date
					# remove records without ranks or gametype isn't 19*19
					if record[2] == '-' or record[4] == '-' or record[6] != 'ranked' or  record[7] != '19' : 
						continue
					else:
						count = count + 1
						record = record[0] + ' ' +record[1] + ' ' +record[2] + ' ' +record[3] + ' ' \
					           +record[4] + ' ' +record[5] + ' ' +record[6] + ' ' +record[7] + ' ' \
					           +record[8] + ' ' +record[9] + ' ' +record[10] + ' ' +record[11] + '\n'
					cleandata =cleandata+ record
				except IndexError:
					errorList.append(count)
					print 'Find IndexError in: ' + str(count)
					print record
			print 'process ' + str(count) + ' records!'
			print 'Find ' + str(len(errorList)) +' error records in processing!'
			print errorList
			return cleandata

		elif (flag == '19+free'):
			count  = 0
			cleandata = ''
			errorList = []
			for record in data:
				record = record.split()

				try:
					record[0] = record[0].replace('-','') #format date
					# remove records without ranks or gametype isn't 19*19
					if record[2] == '-' or record[4] == '-' or record[6] != 'free' or  record[7] != '19' : 
						continue
					else:
						count = count + 1
						record = record[0] + ' ' +record[1] + ' ' +record[2] + ' ' +record[3] + ' ' \
					           +record[4] + ' ' +record[5] + ' ' +record[6] + ' ' +record[7] + ' ' \
					           +record[8] + ' ' +record[9] + ' ' +record[10] + ' ' +record[11] + '\n'
					cleandata =cleandata+ record
				except IndexError:
					errorList.append(count)
					print 'Find IndexError in: ' + str(count)
					print record
			print 'process ' + str(count) + ' records!'
			print 'Find ' + str(len(set(errorList))) +' error records in processing!'
			print set(errorList)
			return cleandata


	def getSubset(self,CleanData,SetSize,Flag):

		if (Flag == 'Random'):
			randomData = []
			indexRange = range(0,SetSize)
			randomIndex = random.sample(indexRange,SetSize)

			for index in randomIndex:
				randomData.append(CleanData[index])

			return randomData

		elif(Flag == ''):
			pass

			# TODO: create different type of subset for comparison










