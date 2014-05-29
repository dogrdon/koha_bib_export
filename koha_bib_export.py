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

b = mechanize.Browser()

b.addheaders = headers
#b.addheaders.append(('Authorization', 'Basic %s' % base64.encodestring('%s:%s' % (user, passwd))))

b.set_handle_robots(False)

b.open(url)

b.select_form(nr=0)

b["userid"] = user
b["password"] = passwd

b.submit()

b.select_form(nr=3)

b["StartingBiblionumber"] = '2'
b["EndingBiblionumber"] = '4'

data = b.submit()

res = data.read()
print res
