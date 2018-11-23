import urllib2
from bs4 import BeautifulSoup
import telebot
import time

TOKEN = '735479089:AAGcJsZPDni66WmdX-UC_mRz4m1msE9lJEU'

tb = telebot.TeleBot(TOKEN)

url = "https://exploit.kitploit.com/"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib2.Request(url, headers=hdr)
data = urllib2.urlopen(req).read()

def tele(link):
    tb.send_message(794877210, str(link))
    tb.send_message(747222456, str(link))

def main()
    data1 = BeautifulSoup(data, "lxml")
    urls = data1.findAll('a')
    for i in urls:
        if "html" in str(i.get('href')):
            with open("s.txt","r") as f:
                info = f.read()
            if info != str(i.get("href")):
                tele(str(i.get("href")))
                break
            break

if __name__ == "__main__":
    while True:
        main()
        time.sleep(3000)
        
