from req_stuff import *
from credential_handler import *
from flask import Flask, redirect, request, render_template
import matplotlib.pyplot as plt
import polyline
import io
import base64


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
		route = []
		for p in polyline.decode(a['map']['summary_polyline']):
			route.append({'lat':p[0], 'lng':p[1]})
		data.append(route)
	return render_template('asdf.html', data=data, g_key=get_g_api())

if __name__ == '__main__':
    app.run()
