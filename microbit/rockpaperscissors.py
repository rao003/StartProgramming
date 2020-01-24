# Add your Python code here. E.g.
from microbit import *
import random

scissor = Image("99009:"
                "99090:"
                "00900:"
                "99090:"
                "99009")
paper = Image("99999:"
              "90009:"
              "90009:"
              "90009:"
              "99999")
rock = Image("00000:"
              "09990:"
              "09990:"
              "09990:"
              "00000")
             
             
game = [rock, paper, scissor]

me_score = 0
bot_score = 0
game_continues = True
winner = 0
spiel_laenge = 3

while game_continues:
    #action logic
    if accelerometer.was_gesture('shake'):
        display.show(random.choice(game))
        sleep(3000)
        # win logic
        if button_a.is_pressed():
            # player won
            me_score += 1
        if button_b.is_pressed():
                # bot won
            bot_score += 1
                #ist das spiel vorbei?
            game_continues = me_score < spiel_laenge and bot_score < spiel_laenge
               
if not game_continues:
    if me_score == spiel_laenge:
        display.show(Image.UMBRELLA)
    else:
        display.show(Image.HEART)

               

