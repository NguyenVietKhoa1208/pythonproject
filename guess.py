import random

top_of_range = input("Nhập 1 số: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Hãy nhập 1 số lớn hơn 0.')
        quit()
else:
    print('Làm ơn hãy nhập số lần sau .')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Mời bạn đoán : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Làm ơn hãy nhập số lần sau.')
        continue

    if user_guess == random_number:
        print("Bạn đoán đúng rồi!")
        break
    elif user_guess > random_number:
        print("Số bạn đoán cao hơn!")
    else:
        print("Số bạn đoán thấp hơn!")

print("Bạn đoán đúng rồi", guesses, "guesses")