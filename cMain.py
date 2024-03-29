#!/usr/bin/env python
import time
from cPreprocess import Preprocess
from cRelationship import Relationship
from cClustering import Clustering
from cComparison import Comparison


def main():
#############################################################
# 	Real Code

	# # initialization
	startTime = time.time()
	process = Preprocess()
	relation = Relationship()
	comparison = Comparison()
	clustering = Clustering()

#--------------------------------Preprocess Data-----------------------------------------------------------
	# data = P.load('cleandata.txt')
	# cleandata = P.preprocess(data,'19+ranked')
	# randomData = P.createRandomData(cleandata,50000)
	# P.save(cleandata,'prepro_data_19_ranked.txt')
	

	# cleandata = P.preprocess(data,'19+free')
	# P.save(cleandata,'prepro_data_19_free.txt')

	# cleandata = P.preprocess(data,'9+ranked')
	# P.save(cleandata,'prepro_data_9_ranked.txt')

	# cleandata = P.preprocess(data,'9+free')
	# P.save(cleandata,'prepro_data_9_free.txt')


	# # create random data

	# cleandata = P.load('prepro_data_19_ranked.txt')
	# randomData = P.getSubset(cleandata,50000,'Random')
	# P.save(randomData,'prepro_random_data_19_ranked.txt')

	# cleandata = P.load('prepro_data_19_free.txt')
	# randomData = P.getSubset(cleandata,50000,'Random')
	# P.save(randomData,'prepro_random_data_19_free.txt')	


	# cleandata = P.load('prepro_data_9_free.txt')
	# randomData = P.getSubset(cleandata,50000,'Random')
	# P.save(randomData,'prepro_random_data_9_free.txt')




#-----------------------------------Degree Distribution-----------------------------------------------------------

# 	data = process.load('prepro_data_19_ranked.txt')
# 	relationship = relation.findRelationship(data)
# 	gameCount = len(data)
# 	degreeList =  relation.cleanRelationship(relationship,'DegreeDistribution')
# 	relation.plotDegreeDistribution(degreeList,gameCount, 'Real Data', '19+ranked')

# 	data = process.load('prepro_data_19_free.txt')
# 	relationship = relation.findRelationship(data)
# 	gameCount = len(data)
# 	degreeList =  relation.cleanRelationship(relationship,'DegreeDistribution')
# 	relation.plotDegreeDistribution(degreeList,gameCount,'Real Data','19+free')

# # can not find records match "border size: 9 & game type: free"

# 	data = process.load('prepro_data_9_free.txt')
# 	relationship = relation.findRelationship(data)
# 	gameCount = len(data)
# 	degreeList =  relation.cleanRelationship(relationship,'DegreeDistribution')
# 	relation.plotDegreeDistribution(degreeList,gameCount,'Real Data','9+free')



# # # random data 

# 	data = process.load('prepro_random_data_19_ranked.txt')
# 	relationship = relation.findRelationship(data)
# 	gameCount = len(data)
# 	degreeList =  relation.cleanRelationship(relationship,'DegreeDistribution')
# 	relation.plotDegreeDistribution(degreeList,gameCount,'Random Data','19+ranked')

# 	data = process.load('prepro_random_data_19_free.txt')
# 	relationship = relation.findRelationship(data)
# 	gameCount = len(data)
# 	degreeList =  relation.cleanRelationship(relationship,'DegreeDistribution')
# 	relation.plotDegreeDistribution(degreeList,gameCount,'Random Data','19+free')

# # # can not find records match "border size: 9 & game type: free"

# 	data = process.load('prepro_random_data_9_free.txt')
# 	relationship = relation.findRelationship(data)
# 	gameCount = len(data)
# 	degreeList =  relation.cleanRelationship(relationship,'DegreeDistribution')
# 	relation.plotDegreeDistribution(degreeList,gameCount,'Random Data','9+free')




