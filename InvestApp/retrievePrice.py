import requests, urllib, json

# Make an API call and store the response.
url = 'http://finance.google.com/finance/info?client=ig&q=NYSEARCA:SCHH'
res = urllib.request.urlopen(url)
content = urllib.request.urlopen(url).read()
content = str(content)
contentClean = content.replace("//", "").replace('\\n', '').replace("b'", "").replace("[", "").replace("]", "").replace(" ", "")
contentClean = contentClean[:-1]

jsonRes = json.loads(contentClean)
print("Content: " + contentClean)

print("Symbol: ", jsonRes['t'])
print("Current Price: ", jsonRes['l_cur'])

