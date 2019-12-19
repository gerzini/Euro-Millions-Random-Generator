import random 
from random import seed
import numpy as np
import time
#seed(6)
print(" ________                                      __       __  __  __  __                                     ")
print("/        |                                    /  \     /  |/  |/  |/  |                                    ")
print("$$$$$$$$/  __    __   ______    ______        $$  \   /$$ |$$/ $$ |$$ |____    ______    ______    _______ ")
print("$$ |__    /  |  /  | /      \  /      \       $$$  \ /$$$ |/  |$$ |$$      \  /      \  /      \  /       |")
print("$$    |   $$ |  $$ |/$$$$$$  |/$$$$$$  |      $$$$  /$$$$ |$$ |$$ |$$$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$$/ ")
print("$$$$$/    $$ |  $$ |$$ |  $$/ $$ |  $$ |      $$ $$ $$/$$ |$$ |$$ |$$ |  $$ |$$ |  $$ |$$    $$ |$$      \ ")
print("$$ |_____ $$ \__$$ |$$ |      $$ \__$$ |      $$ |$$$/ $$ |$$ |$$ |$$ |  $$ |$$ \__$$ |$$$$$$$$/  $$$$$$  |")
print("$$       |$$    $$/ $$ |      $$    $$/       $$ | $/  $$ |$$ |$$ |$$ |  $$ |$$    $$/ $$       |/     $$/ ")
print("$$$$$$$$/  $$$$$$/  $$/        $$$$$$/        $$/      $$/ $$/ $$/ $$/   $$/  $$$$$$/   $$$$$$$/ $$$$$$$/")
print("")

ONE=[
"   __   ",
" _/  |  ",
"/ $$ |  ",
"$$$$ |  ",
"  $$ |  ",
"  $$ |  ",
" _$$ |_ ",
"/ $$   |",
"$$$$$$/ "]

TWO=[
"  ______  ",
" /      \ ",
"/$$$$$$  |",
"$$____$$ |",
" /    $$/ ",
"/$$$$$$/  ",
"$$ |_____ ",
"$$       |",
"$$$$$$$$/ "]
          
          
          
THREE=[
"  ______  ",
" /      \ ",
"/$$$$$$  |",
"$$ ___$$ |",
"  /   $$< ",
" _$$$$$  |",
"/  \__$$ |",
"$$    $$/ ",
" $$$$$$/  "]
          
          
          
FOUR=[
" __    __ ",
"/  |  /  |",
"$$ |  $$ |",
"$$ |__$$ |",
"$$    $$ |",
"$$$$$$$$ |",
"      $$ |",
"      $$ |",
"      $$/ "]
          
          
          
FIVE=[
" _______  ",
"/       | ",
"$$$$$$$/  ",
"$$ |____  ",
"$$      \ ",
"$$$$$$$  |",
"/  \__$$ |",
"$$    $$/ ",
" $$$$$$/  "]
          
          
          
SIX=[
"  ______  ",
" /      \ ",
"/$$$$$$  |",
"$$ \__$$/ ",
"$$      \ ",
"$$$$$$$  |",
"$$ \__$$ |",
"$$    $$/ ",
" $$$$$$/  "]
          
          
          
SEVEN=[
" ________ ",
"/        |",
"$$$$$$$$/ ",
"    /$$/  ",
"   /$$/   ",
"  /$$/    ",
" /$$/     ",
"/$$/      ",
"$$/       "]
          
          
          
EIGHT=[
"  ______  ",
" /      \ ",
"/$$$$$$  |",
"$$ \__$$ |",
"$$    $$< ",
" $$$$$$  |",
"$$ \__$$ |",
"$$    $$/ ",
" $$$$$$/  "]
          
          
          
NINE=[
"  ______  ",
" /      \ ",
"/$$$$$$  |",
"$$ \__$$ |",
"$$    $$ |",
" $$$$$$$ |",
"/  \__$$ |",
"$$    $$/ ",
" $$$$$$/  "]
          
          
          
ZERO=[
"  ______  ",
" /      \ ",
"/$$$$$$  |",
"$$$  \$$ |",
"$$$$  $$ |",
"$$ $$ $$ |",
"$$ \$$$$ |",
"$$   $$$/ ",
" $$$$$$/  "]




array_TEXT = [
    ["0",ZERO],
    ["1",ONE],
    ["2",TWO],
    ["3",THREE],
    ["4",FOUR],
    ["5",FIVE],
    ["6",SIX],
    ["7",SEVEN],
    ["8",EIGHT],
    ["9",NINE]]


def printNumbers(number):
    
    if(number[0]):
        m = 0
        while(array_TEXT[m][0]!=number[0]):
            m +=1
        TEXT_NUMBER1 = array_TEXT[m][1]          
        
    if(len(number)==2):
        m = 0
        while(array_TEXT[m][0]!=number[1]):
            m +=1
        TEXT_NUMBER2 = array_TEXT[m][1]          


    for i in range(9):#number of lines of big numbers
        if(len(number)==2):
            print("                                         " + TEXT_NUMBER1[i]+TEXT_NUMBER2[i])
        else:
            print("                                         " + TEXT_NUMBER1[i])


def run_lotery():
    random_numbers = random.sample(range(1,50), 5) 
    random_stars = random.sample(range(1,12), 2) 

    random_numbers.sort()
    random_stars.sort()


    print("")
    print("")
    print("                     #############################################################")
    print("                     ######################### NUMBERS ###########################")
    print("                     #############################################################")

    for i in range(len(random_numbers)):
        time.sleep(1)
        printNumbers(str(random_numbers[i]))
        
    print("")
    print("")
    print("                     #############################################################")
    print("                     ########################## STARS ############################")
    print("                     #############################################################")


    for i in range(len(random_stars)):
        time.sleep(1)
        printNumbers(str(random_stars[i]))
        
    print("")
    print("")
    print("                     Numbers:",random_numbers)
    print("                     Stars:",random_stars)
    decision = input("                     Run game again? Type Y for Yes or any other combination to exit.")
    if(decision == "y" or decision =="Y"):
        run_lotery()
    
run_lotery()
