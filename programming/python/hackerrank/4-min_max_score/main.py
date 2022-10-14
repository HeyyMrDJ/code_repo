'''
Challenge problem. Using list of basketball scores
update min and max score
'''


def new_count_min_max(player_scores: list) -> list:
    'Test'
    score_list = [0, 0]
    count_list = [0, 0]
    for i, score in enumerate(player_scores):
        if i == 0:
            score_list[1] = score
            score_list[0] = score
        elif score < score_list[1]:
            score_list[1] = score
            count_list[1] += 1
        elif score > score_list[0]:
            score_list[0] = score
            count_list[0] += 1
    return count_list


scores2 = [12, 24, 10, 24]
scores = [0, 9, 3, 10, 2, 20]
print(new_count_min_max(scores))
print(new_count_min_max(scores2))
