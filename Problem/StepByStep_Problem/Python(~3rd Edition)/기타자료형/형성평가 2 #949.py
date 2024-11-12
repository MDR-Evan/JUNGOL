num = int(input())
play = []

while len(play) < num:
    play.append(tuple(input().split()))

print(play)