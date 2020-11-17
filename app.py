import redis

myHostname = "khigashi.redis.cache.windows.net"
myPassword = "PWkp1LRHB+qDZppgpHETiqlAzNsPQ7pK2UZQCvFeq94="

r = redis.StrictRedis(host=myHostname, port=6380,
                      password=myPassword, ssl=True)

result = r.ping()
print("Ping returned : " + str(result))

result = r.set("Message2", "Hello!, The cache is working with Python from webapp!")
