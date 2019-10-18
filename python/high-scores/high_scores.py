def latest(scores):
    return scores[len(scores)-1]


def personal_best(scores):
    highest = -1
    for score in scores:
        if score >= highest:
            highest = score
    return highest


def personal_top_three(scores):
    highest = []
    for i in range(0,3):
        temp = personal_best(scores)
        if temp != -1:
            highest.append(temp)
            scores.remove(temp)
    return highest

