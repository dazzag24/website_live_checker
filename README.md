# website_live_checker

Reads a list of URLs and check if they are acessible. If not it will send a notification via Pushover.

## Local ssage

### Create a Python 3 virtual environment[]

If using a local deployment:

`python3 -m venv venv`

### Install the requirements

`pip install -r requirements.txt`

Note that currently the program is cusomtised to running as a github action in which case the list of URLs is supplied as github secret.  
Running as a github action requires no additonal requirements.

Running locally will rwquire that you install dotenv (see requirements.txt) and that you configure the .env file


### Configuration

Create a file named `.env` to store the [Pushover](https://pushover.net/) user and [application token](https://pushover.net/#apps). 
You also need to set the URLs that check.

```
PUSHOVER_APP_TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PUSHOVER_USER="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
URLS_LIST="[{\"url\": \"http://first.com:1935/\", \"title\": \"First site\"}, {\"url\": \"http://second.com:3000/\", \"title\": \"Second site\"}]"
```


## Github action usage

Add secrets for the following items in the settings for your repo:

```
PUSHOVER_APP_TOKEN
PUSHOVER_USER
URLS_LIST
TAILSCALE_AUTHKEY
```

The tailscale authkey is an ephemeral key to be used by the [tailscsle github action](https://github.com/tailscale/github-action)

When using github actions you don't need to escape the quotes in the JSON.

```
[{"url": "http:/first.com:1935/", "title": "First site"}, {"url": "http://second.com:3000/", "title": "Second site"}]
```

