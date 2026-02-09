N = int(input())
words = [input() for i in range (N)]
for i in range (N):
    if i % 2 ==0:
        print(words[i])
    