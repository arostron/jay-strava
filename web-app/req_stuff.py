import requests





def authenticate(client_id, client_secret, code):
	files = {
	    'client_id': (None, str(client_id)),
	    'client_secret': (None, str(client_secret)),
	    'code': (None, str(code)),
	    'grant_type': (None, 'authorization_code'),
	}
	return requests.post('https://www.strava.com/oauth/token', files=files)


def get_activities(bear):	
	headers = {
	    'accept': 'application/json',
	    'authorization': 'Bearer {}'.format(bear),
	}
	
	response = requests.get('https://www.strava.com/api/v3/athlete/activities?per_page=30', headers=headers)
	return response	
