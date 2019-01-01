import urllib3
response = urllib3.urlopen('http://www.tutorialspoint.com/python')
html = response.info()
print (html)
