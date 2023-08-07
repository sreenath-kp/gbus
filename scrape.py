from bs4 import BeautifulSoup
import requests

def scraperes(source,des):

    list1=['thiruvananthapuram','kollam','pathanamthitta','alappuzha','kottayam','ernakulam','thrissur','palakkad','malappuram','kozhikode','wayanad','kannur','kasargod']
    list2=['thiruvananthapuram-(tvm)','kollam-bs-(klm)','pathanamthitta-(pta)','alappuzha-bs-(alp)','kottayam-bs-(ktm)','ernakulam-bs-(ekm)','thrissur-bs-(tsr)','palakkad-(plk)','malappuram-(mlp)','kozhikode-(kkd)','kannur-bs-(knr)','kasaragod-bs-(kgd)']
    if(source.lower() in list1):
        source=list2[list1.index(source)]


    if(des.lower() in list1):
        des=list2[list1.index(des)]

    url='https://www.aanavandi.com/search/results/source/'+source.lower()+'/destination/'+des.lower()+'/timing/all'
    html=requests.get(url)
    # print(url)
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')
    try:
        results=soup.find(class_='searchresults')
        res=results.find_all('div',class_='trip wow fadeIn') # type: ignore
        for r in res:
            bus = r.find('div',class_='timings')
            if(bus!=None):
                print(bus.text)
            
    except:
        print("No buses available")