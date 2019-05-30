
# coding: utf-8

# In[1]:



from bs4 import BeautifulSoup
import requests
import webbrowser

def openff():
    # This def open firefox browser.
    Jpsen = input("英語にしたい日本語を入力してください: ")
    url = "https://script.google.com/macros/s/AKfycby_dU9RymFwgEsd6txZAhA68MQAnUQxXeRnbVia_V0U8fv-Gkoy/exec?text=" + Jpsen + "&source=ja&target=en"
    browser = webbrowser.get('chrome')
    browser.open(url)
    
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return(soup.contents[0])

openff()

