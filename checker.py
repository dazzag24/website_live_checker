import http.client 
import urllib
import urllib.request
import os
import json
from dotenv import load_dotenv

load_dotenv()

PUSHOVER_APP_TOKEN = os.environ.get("PUSHOVER_APP_TOKEN")
PUSHOVER_USER = os.environ.get("PUSHOVER_USER")
URLS_LIST = os.environ.get("URLS_LIST")
#URLS_LIST = "[{\"url\": \"http://nuc:1935/\", \"title\": \"Get iPlayer\"}, {\"url\": \"http://nuc:3000/\", \"title\": \"Air Gradient\"}, {\"url\": \"http://nuc:9090/\", \"title\": \"Prometheus\"}, {\"url\": \"http://nuc:9000/\", \"title\": \"Portainer\"}, {\"url\": \"http://nuc:8096/\", \"title\": \"Emby\"}, {\"url\": \"http://zeropi:8765/\", \"title\": \"ZeroPi\"}]"

upcount = 0
downcount = 0

def notify_pushover(url: str, title: str):
	conn = http.client.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
	urllib.parse.urlencode({
		"token": PUSHOVER_APP_TOKEN,         	# Insert app token here
		"user": PUSHOVER_USER,          	 	# Insert user token here
		"html": "1",                            # 1 for HTML, 0 to disable
		"title": "Site Down!",              	# Title of the message
		"message": f"{title} is unreachable!",  # Content of the message - include HTML if required
		"url": url,                 			# Link to be included in message
		"url_title":title,                   	# Text for the link
		"sound": "none",                        # Define the sound played on the receiving device
	}), { "Content-type": "application/x-www-form-urlencoded" })
	conn.getresponse()

def check_site(url: str, title: str):
	try:
		if url:
			global upcount
			req = urllib.request.Request(url, headers={'User-Agent':"Magic Browser"})
			code = urllib.request.urlopen(req).getcode()
			print(f"Url: {url:<100} Returned: {code}")
			upcount += 1
	except IOError:
		global downcount
		downcount += 1
		print(f"Url: {url:<100} Unreachable")
		notify_pushover(url, title)
	except KeyboardInterrupt:
		print("Finished")
		exit()

url_list = json.loads(URLS_LIST)
for url in url_list:
	check_site(url['url'], url['title'])

print(f"{upcount+downcount} domains checked. UP: {upcount}\t DOWN: {downcount}")