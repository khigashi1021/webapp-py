import redis

myHostname = "khigashi.redis.cache.windows.net"
myPassword = "PWkp1LRHB+qDZppgpHETiqlAzNsPQ7pK2UZQCvFeq94="

r = redis.StrictRedis(host=myHostname, port=6380,
                      password=myPassword, ssl=True)

result = r.ping()
print("Ping returned : " + str(result))

result = r.set("Message2", "Hello!, The cache is working with Python!")
print("SET Message returned : " + str(result))

result = r.get("Message2")
print("GET Message returned : " + result.decode("utf-8"))

result = r.client_list()
print("CLIENT LIST returned : ")
for c in result:
    print("id : " + c['id'] + ", addr : " + c['addr'])
