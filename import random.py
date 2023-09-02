import random
import sys

def guess(m):
    while True:
        n = int(input("Enter a number: "))
        if n < m:
            if n<m/2:
                print('The number is much too small.')
            else:
                print("The number is too small")
        elif n > m:
            if n>(1.5)*m:
                print("The number is much too big")
            else:
                print("The number is too big")
        else:
            print("You guessed correctly!")
            cont = input("Play again? (y/n): ")
            if cont == "y":
                return True
            else:
                return False

def main():
    while True:
        m = random.randint(1, 50)
        print("Enter a number between 1 and 50")
        if not guess(m):
            print("Thanks for playing!")
            sys.exit()

if __name__ == "__main__":
    main()