import os
from authlib.integrations.flask_client import OAuth


'''
Configuration for OAuth
'''
oauth = OAuth()
clientSecret = os.environ.get("client_secret") 
clientId = os.environ.get("client_id") 
google = oauth.register(
    name="google",
    client_id=clientId,
    client_secret= clientSecret,
    access_token_url="https://accounts.google.com/o/oauth2/token",
    access_token_params=None,
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    authorize_params=None,
    api_base_url="https://www.googleapis.com/oauth2/v1/",
    userinfo_endpoint=
    "https://openidconnect.googleapis.com/v1/userinfo",  # This is only needed if using openId to fetch user info
    client_kwargs={"scope": "openid email profile"},
)