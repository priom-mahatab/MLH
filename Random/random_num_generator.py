import random

def random_gen(upper_limit, lower_limit):
    return random.randint(lower_limit, upper_limit)

def main():
    upper_limit = int(input("Enter an upper limit: "))
    lower_limit = int(input("Enter a lower limit: "))
    print("Random number: ",random_gen(upper_limit, lower_limit))

if __name__ == "__main__":
    main()

