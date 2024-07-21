import pandas as pd
import requests
from bs4 import BeautifulSoup

url="https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450"
r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")
tableHeader = soup.find("thead", class_ = "ds-bg-fill-content-alternate ds-text-left")
header=tableHeader.find_all('td')
titles=[]
for i in header:
    tt=i.text
    titles.append(tt)

df=pd.DataFrame(columns=titles)
table = soup.find("tbody", class_ = "")
rows=table.find_all("tr")
for i in rows:
    data=i.find_all("td")
    row=[tr.text for tr in data]
    l=len(df)
    df.loc[l]=row

df.to_csv("T20_matches.csv")