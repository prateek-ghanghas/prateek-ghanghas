import requests
from bs4 import BeautifulSoup as bs
import json

URL = "https://www.producthunt.com/"

response = requests.get(URL)

html = bs(response.content, 'html5lib')

#print(html.prettify())

tags = html.find('script', attrs = {'id':"__NEXT_DATA__"}).string.strip()

data = json.loads(tags)

#print(data)

data = data["props"]["apolloState"]

ref = []

for i in data:
        if "HomefeedPageFEATURED" in i:
                for j in range(len(data[i]["items"])):
                ref.append(data[i]["items"][j]["__ref"])

info = []

try:
        for k in ref:
                maindic = {}
                dic = {}
                if "Ad" in k or "Discussion" in k or "Antholo" in k or "Collection" in k:
                      continue
                slug = data[k]["slug"]
                dic["name"] = data[k]["name"]
                dic["tagline"] = data[k]["tagline"]
                dic["votesCount"] = data[k]["votesCount"]
                dic["link"] = "https://www.producthunt.com/posts/" + slug
                maindic.update(dic)
                info.append(maindic)
except KeyError:
      pass

print(info)


