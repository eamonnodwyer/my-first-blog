import twitter
import sqlite3

consumer_key =	"EQDdfD4nV2KDKEaiK1x4A"
consumer_secret = "I4v5kxg45HVJihgIippzMv5tP0bRyd02unb9mDLk2kw"
access_token_key	= "107844147-A8tecqekON60gEa6rsB6v0kl7TjKwz4JeAKWRJeN"
access_token_secret = "eTKpZHtZvAZYVJbHTqjfNc5EvvVFXy61pBXdtPZW0cV8j"

api = twitter.Api(consumer_key = consumer_key,
					consumer_secret = consumer_secret,
					access_token_key = access_token_key,
					access_token_secret  = access_token_secret)

print(api.VerifyCredentials())
print(type(api.VerifyCredentials()))

users = api.GetFriends()

print(users)
print(api.GetFollowers())

post_update = api.PostUpdates(status = "@epodwyer #python")

today = datetime.date.today()
me = datetime.date(2018,9,26)
ans = (me - today).days
post_update = api.PostUpdates(status = "@epodwyer " + str(ans))

