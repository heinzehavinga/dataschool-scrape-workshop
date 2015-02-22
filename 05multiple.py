#Here we import the libraries
#requests is a library to make webcalls
#beautifulsoup is our scraping library
#unicodecsv is a replacement for the normal Python csv library, this on supports unicode characters
import requests, unicodecsv
from bs4 import BeautifulSoup
from datetime import date, timedelta

#setting up our CSV file, making sure we have headers
writer = unicodecsv.writer(open('kijkcijfertabelrange.csv', 'wb'), encoding='utf-8',delimiter=';', dialect='excel',quotechar='"')

writer.writerow([
					'date',
					'zender',
					'kdh',
					'madl',
					'abs',
					])

date_range = range(14)
for number in date_range:
	#getting our html file
	
	r = requests.get('https://kijkonderzoek.nl/component/com_kijkcijfers/Itemid,133/file,dt-%d-0-0-p' % number)
	#Making it a beautiful soup object
	soup = BeautifulSoup(r.text)

	#Skip the table, we've got a row with a class name!
	rows = soup.findAll('tr', {'class':'kc_datarow'})

	#Calculate a date
	d = date.today() - timedelta(days=number)

	#This might take some time, so some prints might be nice
	print d.strftime('%m/%d/%Y')

	for row in rows:
		#a DOM thinks of objects nested in objects as children
		cells = row.findChildren()

		#writing it all to the CSV file	
		writer.writerow([
							d.strftime('%m/%d/%Y'),
							cells[0].text,
							cells[1].text,
							cells[2].text,
							cells[3].text
						])

#done!
print "We're done here!"