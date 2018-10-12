def player_score(threes, twos, fieldgoals):
    total_score = 0
    total_score += 3*threes + 2*twos + fieldgoals
    return total_score

print(player_score(6, 5, 5))

print(player_score(0, 2, 2))

print(player_score(2, 8, 7))