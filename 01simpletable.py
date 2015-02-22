#Here we import the libraries
#requests is a library to make webcalls
#beautifulsoup is our scraping library
#unicodecsv is a replacement for the normal Python csv library, this on supports unicode characters
import requests, unicodecsv
from bs4 import BeautifulSoup

#setting up our CSV file, making sure we have headers
writer = unicodecsv.writer(open('kijkcijfertabel1.csv', 'wb'), encoding='utf-8',delimiter=';', dialect='excel',quotechar='"')

writer.writerow([
					'zender',
					'kdh',
					'madl',
					'abs',
					])


#getting our html file
r = requests.get('https://kijkonderzoek.nl/component/com_kijkcijfers/Itemid,133/file,dt-0-0-0-p')
#Making it a beautiful soup object
soup = BeautifulSoup(r.text)

#looking for the right table
table = soup.find('table',id='kc_tabledata')
#looking for the right rows, We don't want the header rows.
rows = table.findAll('tr', {'class':'kc_datarow'})

for row in rows:
	#a DOM thinks of objects nested in objects as children
	cells = row.findChildren()

	#writing it all to the CSV file	
	writer.writerow([
						cells[0].text,
						cells[1].text,
						cells[2].text,
						cells[3].text
					])

#done!
print "We're done here!"