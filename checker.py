import urllib2
import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

def mail(to, subject, text):
	gmail_user = "david@bostonwebgroup.com"
	gmail_pwd = "PASSWORD"
	print "[+] Sending email to " + to 
	msg = MIMEMultipart()
	msg['From'] = gmail_user
	msg['To'] = to
	msg['Subject'] = subject
	msg.attach(MIMEText(text))
	mailServer = smtplib.SMTP("smtp.gmail.com", 587)
	mailServer.ehlo()
	mailServer.starttls()
	mailServer.ehlo()
	mailServer.login(gmail_user, gmail_pwd)
	mailServer.sendmail(gmail_user, to, msg.as_string())
	mailServer.close()
upcount=0
downcount=0
def chk(domain):
	try:
		if domain:
			global upcount
			upcount+=1
			req=urllib2.Request("http://www."+domain, headers={'User-Agent':"Magic Browser"})
			code=urllib2.urlopen(req).getcode()
			print domain+" - " + str(code)
	except IOError:
		global downcount
		downcount+=1
		print domain + " - "+ "	DOWN!"
		#send email to bwg
		mail("bwg@bostonwebgroup.com","Notice! Website: "+domain+" is down!","Automated email.")
	except KeyboardInterrupt:
		print "bye"
		exit()
	
f=open('domains.list','r')
domains=f.read().split('\n')
for domain in domains:
	chk(domain)
f.close()

print "Done. "+ str(upcount+downcount) +" domains checked. "+ str(upcount)+" up, "+str(downcount)+" down."
