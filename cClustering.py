#!/usr/bin/env python
from cRelationship import Relationship
import matplotlib.pyplot as plt
import numpy as np
import time, threading,random

class Clustering():
	def __init__(self):
		pass

	def  cluster(self,playerList,relationship):
		clusterDict = {}
		N = len(playerList)
		remainPlayerList = playerList
		clusterNumber = 1

		while(len(remainPlayerList)>0):
			# random select a centroid 
			n = len(remainPlayerList)
			centroidIndex =  random.randint(0,n) - 1
			centroid = remainPlayerList.pop(centroidIndex)
			connectedNode = self.getConnectedNode(centroid,playerList,relationship)
			connectedNode.sort()
			clusterName = clusterNumber
			clusterDict[clusterName] = connectedNode
			remainPlayerList = self.getRemainPlayerList(connectedNode,remainPlayerList)
			clusterNumber += 1
		# sortedClusterDict = sorted(clusterDict.items())
		return clusterDict


	# find nodes that connect with centroid 
	def getConnectedNode(self, centroid, playerList, relationship):
		R = Relationship()
		connectedNode = []
		connectedNode.append(centroid)

		for player in playerList:
			pathLength = len(R.shortestPath(relationship,centroid,player))
			if pathLength >1:
				print player
				connectedNode.append(player)
			else:
				continue
		return connectedNode



	def getRemainPlayerList(self, connectedNode, remainPlayerList):
		cLength = len(connectedNode)
		rLength = len(remainPlayerList)
		if (rLength >= cLength):
			for node in connectedNode:
				try:
					remainPlayerList.remove(node)
				except ValueError:
					print node 
					print remainPlayerList
					print connectedNode
		else:
			remainPlayerList = []
		
		return remainPlayerList

	def getIntelView(self,clusterDict):
		maxSize = 0
		minSize = 0
		playerCount = 0
		clusterCount = len(clusterDict.keys())
		plotDict = {}
		values = []
		savePath = '/home/yotoo/Project/clustering/'

		for k in clusterDict.keys():			
			length = len(clusterDict.get(k,0))
			values.append(length)
			playerCount += length

		values.sort(reverse =True)
		maxSize = max(values)
		minSize = min(values)

		for i in range(1,clusterCount+1):
			plotDict[i] = values[i-1]


		print plotDict.items()


		plotText = 'Total Player Number: %d \nTotal Cluster Number: %d \nMaximum Cluster: %d \nMinimum Cluster: %d' %(playerCount,clusterCount,maxSize,minSize)
		title = 'Clustering Result for test data'
		plt.grid(True)
		plt.xlabel('Cluster')
		plt.ylabel('Players')
		plt.xlim(0,clusterCount)
		plt.title(title)
		plt.plot(plotDict.keys(),plotDict.values(),'bo-',label = plotText)
		plt.legend()
		plt.savefig(savePath + title+' original' + ".png")
		plt.show()
