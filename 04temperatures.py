#Here we import the libraries
#requests is a library to make webcalls
#beautifulsoup is our scraping library
#unicodecsv is a replacement for the normal Python csv library, this on supports unicode characters
#New on this one is 're' which allows for regular expressions
import requests, re
from bs4 import BeautifulSoup

#getting our html file
r = requests.get('http://www.knmi.nl/cms/content/23519/kouderecord_van_nederland')
#Making it a beautiful soup object
soup = BeautifulSoup(r.text)
article = soup.find('div',{'class':'article'})
#Quickly get only link containing the word Apple (or apple because IGNORECASE)
values = re.findall('-?([0-9]+)(,[0-9]+)?(?=\s?graden)',article.text)
for value in values:
	print ''.join(value)
#done!
