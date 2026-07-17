#Yes, every redis.Redis() client uses a connection pool by default. However, if I create multiple Redis client instances, each one gets its own separate pool. 
#By creating a ConnectionPool explicitly and passing it to multiple clients, they all share the same pool of connections. 
#This reduces the total number of TCP connections, gives better control over settings like max_connections, and is useful in larger applications where multiple modules access the same Redis server.
redis_client = redis.Redis(host="localhost", port=6379)

def login(user):
    redis_client.set(f"user:{user}", "logged_in")
  
redis_client = redis.Redis(host="localhost", port=6379)

def save_chat(user, message):
    redis_client.rpush(f"chat:{user}", message)

redis_client = redis.Redis(host="localhost", port=6379)

def cache_response(question, answer):
    redis_client.set(question, answer)
#here each function will have its own pooling so if there are 10 concurrent users then total connection = 10+10+10 = 30 
#now with pooling 
#all 3 diff function share same connections that is 10 
pool = redis.ConnectionPool(
    host="localhost",
    port=6379,
    max_connections=10,
    decode_responses=True
)
redis_client = redis.Redis(connection_pool=pool)

def login(user):
    redis_client.set(f"user:{user}", "logged_in")
  
redis_client = redis.Redis(connection_pool=pool)

def save_chat(user, message):
    redis_client.rpush(f"chat:{user}", message)

redis_client = redis.Redis(connection_pool=pool)

def cache_response(question, answer):
    redis_client.set(question, answer)
