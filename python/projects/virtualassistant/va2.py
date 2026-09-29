'''
#play a game--rock paper scissor
import random
player1 = input("enter any one of the below: rock,paper,scissor").lower()
player2 = random.choice(['rock','paper','scissor']).lower()
print(player2)
if player1 == "rock" and player2 == "paper":
    print("player2 won")
elif player1 == "paper" and player2 == "scissor":
    print("player2 won")
elif player1 == "scissor" and player2 == "rock":
    print("player2 won")
elif player 1 == player2:
    print("its a tie")
else:
    print("player1 won")
'''
# QR Code creation
import pyqrcode
import png
link = "https://www.linkedin.com/in/usha-yelleti-616900408/"
qr = pyqrcode.create(link)
#print(qr)
qr.png("myqr.png",scale = 10)
