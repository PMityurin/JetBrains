dict_svizei = {}
visited = [-1]
ans = []
ans2 = []
otvet = 0
otvet2 = []
flag = False
n = int(input())
matrix = []
for i in range(1, n + 1):
    dict_svizei[i] = []
    visited.append(-1)
    li = [int(temp) for temp in input().split()]
    for j in range(len(li)):
        if li[j] == 1:
            dict_svizei[i].append(j + 1)
start, finish = [int(temp) for temp in input().split()]
ans.append([start])
visited[start] = otvet
for k in range(n):
    otvet += 1
    temp = []
    for i in ans[k]:
        for j in dict_svizei[i]:
            if visited[j] == -1:
                temp.append(j)
                visited[j] = otvet
    ans.append(temp)
ans2.append([finish])
otvet2.append(finish)
if visited[finish] > 0:
    for k in range(visited[finish]):
        temp = []
        for i in ans2[k]:
            for j in dict_svizei[i]:
                if visited[j] == visited[finish] - (k + 1):
                    otvet2.append(j)
                    temp.append(j)
                    ans2.append(temp)
                    break
            if otvet2[-1] == start:
                break
        if otvet2[-1] == start:
            break
    print(visited[finish])
    otvet2.reverse()
    print(*otvet2)
else:
    print(visited[finish])
