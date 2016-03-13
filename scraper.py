#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# enable debugging

from BeautifulSoup import *
import urllib, json

def imdbscraper(movieData):
	query = urllib.urlencode({'q' : movieData + " imdb"})
	jsonObj = None
	# while jsonObj == None:
	response = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	jsonObj = json.loads(response)
		# try:
	result = jsonObj['responseData']['results']
	url = result[0]['url']
		# except:
		# 	pass
	r = urllib.urlopen (url).read()
	soup = BeautifulSoup(r)
	storyline = soup.find("div", {"itemprop": "description" }).contents[0].strip()
	name = soup.find("h1", {"itemprop": "name" }).contents[0].strip()
	releasedate = soup.find("a", {"title": "See more release dates" }).contents[0].strip()
	runtime = soup.find("time", {"itemprop": "duration"}).contents[0].strip()
	pgrating = soup.find("meta", {"itemprop": "contentRating"})['content'].strip()
	rating = soup.find("span", {"itemprop": "ratingValue"}).contents[0].strip()
	return {"rating": rating, "pgrating": pgrating, "runtime": runtime,
	"releasedate": releasedate, "name": name, "storyline": storyline}

def rottentomatoScraper(movieData):
	query = urllib.urlencode ({'q' : movieData + " rotten tomatoes"})
	jsonObj = None
	# while jsonObj['responseData'] == None:
	response = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	jsonObj = json.loads(response)
		# try:
	result = jsonObj['responseData']['results']
			# print("Hey")
		# except:
		# 	pass
	url = result[0]['url']
	r = urllib.urlopen(url).read()
	soup = BeautifulSoup(r)
	#add image, cast members, genre, reviews
	criticConsensus = soup.find("p", {"class": "critic_consensus superPageFontColor"}).contents[2].strip()
	criticRating = soup.find("span", {'itemprop': "ratingValue"}).contents[0].strip()
	userRating = soup.find("span", {'itemprop': "ratingValue"}).contents[0].strip()
	director = soup.find("span", {"itemprop": "name"}).contents[0].strip()
	cast = [span.contents[0].strip() for span in soup.findAll("span", {'itemprop': "name"})[1:4]]
	genres = [span.contents[0].strip() for span in soup.findAll("span", {'itemprop': "genre"})]
	image = soup.find("img", {"class": " posterImage"})["src"]

	r = urllib.urlopen(url + "/reviews/?type=top_critics").read()
	soup = BeautifulSoup(r)
	reviews = [div.contents[0].strip() for div in soup.findAll("div", {"class": "the_review"})[:6]]

	return {"criticConsensus": criticConsensus, "criticRating": criticRating,
	"userRating": userRating, "cast": cast, "image": image, "reviews": reviews,
	"director": director, "genres": genres}

def finalScraper(movieData):
	imdb = imdbscraper(movieData)
	rotten = rottentomatoScraper(movieData)
	return {"name": imdb["name"].replace("&nbsp;", ""),
			"image": rotten["image"],
			"ratings": [imdb["rating"], rotten["criticRating"], rotten["userRating"]],
			"storyline": imdb["storyline"],
			"cast": rotten["cast"],
			"genres": rotten["genres"],
			"runtime": imdb["runtime"],
			"pgrating" : imdb["pgrating"],
			"releasedate": imdb["releasedate"],
			"criticConsensus": rotten["criticConsensus"],
			"reviews": rotten["reviews"]
		   }
