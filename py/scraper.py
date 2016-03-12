from BeautifulSoup import *
import urllib, json

def imdbscraper(movieData):
	query = urllib.urlencode ( { 'q' : movieData+" imdb" } )
	response = urllib.urlopen ('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	jsonObj = json.loads(response)
	result = jsonObj [ 'responseData' ] [ 'results' ]
	url = result[0]['url']
	r = urllib.urlopen (url).read()
	soup = BeautifulSoup(r)
	storyline = soup.find("div", {"itemprop": "description" }).contents[0]
	name = soup.find("h1", {"itemprop": "name" }).contents[0]
	releasedate = soup.find("a", {"title": "See more release dates" }).contents[0]
	runtime = soup.find("time", {"itemprop": "duration"}).contents[0]
	pgrating = soup.find("meta", {"itemprop": "contentRating"}).contents[0]
	rating = soup.find("span", {"itemprop": "ratingValue"}).contents[0]
	return {"rating": rating, "pgrating": pgrating, "runtime": runtime, 
	"releasedate": releasedate, "name": name, "storyline": storyline}

def rottentomatoScraper(movieData):
	query = urllib.urlencode ( { 'q' : movieData+" rotten tomatoes" } )
	response = urllib.urlopen ('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	jsonObj = json.loads(response)
	result = jsonObj [ 'responseData' ] [ 'results' ]
	url = result[0]['url']
	r = urllib.urlopen (url).read()
	soup = BeautifulSoup(r)
	#add image, cast members, genre, reviews
	criticConsensus = soup.find("div", {"class": "critic_consensus tomato-info noSpacing superPageFontColor"}).contents[0]
	criticRating = soup.find("span", {'itemprop': "ratingValue"}).contents[0]
	userRating = soup.find("span", {'itemprop': "ratingValue"}).contents[1]
	return {"criticConsensus": criticConsensus, "criticRating": criticRating,
	"userRating": userRating, }

def finalScraper(movieData):
	imdb = imdbscraper(movieData)
	rotten = rottentomatoScraper(movieData)
	return { "name": imdb["name"],
			 "image": ####[rotten["image"]], 
			 "ratings": [imdb["rating"], rotten["criticRating"], rotten["userRating"]], 
			 "storyline": imdb["storyline"],
			 "cast": ############
			 "genre": ############
			 "runtime": imdb["runtime"],
			 "pgrating" : imdb["pgrating"],
			 "releasedate": imdb["releasedate"],
			 "criticConsensus": imdb["crticConsensus"]
			 }




	





