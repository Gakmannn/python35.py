from redis import Redis

r = Redis(host='localhost', port=6379, decode_responses=True)

r.hset('foo1', mapping={"arr":"bar","fdsds":1})
r.hset('foo2', mapping={"arr":"bar","fdsds":str([1,2])})
r.set('foo3', "arr", 10)
print(r.hgetall('foo1'))
print(r.hgetall('foo2'))
print(r.get('foo'))
print(r.get('foo3'))