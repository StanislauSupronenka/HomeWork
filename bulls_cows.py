#!/usr/lib/python3
#coding:utf-8


import random


def get_secret_numer():
    secret_set_of_numbers = random.sample(range(10), 4)
    return secret_set_of_numbers


def get_number_of_cows(secret_number, user_number):
    cows = 0
    for secret, user in zip(secret_number, user_number):
        if user in secret_number and user != secret:
            cows += 1
    return cows


def get_number_of_bulls(secret_number, user_number):
    bulls = 0
    for secret, user in zip(secret_number, user_number):
        if secret == user:
            bulls += 1
    return bulls


if __name__ == "__main__":
    secret_number = get_secret_numer()
    user_numbers=[]

    while secret_number != user_numbers:
        user_numbers = [
                int(i)
                for i in input("Enter four different numbers: ").split()
            ]
        if get_number_of_bulls(secret_number, user_numbers) == 4:
            print("You win")
        else:
            print("Bulls:",get_number_of_bulls(secret_number, user_numbers),
                  "Cows:", get_number_of_cows(secret_number, user_numbers))
