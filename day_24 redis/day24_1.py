import redis

r = redis.Redis(host='localhost', port=6379, db=0)

#字符串类型string
r.set('name', 'abo')
value_set = r.get('name')
print(value_set.decode('utf-8'))
#哈希类型hash
r.hset('user', 'name', 'abo')
value_hs = r.hget('user', 'name')
print(value_hs.decode('utf-8'))

#列表类型list
r.lpush('list', '1', '2', '3')
value_lists = r.lrange('list', 0, -1)
print([value_list.decode('utf-8') for value_list in value_lists])

#集合类型set
r.sadd('set', '1', '2', '3')
value_sets = r.smembers('set')
print([value_set.decode('utf-8') for value_set in value_sets])

#有序集合类型sorted set
r.zadd('score', {'a': 1, 'b': 2, 'c': 3})
value_sorted_sets = r.zrange('score', 0, -1, withscores=True)
for member, score in value_sorted_sets:
    print(f"{member.decode('utf-8')}:{score}")








