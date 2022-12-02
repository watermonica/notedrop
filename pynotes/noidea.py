n, m = map(int, input().split())

setn = list(map(int, input().split()))
setm1 = set(list(map(int, input().split())))
setm2 = set(list(map(int, input().split())))

setm1.intersection_update(setn)
setm2.intersection_update(setn)

print(sum([(i in setm1) - (i in setm2) for i in setn]))
