import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

r.hset("user:1", mapping={
    "name": "Alice",
    "age": 25,
    "city": "London"
})

name = r.hget("user:1", "name")

print(name)
