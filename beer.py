for beer_num in range(99, 0, -1):
    if beer_num != 1:
        word = "bottles"
        print(beer_num, word, "on the wall")
        print(beer_num, word, " of beer")
        print("Take one down")
        print("pass it around")
    if beer_num == 1:
        print("no more bottles of beer to pass")
    elif beer_num == 2:
        word = "bottle"
        print(beer_num - 1, word, "of beer left on the wall")
    print()
