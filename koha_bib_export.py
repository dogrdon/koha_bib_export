#!/usr/bin/env python

import base64
import mechanize
import koha_koha_config
import os
import time

'''
TODO:
- Make sure the script gets the extra records at the end - or be lazy and just round up the total
- Error handling, currenlty there is none
'''

headers = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0')]

user = koha_config.user
passwd = koha_config.passwd
domain = koha_config.domain
xml_status = koha_config.xml_status
export_path = '/cgi-bin/koha/tools/export.pl'
data_path = './data/'+ time.strftime("%Y-%m-%d_%H%M%S") + '/'

'''create path'''
if not os.path.exists(data_path):
	os.makedirs(data_path)

url = domain + export_path

total = koha_config.total
#total = 266000
increment = koha_config.increment #the increments in which bib records will be downloaded in i.e. 5000 means it will export by 5000 bibliographic records at a time.
curr = 1
stop = increment

#if total % incre is not 0 well, ....

start_time = time.time()


b = mechanize.Browser()

b.addheaders = headers
#b.addheaders.append(('Authorization', 'Basic %s' % base64.encodestring('%s:%s' % (user, passwd))))

b.set_handle_robots(False) #seems to be the only surefire way to get around the robots.txt declaraction

b.open(url)

b.select_form(nr=0)

b["userid"] = user
b["password"] = passwd

b.submit()


while stop < total + 1:

	b.select_form(nr=3)
	

	b["StartingBiblionumber"] = str(curr)
	b["EndingBiblionumber"] = str(stop)
	if xml_status == 1:
		b["output_format"] = ['xml']
	else:
		pass
		
	print 'Getting export data records %s - %s ready, this may take a moment...' % (str(curr), str(stop))

	data = b.submit()

	print 'Writing to server.'

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
	stop += incre

	b.open(url)

print time.time() - start_time, "seconds to export %s bibliographic records" %(total)

