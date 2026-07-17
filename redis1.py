import redis
r = redis.Redis(host="localhost", port=6379, decode_responses=True)
r.set("bike:1", "bmw")
r.set("bike:2", "duke")
r.set("bike:3", "luna")
print(r.mget("bike:1","bike:2","bike:3"))
#mget is used to get multiple value from a table at once n for single set get is used
