import json

def creds():
	creds = dict()
	with open("creds.json") as f:
		creds = json.load(f)
	return creds

def get_client_secret():
	return creds()['client_secret']

def get_client_id():
	return creds()['client_id']

if __name__ == "__main__":
	print(get_client_id())
