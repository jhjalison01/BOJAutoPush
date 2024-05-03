import sys
input=sys.stdin.readline

T=int(input())

dp=[[0]*15 for _ in range(15)]
for i in range(1,15):
  dp[0][i]=i

for i in range(1,15):
  for j in range(1,15):
    #i층 (j-1)호에 사는 사람 수에 (i-1)층 j호에 사는 사람 더하기
    dp[i][j]=dp[i][j-1]+dp[i-1][j]

for _ in range(T):
  k=int(input())
  n=int(input())
  print(dp[k][n])