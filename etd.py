import csv
final_list = []
with open('combined.csv', 'rU') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		resource = row['resource']
		uuid = resource.split("|uuid:")[1]
		import urllib2
		import xmltodict
		try:
			file = urllib2.urlopen('https://cdr.lib.unc.edu/content/uuid:'+uuid+'/MD_DESCRIPTIVE')
			data = file.read()
			file.close()
			affiliation = data.split("<mods:affiliation>", 1)[1].split("</mods:affiliation>")[0]
			date_published = data.split('<mods:dateIssued keyDate="yes" encoding="iso8601">', 1)[1].split("</mods:dateIssued>")[0]
			#print affiliation, uuid, date_published
			final_list.append(["<a href='https://cdr.lib.unc.edu/record/uuid:"+uuid+"'>"+row['resource']+"</a>", row['downloads'], row['uniquedownloads'],row['views'], row['uniqueviews'], affiliation, date_published, row['downloads']/row['views']])
		except:
			#print 'exception', uuid
			continue
with open("final_list.csv", "wb") as f:
	print 'writing to file'
	writer = csv.writer(f)
	writer.writerows(final_list)