#------------------------------------Shortest Path-------------------------------------------------------------------
	
	# data = P.load('prepro_data_19_ranked.txt')
	# relationship = R.findRelationship(data)
	# playerList = relationship.keys()
	# playerList.sort()
	# P.save(playerList,'playerList_19_ranked.txt')
	# pathMatrix = R.createPathMatrix(relationship,playerList)
	# print pathMatrix


	# data = P.load('prepro_data_19_free.txt')
	# relationship = R.findRelationship(data)
	# playerList = relationship.keys()
	# playerList.sort()
	# P.save(playerList,'playerList_19_free.txt')
	# pathMatrix = R.createPathMatrix(relationship,playerList)
	# print pathMatrix


	# data = P.load('prepro_data_9_free.txt')
	# relationship = R.findRelationship(data)
	# playerList = relationship.keys()
	# playerList.sort()
	# P.save(playerList,'playerList_9_free.txt')
	# pathMatrix = R.createPathMatrix(relationship,playerList)
	# print pathMatrix


	# # random data 

	# data = P.load('prepro_random_data_19_ranked.txt')
	# relationship = R.findRelationship(data)
	# playerList = relationship.keys()
	# playerList.sort()
	# P.save(playerList,'playerList__random_19_ranked.txt')
	# pathMatrix = R.createPathMatrix(relationship,playerList)
	# print pathMatrix
	# P.save(pathMatrix,'pathMatrix_19_ranked.txt')


	# data = P.load('prepro_random_data_19_free.txt')
	# relationship = R.findRelationship(data)
	# playerList = relationship.keys()
	# playerList.sort()
	# P.save(playerList,'playerList_random_19_free.txt')
	# pathMatrix = R.createPathMatrix(relationship,playerList)
	# print pathMatrix
	# P.save(pathMatrix,'pathMatrix_19_free.txt')


	# data = P.load('prepro_random_data_9_free.txt')
	# relationship = R.findRelationship(data)
	# playerList = relationship.keys()
	# playerList.sort()
	# P.save(playerList,'playerList_random_9_free.txt')
	# pathMatrix = R.createPathMatrix(relationship,playerList)
	# print pathMatrix
	# P.save(pathMatrix,'pathMatrix_9_free.txt')


#------------------------------------Clustering-------------------------------------------------------------------

	# data = P.load('prepro_random_data_19_ranked.txt')
	# relationship = R.findRelationship(data)
	# gameCount = len(data)
	# playerList = relationship.keys()
	# C = Clustering()
	# clusterDict = C.cluster(playerList,relationship)
	# P.save(clusterDict,'Clustering Result_random_data_19_ranked.txt')



	# data = P.load('prepro_random_data_19_free.txt')
	# relationship = R.findRelationship(data)
	# gameCount = len(data)
	# playerList = relationship.keys()
	# C = Clustering()
	# clusterDict = C.cluster(playerList,relationship)
	# P.save(clusterDict,'Clustering Result_random_data_19_free.txt')



	# data = P.load('prepro_random_data_9_free.txt')
	# relationship = R.findRelationship(data)
	# gameCount = len(data)
	# playerList = relationship.keys()
	# C = Clustering()
	# clusterDict = C.cluster(playerList,relationship)
	# P.save(clusterDict,'Clustering Result_random_data_9_free.txt')




	# data = P.load('test_data.txt')
	# relationship = R.findRelationship(data)
	# gameCount = len(data)
	# playerList = relationship.keys()
	# C = Clustering()
	# clusterDict = C.cluster(playerList,relationship)
	# print clusterDict
	# print type(clusterDict)
	# C.getIntelView(clusterDict)


#------------------------------------Comparison-------------------------------------------------------------------

	# P.save(clusterDict,'Clustering Result_test_data.txt')

	# data = process.load('/home/yotoo/Project/comparison/Degree Distribution(Border size: 9; Game Type: Free).txt')
	
	data = process.load('/home/yotoo/Project/comparison/Degree Distribution(Border size: 19; Game Type: Ranked).txt')
	flag = '19 + Ranked'
	comparison.linearRegression(data,flag)

	data = process.load('/home/yotoo/Project/comparison/Degree Distribution(Border size: 19; Game Type: Free).txt')
	flag = '19 + Free'
	comparison.linearRegression(data,flag)

	data = process.load('/home/yotoo/Project/comparison/Degree Distribution(Border size: 9; Game Type: Free).txt')
	flag = '9 + Free'
	comparison.linearRegression(data,flag)	
	
	






	endTime = time.time()
	print 'totally use ' + str(endTime-startTime) + ' seconds!'
	

	
if "__main__" == __name__:
	main()