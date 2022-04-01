#!/usr/bin/env python3
import os
import csv


def is_valid(card_number: str) -> bool:

    total_digits = len(card_number)
    if total_digits not in range(13, 17):
        return False

    # https://en.wikipedia.org/wiki/Luhn_algorithm implementation

    total = 0

    digits = [int(d) for d in card_number]

    for i, digit in enumerate(reversed(digits)):
        if i % 2:
            digit *= 2
        if digit > 9:
            # Same thing as doing 10 -> 1 + 0 = 1, example: 13 - 9 = 4 = 1 + 3
            digit -= 9

        total += digit

    return total % 10 == 0


def classify_card(raw_card_number: str) -> None:
    if not is_valid(raw_card_number):
        print('INVALID')
        return

    brands = {
        34: 'AMEX',
        37: 'AMEX',
    }
    brands.update({identifier: 'MASTERCARD' for identifier in range(51, 56)})
    brands.update({identifier: 'VISA' for identifier in range(40, 50)})

    card_brand = brands.get(int(raw_card_number[:2]))

    if card_brand is None:
        print('INVALID')
        return

    print(card_brand)


def run_tests() -> None:
    with open('test_cards.csv', encoding="utf-8-sig") as test_cards_file:
        rows = csv.reader(test_cards_file)

        for row in rows:
            card_number = row[0]
            print(card_number, end=' is ')
            classify_card(card_number)


while True:
    if bool(os.environ.get('TEST', False)):
        run_tests()
        break

    raw_card_number = input('Number: ')

    if not raw_card_number.isdigit():
        continue
    else:
        classify_card(raw_card_number)
        break
