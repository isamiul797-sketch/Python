n=int(input())
arr=list(map(int,input().split()))

unique_score=list(set(arr))
unique_score.sort(reverse=True)
print(unique_score[1])