menu=['ice-cream','chocolate','apple crisp','cookies']


while True:
    desert = input("desert: ")
    if desert in menu:
        print("Your desert will arive in 10 minutes")
        break
    else:
        print("Please choose another desert: ")
