def solution(cacheSize, cities):
    cache=[]
    answer = 0
    for i in cities:
        i = i.lower()
        if i in cache:
            answer +=1
            cache.remove(i)
            cache.append(i)
        if i not in cache:
            answer +=5
            if len(cache)<cacheSize:
                cache.append(i)
            elif cacheSize==0:
                pass
            else:
                del cache[0]
                cache.append(i)
    return answer