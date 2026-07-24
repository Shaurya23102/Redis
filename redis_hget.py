import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

r.hset("user:1", mapping={
    "name": "Alice",
    "age": 25,
    "city": "London"
})
data = r.hgetall("user:101") #will print whole dict 
name = r.hget("user:1", "name") #will print name value in dict
r.hdel("user:1", "name", "city") #will del varibales from a dict
print(data)
print(name)
