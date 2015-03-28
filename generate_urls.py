from datetime import date, timedelta

last_day = date.today()
d = date(2013, 1, 3)

url = 'http://www.gpo.gov/fdsys/pkg/CREC-{}.zip\n'

fh = open('date_urls.txt', 'wb')

while d < last_day:
    fh.write(url.format(d.strftime('%Y-%m-%d')))
    d = d + timedelta(days=1)

fh.close()