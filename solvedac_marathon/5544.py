import sys
input = sys.stdin.readline

n = int(input())
score = [0 for i in range(n + 1)]
for i in range((n*(n-1)) // 2):
    a, b, c, d = list(map(int, input().split()))
    if c > d:
        score[a] += 3
    elif c == d:
        score[a] += 1
        score[b] += 1
    else:
        score[b] += 3

teams = []
for team in range(1, n + 1):
    teams.append([team, score[team]])

teams.sort(key=lambda x:-x[1])
rank_of = [0] * (n + 1)

prev_score = None      
current_rank = 0   
    
for i in range(len(teams)):
    team_num = teams[i][0]     
    team_score = teams[i][1]   

    if prev_score is None or team_score != prev_score:
        current_rank = i + 1   
        prev_score = team_score
    rank_of[team_num] = current_rank

for team in range(1, n + 1):
    print(rank_of[team])



