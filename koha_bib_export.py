#!/usr/bin/env python

import mechanize
import koha_config
import os
import time


#set up headers for the bot, though i don't think we need these if we are just ignoring robot.txt all together
headers = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0')]

#set config and path information
user = koha_config.user
passwd = koha_config.passwd
domain = koha_config.domain
xml_status = koha_config.xml_status
no_items = koha_config.no_items
export_path = '/cgi-bin/koha/tools/export.pl'
data_path = './data/'+ time.strftime("%Y-%m-%d_%H%M%S") + '/'

#create path
if not os.path.exists(data_path):
	os.makedirs(data_path)

#create url
url = domain + export_path

#set export configuration
total = koha_config.total
increment = koha_config.increment
curr = 1
stop = curr + increment - 1

start_time = time.time()

#initiate and prepare bot
b = mechanize.Browser()
b.addheaders = headers
b.set_handle_robots(False) #seems to be the only surefire way to get around the robots.txt declaraction

#go bot, go!
b.open(url)

#select form (not sure if this would be different for other versions of koha - this is tested on PTFS/Liblime Academic Koha 5.8 and Community Koha 3.16)
b.select_form(nr=0)

#authenticate
b["userid"] = user
b["password"] = passwd
b.submit()


#use the export form to export bib records in increments
while stop < total + 1:

	b.select_form(nr=3)
	

	b["StartingBiblionumber"] = str(curr)
	b["EndingBiblionumber"] = str(stop)
	if xml_status == 1:
		b["output_format"] = ['xml']
	else:
		pass
	#check the dont_export_item box if you don't want items exported
	if no_items == 1:
		b.form.find_control(name="dont_export_item").items[0].selected = True
	else:
		pass
		
	print 'Getting export data records %s - %s ready, this may take a moment...' % (str(curr), str(stop))

	data = b.submit()

	print 'Writing to filesystem...'

	res = data.read()

	#print curr, stop, '====\n', res, '====\n' #this is a string that can be saved to marc or xml

	if xml_status == 1:
		filename = data_path+'export-'+ str(curr) + '-' + str(stop) + '.xml'
	else:
		filename = data_path+'export-'+ str(curr) + '-' + str(stop) + '.mrc'


	with open(filename, 'w') as f:
		f.write(res)
		f.close()

	curr = stop + 1
	stop += increment

	b.open(url)

#tell us how long it took in seconds
print time.time() - start_time, "seconds to export %s bibliographic records" %(total)

