from req_stuff import *
from credential_handler import *
from flask import Flask, redirect, request
import matplotlib.pyplot as plt
import polyline

app = Flask(__name__)



redir_url = "http://www.strava.com/oauth/authorize?client_id={}&response_type=code&redirect_uri=http://localhost:5000/exchange_token&approval_prompt=force&scope=read,activity:read_all".format(get_client_id())

@app.route('/')
def auth():
	return redirect(redir_url)


@app.route('/exchange_token')
def get_token():
	
	code = request.args.get('code')
	response = authenticate(get_client_id(), get_client_secret(), code)
	activities = get_activities(response.json()['access_token']).json()
	data = []
	for a in activities:
		for p in polyline.decode(a['map']['summary_polyline']):
			data.append(p)
	plt.scatter(*zip(*data))
	plt.savefig("map.png")
	return "Image saved"

if __name__ == '__main__':
    app.run()
