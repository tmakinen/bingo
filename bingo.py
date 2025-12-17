import os
import random

def get_letter(num):
    if num <= 14:
        return "B"
    elif num <= 29:
        return "I"
    elif num <= 44:
        return "N"
    elif num <= 59:
        return "G"
    else:
        return "O"

numbers = range(1, 76)

randomized = []
while len(randomized) < 75:
    current = random.randrange(0, len(numbers))
    if current in randomized:
        continue

    os.system("clear")
    print("-----------------------------------------------")
    out = []
    for i in range(0, 15):
        if i in randomized:
            if numbers[i] < 10:
                out.append(" " + str(numbers[i]))
            else:
                out.append(str(numbers[i]))
        else:
            out.append("  ")
    print("B: " + " ".join(out))
    out = []
    for i in range(15, 30):
        if i in randomized:
            out.append(str(numbers[i]))
        else:
            out.append("  ")
    print("I: " + " ".join(out))
    out = []
    for i in range(30, 45):
        if i in randomized:
            out.append(str(numbers[i]))
        else:
            out.append("  ")
    print("N: " + " ".join(out))
    out = []
    for i in range(45, 60):
        if i in randomized:
            out.append(str(numbers[i]))
        else:
            out.append("  ")
    print("G: " + " ".join(out))
    out = []
    for i in range(60, 76):
        if i in randomized:
            out.append(str(numbers[i]))
        else:
            out.append("  ")
    print("O: " + " ".join(out))
    print("-----------------------------------------------")

    randomized.append(current)
    print()
    print(str(len(randomized)) + ": " + get_letter(current) + str(numbers[current]))
    input()
