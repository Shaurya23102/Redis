import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

import time

r.set("token", "xyz", ex=5)

time.sleep(3)

print(r.get("token"))
print(r.ttl("token")) # this will give output of how many sec token will live will return -2 if expires
 
