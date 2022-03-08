from tkinter.constants import TRUE
import requests
from bs4 import BeautifulSoup

url = "https://mkm.yildiz.edu.tr/duyurular"
page = requests.get(url)
soup =BeautifulSoup(page.content,"html.parser")
soup2= BeautifulSoup(page.content,"lxml")
results = soup.findAll('div',{'id':'one_news_text'})

days=[]
months=[]
titles=[]
links=[]
links7=set()
resultlinks=[]
links3=[]#links by deleting some parts
links5=[]
links6=[]
links8=[]
for div in results:
    for day in div.find("span", style="font-weight:bold;color:#353535;font-size:24px;float:left;width:51px;padding: 15px 0 0 17px;display:inline;"):
        days.append(day.text.strip())
   
    for month in div.find("span", style="color:#FFF;font-size:9.4px;float:left;width:51px;padding:2px 0 0 10px;"):
        months.append(month.text.strip())    
    
    for title in div.find("span", style="font-family:Tahoma, Geneva, sans-serif;font-weight:bold;font-size:11px;"):
        titles.append(title.text.strip())    
    
    for linc in div.find("div",id="all_news_title"):
        links.append(str(linc))

link2=['\n']

links=[x for x in links if x not in link2]
for string in links:
    
    links3.append(string.replace("</span></a>","").replace('<span style="font-family:Tahoma, Geneva, sans-serif;font-weight:bold;font-size:11px;">','').split(">"))
    
    for link in links3:
        
        for indx,lin in enumerate(link):
            
            if indx==0:
                
                links5.append(lin)
            
            else:
                
                links6.append(lin)

for string in links6:
    
    if string not in links7:
        
        links7.add(string)
        
        resultlinks.append(string)

for item in links5:
    links8.append(item.lstrip('<a href=').strip('"'))

dmt2=[]
dmt=list(zip(days,months,resultlinks,links8))
for item in dmt:
    dmt2.append(list(item))
list9= list(map(' '.join,dmt2))


print(list9)