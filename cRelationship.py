#!/usr/bin/env python
from cPriorityDictionary import PriorityDictionary
from cPreprocess import Preprocess
import matplotlib.pyplot as plt
import numpy as np
import time, threading, math

# from matplotlib.backends.backend_pdf import PdfPages


class Relationship():
	def __init__(self):
		pass

	def findRelationship(self,data):
		recordCount = 0
		relationship = dict()
		for record in data:
			record = record.split() #record[1] -> white record[3] -> black
			player = record[1]
			competitor = record[3]
			numCompetitor = 1
			if(relationship.has_key(player) == False):
				competitors = dict()
				competitors[competitor]=numCompetitor
				relationship[player]=competitors
				recordCount = recordCount + 1
			else:
				competitors = relationship[player]

				#update at 2012-07-04 23:13, improve efficiency
				competitors[competitor]  = 1 + competitors.get(competitor,0)
				
				# # Old Code 
				# if(competitors.has_key(competitor)==False):
				# 	competitors[competitor]=numCompetitor
				# else:
				# 	numCompetitor = competitors[competitor]
				# 	competitors[competitor] = numCompetitor+1


				relationship[player] = competitors
				recordCount = recordCount + 1

			# let competitor as player
			if(relationship.has_key(competitor) == False):
				competitors = dict()
				competitors[player]=numCompetitor
				relationship[competitor]=competitors
				recordCount = recordCount + 1
			else:
				competitors = relationship[competitor]

				#update at 2012-07-04 23:15, improve efficiency
				competitors[player] = 1 + competitors.get(player,0)

				# # old Code 
				# if(competitors.has_key(player) == False):
				# 	competitors[player] = numCompetitor
				# else:
				# 	numCompetitor = competitors[player]
				# 	competitors[player] = numCompetitor + 1

				relationship[competitor] = competitors
				recordCount = recordCount + 1
		print 'totally process ' + str(recordCount) + ' relationship records!'
		return relationship

	def cleanRelationship(self,relationship,Flag): #Example ('scottw', {'wms': 2, 'spelletjes': 1}), r[0]=scottw, r[1][0]=wms, r[1][1]=1
		relationshipItems = relationship.items()
		recordCount = 0
		if (Flag =='createGraph'):
			relationshipList = []
			for r in relationshipItems:
				degree = 0 
				key = r[0]
				count = 0 
				values = ''
				tmp = r[1].items()
				for t in tmp:
					degree = degree + 1
					count = count + t[1]
					t = t[0]+'('+str(t[1])+')'
					values = values + t + ' '
				count = '('+str(degree)+'/'+str(count)+')'
				record = key+ count + ': ' + values
				relationshipList.append(record)
				recordCount = recordCount + 1
			print 'totally process ' + str(recordCount) + ' relationshipList records for Create Graph!'
			return relationshipList

		elif(Flag == 'DegreeDistribution'):
			degreeList = []
			for r in relationshipItems:
				degree = 0
				key = r[0]
				values = ''
				tmp = r[1].items()
				for t in tmp:
					degree = degree + 1
				# record = key+ ' ' + str(degree)
				degreeList.append(degree)
				recordCount = recordCount + 1
			degreeList.sort()
			print 'totally process ' + str(recordCount) + ' degreeList records for Degree Distribution!'
			return degreeList

		# elif (Flag == 'ShortPath'):
		# 	graph = {}
		# 	for r in relationshipItems:
		# 		key = r[0]
		# 		values = r[1]
		# 		graph[key] = values.keys()
		# 		recordCount = recordCount + 1
		# 	print 'totally process ' + str(recordCount) + ' graph records for Short Path!'
		# 	return graph
			
		# elif (Flag == 'PlayerList'):
		# 	playerList = []
		# 	for r in relationshipItems:
		# 		player = r[0]
		# 		playerList.append(player)
		# 		recordCount = recordCount + 1
		# 	print 'totally process ' + str(recordCount) + ' graph records for Player List!'
		# 	print playerList.sort()
		# 	return playerList.sort()

	def plotDegreeDistribution(self,degreeList,GameCount,dataType, gameType):
		

		p = Preprocess()

		cachePath = '/home/yotoo/Project/comparison/'
		plotPath   = '/home/yotoo/Project/logPlot/'
		# details about the data
		maximum = degreeList[len(degreeList)-1]
		dist = {}
		for d in degreeList:
			for i in range(1,maximum+1):
				if (d == i):
					if(dist.has_key(i)==False):
						dist[i] = 1
					else:
						degree = dist[i]
						degree = degree + 1
						dist[i] = degree
				else:
					continue
		print dist.items()



		# plot degree distribution 
		degrees = dist.keys()
		players = dist.values()
		

		#details about this distribution
		sortedP = dist.values()
		sortedP.sort()

		sortedD = dist.keys()
		sortedD.sort()
		minimum = sortedP[0]
		sortedP.reverse()
		maximum = sortedP[0]
		playerCount = len(players)
		degreeCount = len(degrees)

		medianIndex = (minimum + degreeCount) / 2
		Q1Index  = (minimum + medianIndex) / 2
		Q3Index = (medianIndex + degreeCount) / 2
		median = sortedD[medianIndex]
		Q1 = sortedD[Q1Index]
		Q3 = sortedD[Q3Index]

		kurtosis = self.getKurtosisSkewness(degrees)


		plotText = 'Total Games: %d \nTotal Players: %d \nMaximum Degree: %d \nQ3 Degree: %d\nMedian Degree: %d \nQ1 Degree: %d \nMinimum Degree: %d \nKurtosis: %.2e' %(GameCount,playerCount,maximum,Q3,median,Q1,minimum,kurtosis)

		#dataType
		if (dataType == 'Real Data'):
			savePath = plotPath + 'real_data/'
			if (gameType == '19+ranked'):
				title = 'Degree Distribution(Border size: 19; Game Type: Ranked)'
				# # original 
				plt.grid(True)
				plt.xlabel('Degree')
				plt.ylabel('Players')
				plt.title(title)
				plt.plot(degrees,players,'ro',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' original' + ".png")
				plt.show()
				# # log degree
				plt.grid(True)
				plt.xlabel('Log Degree')
				plt.ylabel('Players')
				plt.title(title)
				plt.semilogx(degrees,players,'ro',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' log x' + ".png")
				plt.show()
				# # log players
				plt.grid(True)
				plt.xlabel('Degree')
				plt.ylabel(' Log Players')
				plt.title(title)
				plt.semilogy(degrees,players,'ro',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' log y' + ".png")
				plt.show()
				# # log degrees and players
				plt.grid(True)
				plt.xlabel('Log Degree')
				plt.ylabel('Log Players')
				plt.title(title)
				plt.loglog(degrees,players,'ro',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' log x y' + ".png")
				plt.show()
				# # plot 4-up images for original, log x and y, log x, log y
				# original 
				plt.subplot(221)
				plt.plot(degrees,players,'ro')
				plt.title('Original Plot')
				plt.grid(True)
				#log degrees
				plt.subplot(222)
				plt.semilogx(degrees,players,'ro')
				plt.title('Log Degrees')
				plt.grid(True)
				#log players
				plt.subplot(223)
				plt.semilogy(degrees,players,'ro')
				plt.title('Log Players')
				plt.grid(True)
				#log degrees and players
				plt.subplot(224)
				plt.loglog(degrees,players,'ro')
				plt.title('Log Degrees and Players')
				plt.grid(True)
				plt.savefig(savePath + "random_data_19_ranked_4_ups.png")
				plt.show()
				p.save(dist,cachePath+title+'.txt')

			elif (gameType == '19+free'):
				title = 'Degree Distribution(Border size: 19; Game Type: Free)'
				# # original 
				plt.grid(True)
				plt.xlabel('Degree')
				plt.ylabel('Players')
				plt.title(title)
				plt.plot(degrees,players,'gs',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' original' + ".png")
				plt.show()
				# # log degree
				plt.grid(True)
				plt.xlabel('Log Degree')
				plt.ylabel('Players')
				plt.title(title)
				plt.semilogx(degrees,players,'gs',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' log x' + ".png")
				plt.show()
				# # log players
				plt.grid(True)
				plt.xlabel('Degree')
				plt.ylabel(' Log Players')
				plt.title(title)
				plt.semilogy(degrees,players,'gs',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' log y' + ".png")
				plt.show()
				# # log degrees and players
				plt.grid(True)
				plt.xlabel('Log Degree')
				plt.ylabel('Log Players')
				plt.title(title)
				plt.loglog(degrees,players,'gs',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' log x y' + ".png")
				plt.show()
				# # plot 4-up images for original, log x and y, log x, log y
				# original 
				plt.subplot(221)
				plt.plot(degrees,players,'gs')
				plt.title('Original Plot')
				plt.grid(True)
				#log degrees
				plt.subplot(222)
				plt.semilogx(degrees,players,'gs')
				plt.title('Log Degrees')
				plt.grid(True)
				#log players
				plt.subplot(223)
				plt.semilogy(degrees,players,'sg')
				plt.title('Log Players')
				plt.grid(True)
				#log degrees and players
				plt.subplot(224)
				plt.loglog(degrees,players,'sg')
				plt.title('Log Degrees and Players')
				plt.grid(True)
				plt.savefig(savePath + "random_data_19_free_4_ups.png")
				plt.show()
				p.save(dist,cachePath+title+'.txt')


			elif (gameType == '9+free'):
				title = 'Degree Distribution(Border size: 9; Game Type: Free)'
				# # original 
				plt.grid(True)
				plt.xlabel('Degree')
				plt.ylabel('Players')
				plt.title(title)
				plt.plot(degrees,players,'b^',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' original' + ".png")
				plt.show()
				# # log degree
				plt.grid(True)
				plt.xlabel('Log Degree')
				plt.ylabel('Players')
				plt.title(title)
				plt.semilogx(degrees,players,'b^',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' log x' + ".png")
				plt.show()
				# # log players
				plt.grid(True)
				plt.xlabel('Degree')
				plt.ylabel(' Log Players')
				plt.title(title)
				plt.semilogy(degrees,players,'b^',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' log y' + ".png")
				plt.show()
				# # log degrees and players
				plt.grid(True)
				plt.xlabel('Log Degree')
				plt.ylabel('Log Players')
				plt.title(title)
				plt.loglog(degrees,players,'b^',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' log x y' + ".png")
				plt.show()
				# # plot 4-up images for original, log x and y, log x, log y
				# original 
				plt.subplot(221)
				plt.plot(degrees,players,'b^')
				plt.title('Original Plot')
				plt.grid(True)
				#log degrees
				plt.subplot(222)
				plt.semilogx(degrees,players,'b^')
				plt.title('Log Degrees')
				plt.grid(True)
				#log players
				plt.subplot(223)
				plt.semilogy(degrees,players,'b^')
				plt.title('Log Players')
				plt.grid(True)
				#log degrees and players
				plt.subplot(224)
				plt.loglog(degrees,players,'b^')
				plt.title('Log Degrees and Players')
				plt.grid(True)
				plt.savefig(savePath + "random_data_9_free_4_ups.png")
				plt.show()
				p.save(dist,cachePath+title+'.txt')


		elif (dataType == 'Random Data'):
			savePath = plotPath + '/random_data/'
			if (gameType == '19+ranked'):

				title = 'Degree Distribution(Border size: 19; Game Type: Ranked) *random '
				# # original 
				plt.grid(True)
				plt.xlabel('Degree')
				plt.ylabel('Players')
				plt.title(title)
				plt.plot(degrees,players,'ro',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' original' + ".png")
				plt.show()
				# # log degree
				plt.grid(True)
				plt.xlabel('Log Degree')
				plt.ylabel('Players')
				plt.title(title)
				plt.semilogx(degrees,players,'ro',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' log x' + ".png")
				plt.show()
				# # log players
				plt.grid(True)
				plt.xlabel('Degree')
				plt.ylabel(' Log Players')
				plt.title(title)
				plt.semilogy(degrees,players,'ro',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' log y' + ".png")
				plt.show()
				# # log degrees and players
				plt.grid(True)
				plt.xlabel('Log Degree')
				plt.ylabel('Log Players')
				plt.title(title)
				plt.loglog(degrees,players,'ro',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' log x y' + ".png")
				plt.show()
				# # plot 4-up images for original, log x and y, log x, log y
				# original 
				plt.subplot(221)
				plt.plot(degrees,players,'ro')
				plt.title('Original Plot')
				plt.grid(True)
				#log degrees
				plt.subplot(222)
				plt.semilogx(degrees,players,'ro')
				plt.title('Log Degrees')
				plt.grid(True)
				#log players
				plt.subplot(223)
				plt.semilogy(degrees,players,'ro')
				plt.title('Log Players')
				plt.grid(True)
				#log degrees and players
				plt.subplot(224)
				plt.loglog(degrees,players,'ro')
				plt.title('Log Degrees and Players')
				plt.grid(True)
				plt.savefig(savePath + "random_data_19_ranked_4_ups.png")
				plt.show()
				p.save(dist,cachePath+title+'.txt')


			elif (gameType == '19+free'):
				title = 'Degree Distribution(Border size: 19; Game Type: Free) *random '
				# # original 
				plt.grid(True)
				plt.xlabel('Degree')
				plt.ylabel('Players')
				plt.title(title)
				plt.plot(degrees,players,'gs',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' original' + ".png")
				plt.show()
				# # log degree
				plt.grid(True)
				plt.xlabel('Log Degree')
				plt.ylabel('Players')
				plt.title(title)
				plt.semilogx(degrees,players,'gs',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' log x' + ".png")
				plt.show()
				# # log players
				plt.grid(True)
				plt.xlabel('Degree')
				plt.ylabel(' Log Players')
				plt.title(title)
				plt.semilogy(degrees,players,'gs',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' log y' + ".png")
				plt.show()
				# # log degrees and players
				plt.grid(True)
				plt.xlabel('Log Degree')
				plt.ylabel('Log Players')
				plt.title(title)
				plt.loglog(degrees,players,'gs',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' log x y' + ".png")
				plt.show()
				# # plot 4-up images for original, log x and y, log x, log y
				# original 
				plt.subplot(221)
				plt.plot(degrees,players,'gs')
				plt.title('Original Plot')
				plt.grid(True)
				#log degrees
				plt.subplot(222)
				plt.semilogx(degrees,players,'gs')
				plt.title('Log Degrees')
				plt.grid(True)
				#log players
				plt.subplot(223)
				plt.semilogy(degrees,players,'sg')
				plt.title('Log Players')
				plt.grid(True)
				#log degrees and players
				plt.subplot(224)
				plt.loglog(degrees,players,'sg')
				plt.title('Log Degrees and Players')
				plt.grid(True)
				plt.savefig(savePath + "random_data_19_free_4_ups.png")
				plt.show()
				p.save(dist,cachePath+title+'.txt')

			elif (gameType == '9+free'):
				title = 'Degree Distribution(Border size: 9; Game Type: Free) *random '
				# # original 
				plt.grid(True)
				plt.xlabel('Degree')
				plt.ylabel('Players')
				plt.title(title)
				plt.plot(degrees,players,'b^',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' original' + ".png")
				plt.show()
				# # log degree
				plt.grid(True)
				plt.xlabel('Log Degree')
				plt.ylabel('Players')
				plt.title(title)
				plt.semilogx(degrees,players,'b^',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' log x' + ".png")
				plt.show()
				# # log players
				plt.grid(True)
				plt.xlabel('Degree')
				plt.ylabel(' Log Players')
				plt.title(title)
				plt.semilogy(degrees,players,'b^',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' log y' + ".png")
				plt.show()
				# # log degrees and players
				plt.grid(True)
				plt.xlabel('Log Degree')
				plt.ylabel('Log Players')
				plt.title(title)
				plt.loglog(degrees,players,'b^',label = plotText)
				plt.legend()
				plt.savefig(savePath + title+' log x y' + ".png")
				plt.show()
				# # plot 4-up images for original, log x and y, log x, log y
				# original 
				plt.subplot(221)
				plt.plot(degrees,players,'b^')
				plt.title('Original Plot')
				plt.grid(True)
				#log degrees
				plt.subplot(222)
				plt.semilogx(degrees,players,'b^')
				plt.title('Log Degrees')
				plt.grid(True)
				#log players
				plt.subplot(223)
				plt.semilogy(degrees,players,'b^')
				plt.title('Log Players')
				plt.grid(True)
				#log degrees and players
				plt.subplot(224)
				plt.loglog(degrees,players,'b^')
				plt.title('Log Degrees and Players')
				plt.grid(True)
				plt.savefig(savePath + "random_data_9_free_4_ups.png")
				plt.show()
				p.save(dist,cachePath+title+'.txt')
				


	def getKurtosisSkewness(self,valueList):
		summary = sum(valueList)
		N = len(valueList)
		average = float(summary) / N

		momentN4 = 0
		for i in valueList:
			momentN4 += (i - average)**4
		monent4 = momentN4 / N

		momentN3 = 0
		for i in valueList:
			momentN3 += (i - average)**4
		monent3 = momentN3 / N


		sigmaN =  0 
		for i in valueList:
			sigmaN += (i - average) ** 2
		sigma = math.sqrt (sigmaN / N )

		kurtosis = float(0)

		# keep accuracy as 2
		kurtosis = monent4 / (sigma)**2 - 3
		# skewness = monent3 / (sigma)**3

		return kurtosis
  


	def Dijkstra(self,G,start,end=None):
		D = {}	# dictionary of final distances
		P = {}	# dictionary of predecessors
		Q = PriorityDictionary()   
		Q[start] = 0
		
		for v in Q:
			D[v] = Q[v]
			if v == end: break
			
			for w in G[v]:
				vwLength = D[v] + G[v][w]
				if w in D:
					if vwLength < D[w]:
						raise ValueError, \
	  "Dijkstra: found better path to already-final vertex"
				elif w not in Q or vwLength < Q[w]:
					Q[w] = vwLength
					P[w] = v
		return (D,P)

	def shortestPath(self,G,start,end):
		D,P = self.Dijkstra(G,start,end)
		Path = []
		while 1:
			Path.append(end)
			if end == start: break
			if (P.has_key(end)==False):
				print 'no path between ' + start + ' and ' + end
				break
			else:
				end = P[end]
		Path.reverse()
		return Path

	def createPathMatrix(self,Graph,PlayerList):
		pathMatrix = {}
		length = len(PlayerList)
		print 'Total contains', length, ' players!'
		for i in range(length):
			s = PlayerList[i]
			print s
			print 
			pathList = []
			j = i + 1
			for j in range(length):
				e = PlayerList[j]
				print e 
				pathLength= len(self.shortestPath(Graph,s,e))
				if ( pathLength== 1):
					pathList.append(0)
				else:	
					pathList.append(pathLength - 2)

			pathMatrix[s] = pathList

		print 
		print pathMatrix
		print len(pathMatrix[s])
			# break
		return pathMatrix





	# def createPathMatrix2(self,Graph,PlayerList):
	# 	pathMatrix = {}
	# 	for s in PlayerList:
	# 		n = 0
	# 		pathList = []
	# 		for e in PlayerList:
	# 			n = n + 1
	# 			if (s == e):
	# 				pathList.append(0)
	# 				continue
	# 			else:
	# 				if (len(self.shortestPath(Graph,s,e)) == 1):
	# 					pathList.append(0)
	# 				else:	
	# 					pathList.append(len(self.shortestPath(Graph,s,e)) - 2)
	# 		pathMatrix[s] = pathList
	# 		print pathMatrix
	# 		print len(pathMatrix[s])
	# 		break
	# 	return pathMatrix 







