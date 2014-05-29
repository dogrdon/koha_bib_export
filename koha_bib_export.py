#!/usr/bin/env python

import base64
import mechanize
import keys

headers = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0')]

user = keys.user
passwd = keys.passwd
domain = keys.domain
export_path = '/cgi-bin/koha/tools/export.pl'

url = domain + export_path

total = 100
incre = 10
curr = 1
stop = 10


b = mechanize.Browser()

b.addheaders = headers
#b.addheaders.append(('Authorization', 'Basic %s' % base64.encodestring('%s:%s' % (user, passwd))))

b.set_handle_robots(False)

b.open(url)

b.select_form(nr=0)

b["userid"] = user
b["password"] = passwd

b.submit()


while stop < total + 1:

	b.select_form(nr=3)
	

	b["StartingBiblionumber"] = str(curr)
	b["EndingBiblionumber"] = str(stop)

	data = b.submit()

	res = data.read()
	print curr, stop, '====\n', res, '====\n' #this is a string that can be saved to marc or xml

	curr = stop + 1
	stop += incre

	b.open(url)

