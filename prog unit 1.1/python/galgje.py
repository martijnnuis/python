import time, random
hiddenword = ""
print("gegroet reiziger u mag niet verder tot dat u uw naam bekend heeft gemaakt")
username = input("vertel mij uw naam: ")
print("hallo " + username + " bekend met het spel galgje?")

while True:
    print("zo ja type dan ja, zo nee type dan nee")
    x = input("uw antwoord? ")
    if x == "ja":
        print("helemaal goed dan stuur ik je nu door naar het spel")
        time.sleep(1)
        break
    elif x == "nee":
        print("de uitleg: de game master verzint een woord, daar op begin jij letters te raden")
        print("je hebt 7 levens iedere keer dat je een foute letter invoert dan verlies je een leven")
        print("als al je levens op zijn heb je verloren en kan je kiezen om opnieuw te beginnen")
        print("zijn de regels duidelijk?")

def randomword():
    lijst = ["dit", "is", "galgje"]
    word = random.choice(lijst)
    hiddenword = list(word)
    for i in range(len(hiddenword)):
        juiste.append("_")
    return hiddenword

while True:
    geraden = []
    juiste = []
    z = input("welke letter wil je raden?")
    geraden.append(z)
    if z in hiddenword:
        print("goed!")
        juiste.append(z)
        print(juiste)









