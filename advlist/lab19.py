#!/usr/bin/env python3

def main():

    wordbank= ["indentation", "spaces"]

    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    print(wordbank)
    wordbank.append(4)
    print(wordbank)

    num = int(input("Please enter a number between 0 and 18: "))

    pick = tlgstudents[num]

    print(f"{pick} always uses 4 spaces to indent.")

main()
