#!/usr/bin/env python

import base64
import mechanize
import keys
import os
import time

'''
TODO:
- Log information so people know where the script is at in the export
- Make sure the script gets the extra records at the end
- switch for XML or marc
- Better directory creation so that if there is an error, it fails/picksup gracefully
- Error handling, currenlty there is none
- Track how long it is taking to run the script "Script finished, it took __ hours/min to run"
'''

headers = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0')]

user = keys.user
passwd = keys.passwd
domain = keys.domain
export_path = '/cgi-bin/koha/tools/export.pl'
data_path = './data/'+ time.strftime("%Y-%m-%d") + '/'

'''create path'''
if not os.path.exists(data_path):
	os.makedirs(data_path)

url = domain + export_path

total = 50000
incre = 5000
curr = 1
stop = 5000


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

	print 'Getting export data ready, this may take a moment...'

	data = b.submit()

	print 'Have a nice coffee?'

	res = data.read()

	print curr, stop, '====\n', res, '====\n' #this is a string that can be saved to marc or xml

	filename = data_path+'export-'+ str(curr) + '-' + str(stop) + '.mrc'

	with open(filename, 'w') as f:
		f.write(res)
		f.close()

	curr = stop + 1
	stop += incre

	b.open(url)

