# pylint: skip-file
"""Python Azure Function sample"""

import httplib
import json

connection = httplib.HTTPConnection('quotesondesign.com')
connection.request(
    'GET',
    '/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1'
)

res = connection.getresponse()
quote = json.loads(res.read())[0]['content']

print('... {}'.format(quote[3:-5]))
