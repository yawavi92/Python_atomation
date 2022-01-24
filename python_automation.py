# http requests
import requests 

# web scraping 
from bs4 import BeautifulSoup 
# send email
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#system date and time manipulation
import datetime
now = datetime.datetime.now()

# email content placerholder
content = ""

# extracting hacher news stories

def extract_news (url):
    print ('Extract Hacker News Stories ...')
    cnt = ''
    cnt+= ('<b>HN Top Stories :</b>\n' + 'br' + '-'*50 + '<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup (content, 'html.parser')
    for i, tag in enumerate (soup.find_all('div', attrs = {'class':'title' 'valign' :''})):
        cnt+= ((str(i+1)+'-' + tag.text + "\n" + '<br>' )if tag.text!= 'More' else '')
        #print (tag.pretty) # find_all ('span', attrs={'class' : sitestr'})
    return (cnt)

cnt = extract_news('https://news.ycombinator.com/')
content+= cnt
content+= ('<br>------<br>')
content+= ('<br><br>end of Message') 

#lets send the email
print('composing Email ...')

# update your email details
SERVER = 'smtp.gmail.com' # your smtp server
PORT = 587 # your port number
FROM = '****'# your from email id
TO = '***' # your to email ids  # can be a list
PASS = '***' # your email id's password

# fp  = open  (file_name, 'rb')

# create a text /plain message
# msg = MIMEText('')
msg = MIMEMultipart()

# msg.add_header('Content-Disposition, 'attachment', filename= 'empty.text')
msg['Subject'] = 'Top News Stories HN [Automated Email]' + '' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO 

msg.attach(MIMEText(content, 'html')) 
#fp.close()

print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
#server = smtplib.SMPT_SSL('smtp.gmail.com', 465)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.ehlo
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email.sent ...')

server.quit()
