from collections import deque
def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    t = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            t += 1
        else:
            t += 5
        cache.append(city)
    return t