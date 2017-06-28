#! /usr/bin/env python
# need to change this script
from bs4 import BeautifulSoup
import requests
import emailsender
import sys
import os

def check_for_tithi(url):
    send_from = "Today's-Tithi@drikpanchang.com"
    send_to = ["karthik.dandavathi@gmail.com"]
    
    text = "None"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    html =  soup.prettify("utf-8")

    keys =[]
    vals =[]

    try:
        for row in soup.find_all("div",attrs={"class":"pnchngEleKey"}):
            keys.append(str(row.text))
        #print keys

        for row in soup.find_all("div",attrs={"class":"pnchngEleVal"}):
            #print type(row.text)
            vals.append(str(row.text))
        
        text = vals[-2]
        sub = "Today's Tithi data is:%s"%text

        email(send_from,send_to,sub,text)

    except Exception as e:
        sub = "Exception in parsing content from drikpanchang and Exception is:%s"%e
        text = "None"
        email(send_from,send_to,sub,text)

def email(send_from,send_to,sub,text):
    emailsender.send_mail(send_from,send_to,sub,text)


if __name__ == '__main__':
    url ='http://www.drikpanchang.com/?l=21555'
    check_for_tithi(url)