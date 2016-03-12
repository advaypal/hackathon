from BeautifulSoup import *
import urllib

def scraper(movieData):
	query = urllib.urlencode ( { 'q' : movieData+" imdb" } )
	response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	jsonObj = json.loads ( response )
	result = jsonObj [ 'responseData' ] [ 'results' ]	
	url = result[0]['url']
	r = urllib.urlopen (url).read()
	soup = BeautifulSoup(r)
	rating = float(soup.find("span", {"itemprop": "ratingValue"}).contents[0])
	return json.dumps({"rating": rating})



