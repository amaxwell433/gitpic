from gitpic import Gitpic

from art import *


Art=text2art("GLITCH PIC",font='block',chr_ignore=True)

try:
    input = input("FILE PATH FOR GLITCHING> ")

    g = Gitpic(img=input)

    g.generate_image()
    print("ALL DONE!")
except Exception as e:
    print(e)
