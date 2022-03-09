#importing needed files 
from tkinter.constants import TRUE #for interface use
import requests 
from bs4 import BeautifulSoup #for scraping

days=[]
months=[]
links=[]
link2=['\n']
links3=[]#links by deleting some parts
links5=[]
links6=[]
links7=set()
links8=[]
resultlinks=[]
dmt2=[]

url = "https://mkm.yildiz.edu.tr/duyurular"
page = requests.get(url)
soup =BeautifulSoup(page.content,"html.parser")
soup2= BeautifulSoup(page.content,"lxml")
results = soup.findAll('div',{'id':'one_news_text'})
daystyle= "font-weight:bold;color:#353535;font-size:24px;float:left;width:51px;padding: 15px 0 0 17px;display:inline;"
monthstyle= "color:#FFF;font-size:9.4px;float:left;width:51px;padding:2px 0 0 10px;"
linkId= "all_news_title"
clearingStyle= '<span style="font-family:Tahoma, Geneva, sans-serif;font-weight:bold;font-size:11px;">'


def finding():
    '''finding needed html structures'''
    for div in results:
        #looping in all the html structures in the website
        for day in div.find("span", style=daystyle):
            days.append(day.text.strip())
            #finding the days in the html structure of the website
   
        for month in div.find("span", style=monthstyle):
            months.append(month.text.strip())    
            #finding the month text in the html structure of the website
  
        for linc in div.find("div",id=linkId):
            links.append(str(linc))
            #finding all the links that are needed in the html structure

def cleaning():
    '''cleaning the part of each element wich we dont need'''
    for string in links:
        #looping to clean all the links that are stored in variables
        links3.append(string.replace("</span></a>","").replace(clearingStyle,'').split(">"))
        #cleaning all the access parts
        for link in links3:
            #looping to seperate the title from the links 
            for indx,lin in enumerate(link):
                #iterating by index and appending by thier value
                if indx==0:
                
                    links5.append(lin)
            
                else:
                
                    links6.append(lin)

    for string in links6:
        #looping to see if are there any duplicates
        if string not in links7:
        
            links7.add(string)
        
            resultlinks.append(string)

    for item in links5:
        #clearing the part that didnt deleted in the first part
        links8.append(item.lstrip('<a href=').strip('"'))


finding()

links=[x for x in links if x not in link2]
#deleting the new line

cleaning()

#creating a new variable that zip all the data together 
dmt=list(zip(days,months,resultlinks,links8))

for item in dmt:
    #iterating to have list for every zipped item
    dmt2.append(list(item))

list9= list(map(' '.join,dmt2))
#joining all the part together to have a sentence
