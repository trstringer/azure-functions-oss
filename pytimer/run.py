"""Python Azure Function sample"""

import http.client
import json

connection = http.client.HTTPConnection('quotesondesign.com')
connection.request(
    'GET',
    '/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1'
)

res = connection.getresponse()
quote = json.loads(res.read())[0]['content']

print('... {}'.format(quote[3:-5]))
