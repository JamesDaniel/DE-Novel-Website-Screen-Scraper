from twilio.rest import TwilioRestClient
import urllib2
import time
import os

def sendSMS(message):
    client = TwilioRestClient(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
    client.messages.create(to=os.environ['USER_PHONE'], from_=os.environ['TWILIO_PHONE'], body=message)

book = 21
chapter = 1
url = 'http://www.wuxiaworld.com/desolate-era-index/de-book-'+ str(book) +'-chapter-'+ str(chapter) +'/' 
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
request = urllib2.Request(url, headers=hdr)

while True:
    response = urllib2.urlopen(request)
    html_doc = response.read()
    if 'Chapter teaser below!' not in html_doc:
        sendSMS('New Desolate Era released!')
        chapter = chapter + 1
    time.sleep(30)
