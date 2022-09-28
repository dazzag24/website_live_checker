# Website Checker

Supplied with a list of URLs, this script will check if they are acessible. If not it will send a notification via Pushover.

## Local usage

### Create a Python 3 virtual environment[]

If using a local deployment:

```
python3 -m venv venv
source venv/bin/activate
```

### Install the requirements

`pip install -r requirements.txt`

Note that currently the program is configured to run as a github action. In this mode the list of URLs is supplied as github secret.  
Running as a github action requires no additonal python module requirements.

Running locally requires that you install dotenv (see requirements.txt) and that you configure the .env file.

### Configuration

Create a file named `.env` to store the [Pushover](https://pushover.net/) user and [application token](https://pushover.net/#apps). 
You also need to set the URLs that check using the URLS_LIST env var.

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

To create a tailscale key vist the key section of the admin [page](https://login.tailscale.com/admin/settings/keys) and create a key with the following settings:
- Reusable: YES
- Ephemeral: YES
- Tags: NO

By default this key will need refreshing after 3 months.


Note that for the URL_LIST when using github actions you don't need to escape the quotes in the JSON.

```
[{"url": "http:/first.com:1935/", "title": "First site"}, {"url": "http://second.com:3000/", "title": "Second site"}]
```

