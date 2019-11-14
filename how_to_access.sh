#!/bin/bash

open -a Google\ Chrome\
	"http://www.strava.com/oauth/authorize?client_id=40782&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read,activity:read"

# need client creds from strava 
# need code from oauth/authorize
curl -X POST https://www.strava.com/oauth/token \
	-F client_id={} \
	-F client_secret={} \
	-F code={}\
	-F grant_type=authorization_code 

# need Beare for this line here
curl -X GET "https://www.strava.com/api/v3/athlete/activities?per_page=30" -H "accept: application/json" -H "authorization: Bearer {}"
