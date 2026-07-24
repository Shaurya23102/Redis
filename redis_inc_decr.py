import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

r.set("visits", 10)

new_value = r.incrby("visits",10)
r.decrby("visits", 5)

print(r.get("visits"))