####################################################################################################


	# def plotDegreeDistribution_old(self,degreeList,GameCount,Flag):
	# 	maximum = degreeList[len(degreeList)-1]
	# 	dist = {}
	# 	for d in degreeList:
	# 		for i in range(1,maximum+1):
	# 			if (d == i):
	# 				if(dist.has_key(i)==False):
	# 					dist[i] = 1
	# 				else:
	# 					degree = dist[i]
	# 					degree = degree + 1
	# 					dist[i] = degree
	# 			else:
	# 				continue
	# 	print dist.items()

	# 	# plot degree distribution 
	# 	degrees = dist.keys()
	# 	players = dist.values()
	# 	kurtosis,skewness = self.getKurtosisSkewness(degrees)


	# 	#details about this distribution
	# 	sortedP = dist.values()
	# 	sortedP.sort()

	# 	sortedD = dist.keys()
	# 	sortedD.sort()
	# 	minimum = sortedP[0]
	# 	sortedP.reverse()
	# 	maximum = sortedP[0]
	# 	playerCount = len(players)
	# 	degreeCount = len(degrees)

	# 	medianIndex = (minimum + degreeCount) / 2
	# 	Q1Index  = (minimum + medianIndex) / 2
	# 	Q3Index = (medianIndex + degreeCount) / 2
	# 	median = sortedD[medianIndex]
	# 	Q1 = sortedD[Q1Index]
	# 	Q3 = sortedD[Q3Index]


	# 	trailCount = self.getTrails(maximum,degrees,0.01)
	# 	trailPercent = round((float(trailCount )/ degreeCount) * 100, 3)

	# 	plotText = 'Total Games: '+str(GameCount) + '\nTotal Players: '+str(playerCount)+ '\nMaximum Degree: ' + str(maximum) +'\nQ3 Degree: ' + str(Q3)+ '\nMedian Degree: ' + str(median) + '\nQ1 Degree: ' + str(Q1) + '\nMinimum Degree: ' + str(minimum)  + '\nKurtosis: '+str(kurtosis) + '\nSkewness: '+str(skewness) # + '\nTrail Percentage: '+str(trailPercent) + '%'
	# 	thresholdList = [1, 0.10, 0.075, 0.05]
		
	# 	if (Flag == '9+free'):
	# 		for i in range(4):
	# 			threshold = thresholdList[i]
	# 			xMax = maximum * threshold
	# 			yMax= playerCount * threshold

	# 			title = 'Degree Distribution(Border size: 9; Game Type: Free) '+str(threshold*100)+'%'
	# 			# for better plotting
	# 			if(playerCount >50):
	# 				playerCount = playerCount
	# 			else:
	# 				playerCount = 50

	# 			plt.grid(True)
	# 			plt.xlabel('Degree --->')
	# 			plt.ylabel('Number of Players --->')
	# 			plt.title(title)
	# 			plt.xlim(minimum,xMax)
	# 			plt.ylim(1,yMax)
	# 			plt.plot(degrees,players,'b^',label = plotText)


	# 			plt.legend()
	# 			plt.savefig(title + ".png")
	# 			plt.show()


	# 		# plt.figure(1)
	# 		# plt.grid(True)
	# 		# figureLocationList = [221,222,223,224]
	# 		# for i in range(1,5):
	# 		# 	threshold = thresholdList[i-1]
	# 		# 	location = figureLocationList[i-1]
	# 		# 	xMax = maximum * threshold
	# 		# 	yMax= playerCount * threshold
	# 		# 	plt.xlim(minimum,xMax)
	# 		# 	plt.ylim(1,yMax)
	# 		# 	plt.subplot(location)
	# 		# 	plt.plot(degrees,players,'b^',label = str(threshold*100)+'%')
	# 		# 	plt.legend()
	# 		# plt.savefig('Degree Distribution(Border size: 9; Game Type: Free) 4 ups.png')
	# 		# plt.show()

				
				

		
		
	# 	elif (Flag == '19+ranked'):
			
	# 		for i in range(1,5):
	# 			threshold = thresholdList[i-1]
	# 			xMax = maximum * threshold
	# 			yMax= playerCount * threshold

	# 			title = 'Degree Distribution(Border size: 19; Game Type: Ranked) '+str(threshold*100)+'%'
	# 			# for better plotting
	# 			if(playerCount >50):
	# 				playerCount = playerCount
	# 			else:
	# 				playerCount = 50

	# 			plt.grid(True)
	# 			plt.xlabel('Degree --->')
	# 			plt.ylabel('Number of Players --->')
	# 			plt.title(title)
	# 			plt.xlim(minimum,xMax)
	# 			plt.ylim(1,yMax)
	# 			plt.plot(degrees,players,'ro',label = plotText)
	# 			plt.legend()
	# 			plt.savefig(title + ".png")
	# 			plt.show()


	# 	elif (Flag == '19+free'):	

	# 		for i in range(1,5):
	# 			threshold = thresholdList[i-1]
	# 			xMax = maximum * threshold
	# 			yMax= playerCount * threshold

	# 			title = 'Degree Distribution(Border size: 19; Game Type: Free) '+str(threshold*100)+'%'
	# 			# for better plotting
	# 			if(playerCount >50):
	# 				playerCount = playerCount
	# 			else:
	# 				playerCount = 50

	# 			plt.grid(True)
	# 			plt.xlabel('Degree --->')
	# 			plt.ylabel('Number of Players --->')
	# 			plt.title(title)
	# 			plt.xlim(minimum,xMax)
	# 			plt.ylim(1,yMax)
	# 			plt.plot(degrees,players,'gs',label = plotText)
	# 			plt.legend()
	# 			plt.savefig(title + ".png")
	# 			plt.show()


	# def plotRandomDegreeDistribution(self,degreeList,GameCount,distributionFlag,dataFlag):
	# 	maximum = degreeList[len(degreeList)-1]
	# 	dist = {}
	# 	for d in degreeList:
	# 		for i in range(1,maximum+1):
	# 			if (d == i):
	# 				if(dist.has_key(i)==False):
	# 					dist[i] = 1
	# 				else:
	# 					degree = dist[i]
	# 					degree = degree + 1
	# 					dist[i] = degree
	# 			else:
	# 				continue
	# 	print dist.items()

	# 	# plot degree distribution 
	# 	degrees = dist.keys()
	# 	players = dist.values()
		

	# 	#details about this distribution
	# 	sortedP = dist.values()
	# 	sortedP.sort()

	# 	sortedD = dist.keys()
	# 	sortedD.sort()
	# 	minimum = sortedP[0]
	# 	sortedP.reverse()
	# 	maximum = sortedP[0]
	# 	playerCount = len(players)
	# 	degreeCount = len(degrees)

	# 	medianIndex = (minimum + degreeCount) / 2
	# 	Q1Index  = (minimum + medianIndex) / 2
	# 	Q3Index = (medianIndex + degreeCount) / 2
	# 	median = sortedD[medianIndex]
	# 	Q1 = sortedD[Q1Index]
	# 	Q3 = sortedD[Q3Index]

	# 	kurtosis,skewness = self.getKurtosisSkewness(degrees)


	# 	plotText = 'Total Games: '+str(GameCount) + '\nTotal Players: '+str(playerCount)+ '\nMaximum Degree: ' + str(maximum) +'\nQ3 Degree: ' + str(Q3)+ '\nMedian Degree: ' + str(median) + '\nQ1 Degree: ' + str(Q1) + '\nMinimum Degree: ' + str(minimum)  + '\nKurtosis: '+str(kurtosis) #+ '\nSkewness: '+str(skewness) 

		
	# 	if (distributionFlag == '9+free'):
	# 		title = 'Degree Distribution(Border size: 9; Game Type: Free) *random '
	# 		# for better plotting
	# 		if(playerCount >50):
	# 			playerCount = playerCount
	# 		else:
	# 			playerCount = 50

	# 		plt.grid(True)
	# 		plt.xlabel('Degree --->')
	# 		plt.ylabel('Number of Players --->')
	# 		plt.title(title)
	# 		# # plot the log_plot for degrees, still get similar sharp with the original plot.

	# 		# plt.xlim(math.log10(minimum),math.log10(xMax))
	# 		# plt.ylim(1,yMax)
	# 		plt.loglog(degrees_log,players,'b^',label = plotText)

	# 		plt.legend()
	# 		plt.savefig(title + ".png")
	# 		plt.show()


	# 		# # plot 4-up images for original, log x and y, log x, log y
	# 		# original 
	# 		plt.subplot(221)
	# 		plt.plot(degrees,players,'b^')
	# 		plt.title('Original Plot')
	# 		plt.grid(True)

	# 		#log x,y axis
	# 		plt.subplot(222)
	# 		plt.loglog(degrees,players,'b^')
	# 		plt.title('Log Degrees and Players')
	# 		plt.grid(True)

	# 		#log x axis
	# 		plt.subplot(223)
	# 		plt.semilogx(degrees,players,'b^')
	# 		plt.title('Log Degrees')
	# 		plt.grid(True)

	# 		#log y axis
	# 		plt.subplot(224)
	# 		plt.semilogy(degrees,players,'b^')
	# 		plt.title('Log Players')
	# 		plt.grid(True)


	# 		plt.savefig("random_data_9_free_4_ups.png")
	# 		plt.show()




				
		
	# 	elif (distributionFlag == '19+ranked'):
	# 		xMax = maximum 
	# 		yMax= playerCount 

	# 		title = 'Degree Distribution(Border size: 19; Game Type: Ranked) *random '
	# 		# for better plotting
	# 		if(playerCount >50):
	# 			playerCount = playerCount
	# 		else:
	# 			playerCount = 50

	# 		plt.grid(True)
	# 		plt.xlabel('Log Degree --->')
	# 		plt.ylabel('Number of Players --->')
	# 		plt.title(title)
	# 		# plt.xlim(math.log10(minimum),math.log10(xMax))
	# 		# plt.ylim(1,yMax)
	# 		plt.loglog(degrees,players,'ro',label = plotText)
	# 		plt.legend()
	# 		plt.savefig(title + ".png")
	# 		plt.show()


	# 		# # plot 4-up images for original, log x and y, log x, log y
	# 		# original 
	# 		plt.subplot(221)
	# 		plt.plot(degrees,players,'ro')
	# 		plt.title('Original Plot')
	# 		plt.grid(True)

	# 		#log x,y axis
	# 		plt.subplot(222)
	# 		plt.loglog(degrees,players,'ro')
	# 		plt.title('Log Degrees and Players')
	# 		plt.grid(True)

	# 		#log x axis
	# 		plt.subplot(223)
	# 		plt.semilogx(degrees,players,'ro')
	# 		plt.title('Log Degrees')
	# 		plt.grid(True)

	# 		#log y axis
	# 		plt.subplot(224)
	# 		plt.semilogy(degrees,players,'ro')
	# 		plt.title('Log Players')
	# 		plt.grid(True)


	# 		plt.savefig("random_data_19_ranked_4_ups.png")
	# 		plt.show()




	# 	elif (distributionFlag == '19+free'):	
	# 		xMax = maximum 
	# 		yMax= playerCount 
	# 		title = 'Degree Distribution(Border size: 19; Game Type: Free) *random '
	# 			# for better plotting
	# 		if(playerCount >50):
	# 			playerCount = playerCount
	# 		else:
	# 			playerCount = 50

	# 		plt.grid(True)
	# 		plt.xlabel('Log Degree --->')
	# 		plt.ylabel('Number of Players --->')
	# 		plt.title(title)
	# 		# plt.xlim(math.log10(minimum),math.log10(xMax))
	# 		# plt.ylim(1,yMax)
	# 		plt.loglog(degrees,players,'gs',label = plotText)
	# 		plt.legend()
	# 		plt.savefig(title + ".png")
	# 		plt.show()



	# 		# # plot 4-up images for original, log x and y, log x, log y
	# 		# original 
	# 		plt.subplot(221)
	# 		plt.plot(degrees,players,'gs')
	# 		plt.title('Original Plot')
	# 		plt.grid(True)

	# 		#log x,y axis
	# 		plt.subplot(222)
	# 		plt.loglog(degrees,players,'gs')
	# 		plt.title('Log Degrees and Players')
	# 		plt.grid(True)

	# 		#log x axis
	# 		plt.subplot(223)
	# 		plt.semilogx(degrees,players,'gs')
	# 		plt.title('Log Degrees')
	# 		plt.grid(True)

	# 		#log y axis
	# 		plt.subplot(224)
	# 		plt.semilogy(degrees,players,'gs')
	# 		plt.title('Log Players')
	# 		plt.grid(True)


	# 		plt.savefig("random_data_19_free_4_ups.png")
	# 		plt.show()
