#!/usr/bin/python
import requests
import sys

# Pass movie name as parameters.
movieName = sys.argv[1]

# API-Endpint, to call omdbapi to pass the search term.
apiUrl = 'http://www.omdbapi.com/?apikey=232cc796'

# Defining the query parameter to be sent along with the GET URL.
PARAMS = {'t':movieName}

# Sending get request and getting the response as response object.
req = requests.get(url = apiUrl, params = PARAMS)

# Extracting data in json format.
data = req.json()

# Extracting the Rotten Tomatoes ratings.
if data['Response'] == "True":
        allRatings = data['Ratings']
        for x in allRatings:
                if x['Source'] == "Rotten Tomatoes":
                        print( movieName + " " "Rotten Tomaotes rating is: %s" % x['Value'])
else:
        print( movieName + "does not exist in the library")
