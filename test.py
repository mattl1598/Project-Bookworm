import urllib.request

with urllib.request.urlopen('https://www.googleapis.com/books/v1/volumes?q=9780393972832') as response:
   html = response.read()