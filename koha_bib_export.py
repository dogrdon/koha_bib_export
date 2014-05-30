#!/usr/bin/env python

import base64
import mechanize
import keys
import os
import time

'''
TODO:
- Make sure the script gets the extra records at the end
- switch for XML or marc
- Error handling, currenlty there is none
- Track how long it is taking to run the script "Script finished, it took __ hours/min to run"
'''

headers = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0')]

user = keys.user
passwd = keys.passwd
domain = keys.domain
xml_status = keys.xml_status
export_path = '/cgi-bin/koha/tools/export.pl'
data_path = './data/'+ time.strftime("%Y-%m-%d_%H%M%S") + '/'

'''create path'''
if not os.path.exists(data_path):
	os.makedirs(data_path)

url = domain + export_path

total = 165
incre = 10
curr = 1
stop = 10

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
		#set xml status
		pass

	print 'Getting export data records %s - %s ready, this may take a moment...' % (str(curr), str(stop))

	data = b.submit()

	print 'Writing to server.'

	res = data.read()

	#print curr, stop, '====\n', res, '====\n' #this is a string that can be saved to marc or xml

	filename = data_path+'export-'+ str(curr) + '-' + str(stop) + '.mrc'

	with open(filename, 'w') as f:
		f.write(res)
		f.close()

	curr = stop + 1
	stop += incre

	b.open(url)

print time.time() - start_time, "seconds to export %s bibliographic records" %(total)

