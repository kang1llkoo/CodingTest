def solution(answers):
    answer_types = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    scores = [0,0,0]
    for type_idx, ans_type in enumerate(answer_types):
        for idx, ans in enumerate(answers):
            if ans == ans_type[idx % len(ans_type)]:
                scores[type_idx] += 1
    return [idx+1 for idx, score in enumerate(scores) if score == max(scores)]