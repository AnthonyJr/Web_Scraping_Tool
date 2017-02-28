from lxml import html 
import requests 

def main(): 
	print " Welcome to Web Scrape 1.0! "

	read_from = input('What file are we reading from? ')

	write_to = input('Please enter the filename you want to write to? ')
	state = input('What state? Use Abbreviation ')

	w  = open('detail_counties_ky.txt', 'w+')
	f = open('counties_ky.txt', 'r+')

	for line in f: #line prints out the city name



		cityname = line.replace('\n', "")
		request ='http://citylatitudelongitude.com/' + state +'/' + cityname + '.htm'
		page = requests.get(request)
		tree = html.fromstring(page.content)
		raw_lat = tree.xpath('//*[@id="map area"]/table/tr[2]/td[1]/div/font/strong/text()')
		raw_long = tree.xpath('//*[@id="map area"]/table/tr[2]/td[2]/div/font/strong/text()')
		Latitude = raw_lat[0].replace('\n', "")
		Longitude = raw_long[0].replace('\n', "")
		#output = cityname + Longitude + Latitude + '\n'
		output = Latitude + Longitude + cityname + '\n'
		w.write(output)






	# page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
	# tree = html.fromstring(page.content)





	# print 'Buyers: ', buyers
	# print 'Prices: ', prices


main()