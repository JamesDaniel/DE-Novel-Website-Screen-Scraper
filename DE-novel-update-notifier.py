from twilio.rest import TwilioRestClient
from bs4 import BeautifulSoup
import urllib2
import time
import os

def sendSMS(message):
    client = TwilioRestClient(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
    client.messages.create(to=os.environ['USER_PHONE'], from_=os.environ['TWILIO_PHONE'], body=message)
def getURL(book,chapter):
    return 'http://www.wuxiaworld.com/desolate-era-index/de-book-'+ str(book) +'-chapter-'+ str(chapter) +'/'
def txtInPar(text, html):
    soup = BeautifulSoup(html, 'html.parser')
    for txt in soup.find_all('p'):
        if text in txt.text:
            return True
    return False
book = 21
chapter = 1
num_sms_sent = 0
 
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

while True:
    url = getURL(book,chapter)
    request = urllib2.Request(url, headers=hdr)
    response = urllib2.urlopen(request)
    html_doc = response.read()
    if not txtInPar('Chapter teaser below!', html_doc):
        print 'New Desolate Era released!'
        sendSMS('New Desolate Era released!')
        num_sms_sent = num_sms_sent + 1
        chapter = chapter + 1
    else:
        print 'no new chapter yet'
    if num_sms_sent > 4 :
        break
    time.sleep(30)
