"""

Given balls of 3 colors: Red, Green and Blue, assume that a person picks two balls.
Find the probability of picking two balls of same color.
"""
from math import comb

def calc_prob_same(r,g,b,t):
    return round((comb(r,2) + comb(g,2) + comb(b,2))/comb(t,2),4)*100

def next_prob(r,g,b,t):
    #6 possibilities in previous try.
    #If two reds in previous try:
    print("Probability of selecting two balls of same color if two red balls are selected in the first try",calc_prob_same(r-2,g,b,t-2))
    #If two greens in previous try:
    print("Probability of selecting two balls of same color if two green balls are selected in the first try",calc_prob_same(r,g-2,b,t-2))
    #If two blues in previous try:
    print("Probability of selecting two balls of same color if two blue balls are selected in the first try",calc_prob_same(r,g,b-2,t-2))
    #If one red and one green in previous try:
    print("Probability of selecting two balls of same color if one green ball and one red ball is selected in the first try",calc_prob_same(r-1,g-1,b,t-2))
    #If one blue and one green in previous try:
    print("Probability of selecting two balls of same color if one green ball and one blue ball is selected in the first try",calc_prob_same(r,g-1,b-1,t-2))
    #If one red and one blue in previous try:
    print("Probability of selecting two balls of same color if one red ball and one blue ball is selected in the first try",calc_prob_same(r-1,g,b-1,t-2))

red = int(input("Enter the count of red balls > "))
green = int(input("Enter the count of green balls > "))
blue = int(input("Enter the count of blue balls > "))
total = red+green+blue
#Pick two balls of same color : Could be green, blue, red.
print("Probability of drawing two balls of same color on first try is",calc_prob_same(red,green,blue,total))
next_prob(red,green,blue,total)
