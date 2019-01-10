from bs4 import BeautifulSoup
import requests
import urllib
import os
page = requests.get ("https://www.shitpostbot.com/gallery/sourceimages")
soup = BeautifulSoup (page.content, 'html.parser')
imgs=soup.find_all ('div', class_='img')
all_links=[]
for i in imgs:
    all_links.append (str(i.find('a')))
all_links_new=[]
for a in all_links:
    all_links_new.append("https://www.shitpostbot.com/img/sourceimages" + (a.split("\"")[1][12:]) + ".jpeg")
counter=1

for a in all_links_new:
    print (a)
    image = urllib.urlopen (a).read()
    with open ("data/" + "img" + str(counter)+".jpg", "wb+") as f:
        f.write (image)
    counter +=1

'''image = urllib.urlopen("https://www.shitpostbot.com/img/sourceimages/my-shiny-teeth-and-me-59a629346570a.jpeg").read()
with open ("data/" + "image.jpeg", "wb+") as f:
    f.write (image)
print (image)'''
'''ua=UserAgent()
header = {'User-Agent':str(ua.chrome)}
image=requests.get('https://www.shitpostbot.com/sourceimage/my-shiny-teeth-and-me-59a629346570a.jpeg', headers=header)
with  open("data/"+"hello.html", "wb+") as f:
        f.write (image.content)'''