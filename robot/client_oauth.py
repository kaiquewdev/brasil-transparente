import oauth2 as oauth
import simplejson as json

config_file = open('config.json')
config = json.loads( config_file.read() )
config_file.close()

# Create your consumer with the proper key/secret.
consumer = oauth.Consumer(key=config["consumer_key"], 
                          secret=config["consumer_secret"])

# Request token URL for Twitter.
request_token_url = "http://tumblr.com/oauth/request_token"

# Create our client.
client = oauth.Client(consumer)

# The OAuth Client request works just like httplib2 for the most part.
resp, content = client.request(request_token_url, "GET")
print resp
print content
