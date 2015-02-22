#Here we import the libraries
#requests is a library to make webcalls
#beautifulsoup is our scraping library
#unicodecsv is a replacement for the normal Python csv library, this on supports unicode characters
#New on this one is 're' which allows for regular expressions
import requests, unicodecsv,re
from bs4 import BeautifulSoup

#setting up our CSV file, making sure we have headers
writer = unicodecsv.writer(open('relevantnieuws.csv', 'wb'), encoding='utf-8',delimiter=';', dialect='excel',quotechar='"')

writer.writerow([
					'artikel',
					'link',
					])


#getting our html file
r = requests.get('http://tweakers.net/')
#Making it a beautiful soup object
soup = BeautifulSoup(r.text)

#Quickly get only link containing the word Apple (or apple because IGNORECASE)
links = soup.find_all('a',text = re.compile('Apple', re.IGNORECASE))
for link in links:
	print link
	#Another way of doing this is to check using python itself like this
	#In this case we check if the url contains "nieuws"
	if not "nieuws" in link.get('href'):
		writer.writerow([
						link.text,
						link.get('href')
					])

#done!
print "We're done here!"