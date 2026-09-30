import random

number = random.randint(1, 100)

print("🎯 Number Guessing Game")
print("Maine 1 se 100 ke beech ek number socha hai.")
print("Use guess karo!")

while True:
    guess = int(input("Apna guess enter karo: "))

    if guess < number:
        print("📈 Thoda bada number try karo.")

    elif guess > number:
        print("📉 Thoda chhota number try karo.")

    else:
        print("🎉 Congratulations!")
        print("Tumne sahi number guess kar liya!")
        break