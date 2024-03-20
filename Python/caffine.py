import random
from time import sleep
from playsound import playsound

filePaths = [
    "Python/SFX/-999SocialCreditSiren.mp3",
    "Python/SFX/BassBoostedNFL.mp3",
    "Python/SFX/DespicableMeWhistleBassBoosted.mp3",
    "Python/SFX/DiscordPing.mp3",
    "Python/SFX/FBIOPENUP.mp3",
    "Python/SFX/TacoBellBong.mp3"
]


def selectSound():
    currentSound = random.choice(filePaths)
    return currentSound

def safePlaysound(playWhat):
    try:
        playsound(playWhat)
        print("Success! \n")
    except:
        print("Oops, it didn't work, hopefully this wont crash lolol")


print("Beginning loop... \n")

while True:
    currentSound = selectSound()
    print("Next sound: " + currentSound + "\n")

    #timer = 5
    timer = random.randint(30, 600)

    for i in range(timer):
        print("remaining time:", timer - i)
        sleep(1)  # Sleep for 1 second

    print("\nPlaying sound... \n")
    safePlaysound(currentSound)
