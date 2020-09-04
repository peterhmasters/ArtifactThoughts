from random import randint, sample
import pandas as pd


def generate_cards():
    cards = set()
    colors = ["B", "G", "R", "U"]
    values = range(10)
    for color in colors:
        for value in values:
            cards.add(color + str(value))
    return cards


def color_count(hand):
    count = dict()
    colors = ["B", "G", "R", "U"]
    for color in colors:
        count[color] = 0
    for card in hand:
        count[card[0]] += 1
    return count


def calculate_score(hand):
    score = 0
    for card in hand:
        score += int(card[1])
    return score


# B > G > R > U > B ...


def calculate_advantage(hand_a, hand_b):
    colors = ["B", "G", "R", "U"]
    count_a = color_count(hand_a)
    count_b = color_count(hand_b)
    advantage = 0
    for i in range(len(colors)):
        advantage += count_a[colors[i]] * count_b[colors[(i + 1) % 4]]
        advantage -= count_b[colors[i]] * count_a[colors[(i + 1) % 4]]
    return advantage


def calculate_winner(hand_a, hand_b):
    return (
        calculate_score(hand_a)
        - calculate_score(hand_b)
        + calculate_advantage(hand_a, hand_b)
        + randint(-5, 5)
    )


def choose_cards(choice_cards, my_hand, opponent_hand):
    best_card, best_score = None, None
    for card in choice_cards:
        current_hand = my_hand.copy()
        current_hand.add(card)
        score = calculate_winner(current_hand, opponent_hand)
        if best_card is None:
            best_card, best_score = card, score
        elif score > best_score:
            best_card, best_score = card, score
        else:
            continue
    return best_card


def generate_draft(cards):
    i = 0
    hand_a = []
    hand_b = []
    while i < 10:
        current_cards = sample(cards, 4)
        if i % 2 == 0:
            choice = choose_cards(current_cards, set(hand_a), set(hand_b))
            hand_a.append(choice)
            cards.remove(choice)
        else:
            choice = choose_cards(current_cards, set(hand_b), set(hand_a))
            hand_b.append(choice)
            cards.remove(choice)
        i += 1
    outcome = calculate_winner(set(hand_a), set(hand_b))
    if outcome >= 0:
        winner = ["a"]
    else:
        winner = ["b"]
    return hand_a + hand_b + winner


def generate_history(draft):
    output = []
    a_won = (draft[-1] == "a") * 1
    b_won = (draft[-1] == "b") * 1
    for i in range(10):
        if i % 2 == 0:
            output.append(
                draft[: i // 2 + 1]
                + list(" " * (5 - i // 2 - 1))
                + draft[5 : 5 + i // 2]
                + list(" " * (5 - i // 2))
                + [a_won]
            )
        else:
            output.append(
                draft[: (i + 1) // 2]
                + list(" " * (5 - (i + 1) // 2))
                + draft[5 : 5 + i // 2 + 1]
                + list(" " * (5 - i // 2 - 1))
                + [a_won]
            )
    return output


def generate_dummies(history):
    # check in hand 1, check in hand 2, add winner
    # ["B", "G", "R", "U"]
    output = []
    for board_state in history:
        dummies = [0] * 81
        for i in range(len(board_state)):
            value = board_state[i]
            if value == 0 or value == 1:
                dummies[80] = value
            elif value[0] == " ":
                pass
            elif value[0] == "B":
                dummies[int(value[1]) + (i // 5) * 40] = 1
            elif value[0] == "G":
                dummies[int(value[1]) + 10 + (i // 5) * 40] = 1
            elif value[0] == "R":
                dummies[int(value[1]) + 20 + (i // 5) * 40] = 1
            else:
                dummies[int(value[1]) + 30 + (i // 5) * 40] = 1
        output.append(dummies)
    return output


def generate_data(size):
    df = pd.DataFrame()
    for _ in range(size):
        cards = generate_cards()
        draft = generate_draft(cards)
        history = generate_history(draft)
        dummies = generate_dummies(history)
        df = df.append(dummies)
    return df
