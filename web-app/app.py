from credential_handler import *
from flask import Flask, redirect, request
app = Flask(__name__)



redir_url = "http://www.strava.com/oauth/authorize?client_id={}&response_type=code&redirect_uri=http://localhost:5000/exchange_token&approval_prompt=force&scope=read,activity:read_all".format(get_client_id())

@app.route('/')
def auth():
	return redirect(redir_url)


@app.route('/exchange_token')
def get_token():
	
	request.args.get('code')
	return "Got the auth code"


if __name__ == '__main__':
    app.run()
