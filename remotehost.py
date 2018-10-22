import urllib.request
import json
import math

'''
A module to compute the distances between any given number of stations provided.
In this case the json data stations is pulled from a given url, distances between any pairs of stations 
computed then the shortest euclidian distances outputed.
'''
def closestStations(*stations):
	# Using the transport API to pull stations json data from given url 
	path = "http://transportapi.com/v3/uk/places.json?query={}&type=train_station&app_id=8b9cd4d9&app_key=69eaf54e2f7d2f279a03077acab2721b"
	
	#Instantiate an empty dictionary onto which pulled data is to be appended
	pulled_stations = []

	'''Loop through all of the given stations and format each into the url
	   Use replace function to remove whitespaces within strings and replacing them with underscores
	   Finally let urllib do the rest of the job
	'''
	for i in range(len(stations)):
		url = path.format((stations[i]).replace(' ', '_'))
		response = urllib.request.urlopen(url)
		station = json.loads(response.read())
		pulled_stations.append(station)
	
	#print(pulled_stations)

	#Extract into a list the easily iterable list of members using a list comprehension
	members = list(station['member'][0] for station in pulled_stations)
	#print(members)

	#get all the unique combinations of elements in the list
	from itertools import combinations
	combs = [comb for comb in combinations(members, 2)]

	#instantiate an empty list of distances on which to append each computed distance
	distances = []

	#Loop through the combinations to get all possible distances then output the shortest distance.
	for i in range(len(combs)):
		
		if i < len(combs):

			dist = math.sqrt((combs[i][1]['latitude'] - combs[i][0]['latitude'])**2 + (combs[i][1]['longitude'] - combs[i][0]['longitude'])**2)
			distances.append(dist)

	#print(round((min(distances), 11))
	shortest = min(distances)
	print(round(shortest, 11))

if __name__ == '__main__':
	closestStations('euston', 'Mossley Hill', 'Glasgow Central')
