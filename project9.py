#concession stand program

menu = {"piza":3,
        "burger":4,
        "fires": 1,
        "chips":5,
        "chicken": 12,
        "juice": 1}

cart = []
total = 0
for key, value in menu.items():
    print(f"{key}:{value}")
