from steem import Steem
import pprint

limit = 1000
account=""

s = Steem(nodes=["https://api.steemit.com"])
start_id = ""
mutes = r = s.get_followers(account, start_id, "ignore", limit)
while len(r) == limit:
    start_id = mutes[-1]['follower']
    r = s.get_followers(account, start_id, "ignore", limit)
    mutes = mutes + r[1:]

pprint.pprint([m['follower'] for m in mutes])
