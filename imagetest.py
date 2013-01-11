from wkhtmltopdf import WKhtmlToPdf
import re

# wkhtmltoimage = WKhtmlToPdf('http://web.mit.edu', '~/Desktop/AVG/wkhtmltoimage/mit4.pdf')
# wkhtmltoimage.render()

# wkhtmltoimage = WKhtmlToPdf('http://web.mit.edu', '~/Desktop/AVG/wkhtmltoimage/mit5.jpg')
# wkhtmltoimage.render()

# wkhtmltoimage = WKhtmlToPdf('http://web.mit.edu', '~/Desktop/AVG/wkhtmltoimage/mit6.jpg', crop_h=500)
# wkhtmltoimage.render()

# wkhtmltoimage = WKhtmlToPdf('http://web.mit.edu', '~/Desktop/AVG/wkhtmltoimage/mit7.jpg', crop_w=500)
# wkhtmltoimage.render()

sites = ['web.mit.edu', 'www.google.com', 'www.avg.com', 'www.espn.com', 
		'www.punahou.edu', 'www.harvard.edu', 'www.stanford.edu',
		'www.princeton.edu', 'www.usc.edu', 'www.nfl.com', 'www.yahoo.com', 'www.yale.edu',
		'www.microsoft.com', 'www.palantir.com', 'www.apple.com', 'www.wikipedia.org']


for site in sites:
	count=0
	name=re.split('\.', site)[1]
	WKhtmlToPdf(site, '~/Desktop/AVG/tests/%s.jpg' % name).render()