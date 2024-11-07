# Programmers: Lucas Podowski, Antonio Dueno
# Course: CS151, Zelalem Yalew
# Due Date: 11/6
# Programming Assignment: Lab 08
# Problem Statement: In this lab we were instructed to create a program that calculated the number of times a number was
#                    rolled after rolling a pair of dice, after rolling the dice a number of times indicated by the user.
# Data In: Number of times user wants dice to be rolled.
# Data Out: List of number of times a number was rolled.
# Credits: Class notes

import random

# Purpose: prompting user to input the number of times they want to roll dice
# name: roll_input
# parameter: none
# return: num_rolls
def roll_input():
    num_rolls = input("Enter the number of times you want to roll the pair of dice: ")
    while not num_rolls.isdigit():
        print('Input must be an integer')
        num_rolls = input("Enter the number of times you want to roll the pair of dice: ")
    return int(num_rolls)

# Purpose: roll the die the number of times they want and store in list
# name: roller
# parameter: num_rolls
# return: list_of_values
def roller(num_rolls):
    count = 0
    list_of_values = []
    while count < num_rolls:
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        roll_sum = roll1 + roll2
        list_of_values.append(roll_sum)
        count += 1
    return list_of_values

# Purpose:  count the number of times a value is rolled
# name: times_rolled
# parameter: list of values
# return:  count_list
def times_rolled(list_of_values):
    sums_list = []
    count = 2
    while count <= 12 :
        sum_count = list_of_values.count(count)
        sums_list.append(sum_count)
        count += 1
    return sums_list

# Purpose:  output the sum of list with *
# name: sum_chart
# parameter: sums_list
# return:  none
def sum_chart(sums_list):
    count = 2
    sum_count = 0
    while count <= 12:
        print(f"Sum of {count:02}", '*' * sums_list[sum_count])
        count += 1
        sum_count += 1

# Main function
def main():
    num_rolls = roll_input()
    list_of_values = roller(num_rolls)
    sums_list = times_rolled(list_of_values)

    print(f"\nRolling {num_rolls} pairs of dice.")
    print(sums_list)
    sum_chart(sums_list)

main()