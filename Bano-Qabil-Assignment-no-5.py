from bs4 import 
BeautifulSoup import 
requests import 
pandas as pd

url = "https://islamqa.info/en/answers/448903/repetition-of-stories-in-the-quran-with-different-wording" 
page= requests.get(url) 
Soup=BeautifulSoup(page.content,"html5") 
title=Soup.find(class_="title is-4 is-size-5-touch").text.replace("\n","") 
print(title) 
question=Soup.find(class_="single_fatwa__question text-justified").text.replace("\n","") 
print(question) 
answer=Soup.find(class_="single_fatwa__answer").text.replace("\n","") 
print(answer)

data=[[title,question,answer]] 
df=pd.DataFrame(data,columns=["title","question","answer"]) 
print(df) 
df.to_csv("Bano-Qabil-Assignment-no-5") 
print("ok")