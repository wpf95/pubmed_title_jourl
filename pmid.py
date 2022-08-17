import re
import requests
from bs4 import BeautifulSoup

kv = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
factor = input("请输入关键词，空格分隔,第一个默认为基因：")
page = str(input("请输入页面，默认一页20个结果："))
li = []
for z in factor.split(" "):
    li.append(z)
zjion="+".join(li)
url1 = "https://www.genecards.org/cgi-bin/carddisp.pl?gene="+ li[0]
r = requests.get(url1,headers = kv)
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
sa = soup.find_all("a",{"data-ga-action":"GWA"})
list1=[]
list2=[]
list3=[]
list4=[]
for m in sa:
    list1.append(str(m))
for n in list1:
    if 'title=' not in n:
        list2.append(str(n))
for i in list2[1:]:
    re1 = r'data-ga-source-accession=(.*?)href'
    func=re.findall(re1,i)
    list3.append(func)
for a in list3:
    b=str(a).replace('"','').replace("'","")
    list4.append(b)
print(li[0])
print([str(list4).replace("[","").replace("]","").replace("'","")])

url2 = "https://pubmed.ncbi.nlm.nih.gov/?term="+zjion+"&size=20"+"&page="+page
r2 =  requests.get(url2,headers=kv)
demo2 = r2.text
soup2 = BeautifulSoup(demo2,"html.parser")
list5=[]
for line in str(demo2).split("<"):
    list5.append(str(line))
for h in list5:
    if "log_resultcount" in h:
        re2 = r'\d+'
        num = re.findall(re2,h)
        print("pubmed共找到"+str(num).replace("['","").replace("']","")+"篇文献,第"+page+"页")

sb = soup2.find_all("span",{"class","docsum-pmid"})
list6=[]
for j in sb:
    re2 = r'\d+'
    pmid = re.findall(re2,str(j))
    list6.append(pmid)
for k in list6:
    number = str(k).replace("['","/").replace("']","/")
    url3 = "https://pubmed.ncbi.nlm.nih.gov" + number
    r3 = requests.get(url3,headers=kv)
    demo3 = r3.text
    soup3 = BeautifulSoup(demo3,"html.parser")
    st = soup3.find("title")
    sj = soup3.find("button",id="full-view-journal-trigger").attrs["title"]
    print(url3,sj)
    print(str(st).split(">")[1].split("<")[0].rstrip(" - PubMed"))




