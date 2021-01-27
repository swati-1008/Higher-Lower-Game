from art import logo, vs
from game_data import data
from replit import clear
import random

# print(random.choice(data)['name'])

game_on = True
inp = {}
score = 0
flag = True
A = random.choice(data)
while game_on:
  clear()
  print(logo)
  B = random.choice(data)
  while B == A:
    B = random.choice(data)
  inp['A'] = A
  inp['B'] = B
  if flag and score > 0:
    print("You're right! Current score: " + str(score) + ".")
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
  print(vs)
  print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
  answer = input("Who has more followers? Type 'A' or 'B': ")
  # print(inp[answer]['name'])
  if answer == 'A':
    other = 'B'
  elif answer == 'B':
    other = 'A'
  if inp[answer]['follower_count'] > inp[other]['follower_count']:
    score += 1
    flag = True
    A = B
  else:
    flag = False
    game_on = False

if flag == False:
  clear()
  print(logo)
  print("Sorry, that's wrong. Final score = " + str(score) + ".")
