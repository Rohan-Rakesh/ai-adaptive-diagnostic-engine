import math

def irt_probability(ability, difficulty):
    return 1 / (1 + math.exp(-(ability - difficulty)))


def update_ability(current_ability, difficulty, correct):

    expected = irt_probability(current_ability, difficulty)

    learning_rate = 0.2

    if correct:
        current_ability += learning_rate * (1 - expected)
    else:
        current_ability -= learning_rate * expected

    return max(0.1, min(1.0, current_ability))


def select_next_question(ability, questions):

    return min(
        questions,
        key=lambda q: abs(q["difficulty"] - ability)
    )
