import random
from turtle import clear
from game_data import data


def formatData(account):
    accountName = account["name"]
    accountDescr = account["description"]
    accountCountry = account["country"]
    return f"{accountName}, a {accountDescr} from {accountCountry}"


def checkAnswer(guess, aFollowers, bFollowers):
    if aFollowers > bFollowers:
        return guess == 'a'
    else:
        return guess == 'b'


score = 0
gameShouldContinue = True
accountB = random.choice(data)


while gameShouldContinue:

    accountA = accountB
    accountB = random.choice(data)
    if accountA == accountB:
        accountB = random.choice(data)

    print(f"Compare A: {formatData(accountA)}.")
    print(f"Compare B: {formatData(accountB)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    aFollowerCount = accountA["follower_count"]
    bFollowerCount = accountB["follower_count"]

    isCorrect = checkAnswer(guess, aFollowerCount, bFollowerCount)
    clear()

    if isCorrect:
        score += 1
        print(f"You're right! Score: {score}")
    else:
        gameShouldContinue = False
        print(f"You guessed wrong. Your score that round was {score}.")
