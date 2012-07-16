#!/usr/bin/env python
from cPreprocess import Preprocess
from cRelationship import Relationship
from scipy import linspace, polyval, polyfit, sqrt, stats, randn
# from pylab import plot, title, show , legend
import matplotlib.pyplot as plt
import numpy as np
import time, threading,random,math

class Comparison():

	def __init__(self):
		pass


	def isPowerLaw(self):
		#TODO: methods of detecting power-law
		pass


	def getPowerLawParameters(self,data):
		pass


	def linearRegression(self,data):
		savePath = '/home/yotoo/Project/comparison'
		# plot original data
		title = 'test data'
		degreeArray = []
		playerArray = []
		degreeList = []
		playerList = []

		for record in data:
			record = record.split()
			degree = int(record[0])
			player = int(record[1])
			degreeList.append(degree)
			playerList.append(player)

			degree = float(record[0])
			player = float(record[1])
			degreeArray.append(math.log10(degree))
			playerArray.append(math.log10(player))

		degreeArray = np.array(degreeArray)
		playerArray = np.array(playerArray)


		# linear regression
		n = len(degreeList)
		slope,intercept = polyfit(degreeArray,playerArray,1)
		playerRegression=polyval([degreeArray,playerArray],degreeArray)
		ms_error=sqrt(sum((playerRegression-playerArray)**2)/n)

		# plot the original data points
		plt.grid(True)
		plt.xlabel('Degree')
		plt.ylabel('Players')
		plt.title(title)
		plt.plot(degreeArray,playerArray,'bo')


		# error
		# plot regression line
		x = [x for x in range(0,5)]
		y = [i*slope+intercept for i in x]

		regressLineText = 'Slope = %.3f \nIntercept = %.3f \nMean Square Error = %.3f' %(slope,intercept,ms_error)
		plt.plot(x,y,'r.-',label = regressLineText)

		plt.legend()
		plt.savefig(savePath + title + ".png")

		plt.show()

		print regressLineText