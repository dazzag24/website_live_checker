# website_live_checker

Reads a list of URLs and check if they are acessible. If not it will send a notification via Pushover.

## Installation

### Create a Python 3 virtual environment

`python3 -m venv venv`

### Install the requirements

`pip install -r requirements.txt`

## Configuration

### URL list

This prgram looks for a file named `urls.list`. Format of file should look like:

```
http://foo:1935/,Get iPlayer
http://foo:3000/,Air Gradient
http://foo:9090/targets,Prometheus
http://boo:9000/,Portainer
http://zoo:8096/web/index.html#%21%2Fhome=,Emby
http://raspberrypi:8765/,RaspberryPi
```

### Secrets

Create a file named `.env` to store the [Pushover](https://pushover.net/) user and [application token](https://pushover.net/#apps).

```
PUSHOVER_APP_TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PUSHOVER_USER="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
