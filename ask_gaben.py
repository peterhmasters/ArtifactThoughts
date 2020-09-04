from dummy_data import generate_dummies
import pandas as pd

def ask_gaben(clf, choice_cards, hand_a, hand_b):
    best_card, best_probability = None, None
    if len(hand_a) == len(hand_b):
        my_hand = hand_a.copy()
        for card in choice_cards:
            current_hand = my_hand.copy()
            current_hand.add(card)
            board_state = (
                list(current_hand)
                + list(" " * (5 - len(current_hand)))
                + list(hand_b)
                + list(" " * (5 - len(hand_b)))
            )
            dummies = pd.DataFrame(generate_dummies([board_state])).iloc[:,:-1]
            probability = clf.predict(dummies)
            if best_card is None:
                best_card, best_probability = card, probability
            elif probability > best_probability:
                best_card, best_probability = card, probability
            else:
                continue
    else:
        my_hand = hand_b.copy()
        for card in choice_cards:
            current_hand = my_hand.copy()
            current_hand.add(card)
            board_state = (
                list(hand_a)
                + list(" " * (5 - len(hand_a)))
                + list(current_hand)
                + list(" " * (5 - len(current_hand)))
            )
            dummies = pd.DataFrame(generate_dummies([board_state])).iloc[:,:-1]
            probability = 1 - clf.predict(dummies)
            if best_card is None:
                best_card, best_probability = card, probability
            elif probability > best_probability:
                best_card, best_probability = card, probability
            else:
                continue
    return best_card
