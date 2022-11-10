from turtle import delay
from csv import list_dialects

#vraag4
def vraag4():
    print("oke, oke dan is het tijd voor de laatste vraag")
    print("wat is martijn's zijn favoriete band?")
    print("de keuzes: A: sabaton, B: powerwolf, C: alestorm")

    n = input("jou antwoord:")

    if n == ("A") or n == ("a"):
        print("dat is helemaal goed!")
    elif n == ("B") or n == ("b"):
        print("ai dat is fout")
    elif n == ("C") or n == ("c"):
        print("ai dat is fout")

#vraag3
def vraag3():
    print("dat is het antwoord dat ik zocht")
    print("laten we doorgaan met de 3e vraag")
    print("wat is martijn's favoriete gerecht?")
    print("de keuzes: A: witlof, B: lasagne, C: kip kerrie")

    z = input("jou antwoord:")

    if z == "A" or z == "a":
        vraag4()
    elif z == "B" or z == "B":
        vraag4()
    elif z == "C" or z == "c":
        vraag4()

def vraag33():
    print("dat is niet wat ik zocht, ik ga binnenkort wel een D&D capaign op school spelen om het te proberen")
    print("laten we doorgaan met de 3e vraag")
    print("wat is martijn's favoriete gerecht?")
    print("de keuzes: A: witlof, B: lasagne, C: kip kerrie")

    z = input("jou antwoord:")

    if z == "A" or z == "a":
        vraag4()
    elif z == "B" or z == "B":
        vraag4()
    elif z == "C" or z == "c":
        vraag4()

def vraag32():
    print("denk je nou echt dat ik zo sportief ben?")
    print("laten we doorgaan met de 3e vraag")
    print("wat is martijn's favoriete gerecht?")
    print("de keuzes: A: witlof, B: lasagne, C: kip kerrie")

    z = input("jou antwoord:")

    if z == "A" or z == "a":
        vraag4()
    elif z == "B" or z == "B":
        vraag4()
    elif z == "C" or z == "c":
        vraag4()

def vraag213():

    print("dat is helemaal goed")
    print("laten we doorgaan met de 3e vraag")
    print("wat is martijn's favoriete gerecht?")
    print("de keuzes: A: witlof, B: lasagne, C: kip kerrie")

    z = input("jou antwoord:")

    if z == "A" or z == "a":
        vraag4()
    elif z == "B" or z == "B":
        vraag4()
    elif z == "C" or z == "c":
        vraag4()

def vraag214():
    print("je hebt het niet mis dit was mijn eerste keuze voor een school maar het is het niet geworden")
    print("laten we doorgaan met de 3e vraag")
    print("wat is martijn's favoriete gerecht?")
    print("de keuzes: A: witlof, B: lasagne, C: kip kerrie")

    z = input("jou antwoord:")

    if z == "A" or z == "a":
        vraag4()
    elif z == "B" or z == "B":
        vraag4()
    elif z == "C" or z == "c":
        vraag4()

def vraag215():
    print("hey flappie zo slim ben ik niet")
    print("laten we doorgaan met de 3e vraag")
    print("wat is martijn's favoriete gerecht?")
    print("de keuzes: A: witlof, B: lasagne, C: kip kerrie")

    z = input("jou antwoord:")

    if z == "A" or z == "a":
        vraag4()
    elif z == "B" or z == "B":
        vraag4()
    elif z == "C" or z == "c":
        vraag4()

def vraag223():
    print("ik heb op het vso leystede de opleiding vmbo-tl gevolgd als je dit had goed gedaan")
    print("laten we doorgaan met de 3e vraag")
    print("wat is martijn's favoriete gerecht?")
    print("de keuzes: A: witlof, B: lasagne, C: kip kerrie")

    z = input("jou antwoord:")

    if z == "A" or z == "a":
        vraag4()
    elif z == "B" or z == "B":
        vraag4()
    elif z == "C" or z == "c":
        vraag4()
     

#vraag2
def vraag2():
    print("dat is het antwoord dat ik zocht")
    print("laten we doorgaan met de 2e vraag")
    print("wat zijn martijn's hobby's?")
    print("de keuzes: A: D&D, B: hardlopen, C:gamen")

    m = input("jouw antwoord:")

    if m == "A" or m == "a":
        vraag33()
    elif m == "B" or m == "b":
        vraag32()
    elif m == "C" or m == "c":
        vraag3()

def vraag21():
    print("juist ja, dat is niet helemaal het antwoord dat ik zocht")
    print("laten we doorgaan naar de 2e vraag")
    print("op welke school zit martijn")
    print("de antwoorden: A: mediacollege amsterdam, B: roc van amsterdam, C:  universiteit van amsterdam")
    q = input("jouw antwoord:")

    if q == "A" or q == "a":
        vraag213()
    elif q == "B" or q == "b":
        vraag214()
    elif q == "C" or q == "c":
        vraag215()

def vraag22():
    print("juist ja, dat is niet helemaal het antwoord dat ik zocht")
    print("laten we doorgaan met de 2e vraag")
    print("martijn heeft in leiden op de middelbare school. welk niveau heeft martijn gevolgd?")
    print(" de antwoorden: A: vmbo-b, B: vmbo-k, C: vmbo-tl")
    w = input("jouw antwoord:")

    if w == "A" or w == "a":
        vraag223()
    elif w == "B" or w == "b":
        vraag223()
    elif w == "C" or w == "c":
        vraag223()



#vraag1
def vraag1(): 

    print("dit is vraag 1")
    print("Waar kom ik vandaan?")
    print("de keuzes: A: lisse B: amsterdam C: leiden")
    x = input("jouw antwoord:")
    
    if x == "A" or x == "a":
        vraag2()
    elif x == "B" or x == "b":
        vraag21()
    elif x == "C" or x == "c":
        vraag22()

print("Hallo, ik ben de quiz master Martijn")
print("de vragen gaan over mij, dus wees voorbereid!")
username = input("En wie speelt er vandaag:")
print("de speler van vandaag is: " + username +"!")   

vraag1()








