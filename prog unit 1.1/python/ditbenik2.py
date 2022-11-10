from csv import list_dialects


print("Hallo, ik ben de quiz master Martijn")
print("de vragen gaan over mij, dus wees voorbereid!")
username = input("En wie speelt er vandaag:")
print("de speler van vandaag is: " + username +"!")   

print("dit is vraag 1")
print("Waar kom ik vandaan?")
print("de keuzes: A: lisse B: amsterdam C: leiden")


x = input("jou antwoord:")

if (x == "A" or x == "a"):
    print("dat is helemaal goed")
elif (x == "B" or x == "b"):
    print("ai dat is fout")
elif (x == "C" or x == "c"):
    print("ai dat is fout")

print("laten we doorgaan met de 2e vraag")
print("wat zijn martijn's hobby's?")
print("de keuzes: A: D&D, B: hardlopen, C:gamen")

m = input("jou antwoord:")

if m == ("C") or m == ("c"):
    print("dat is helemaal goed!")
elif m == ("A") or m == ("a"):
    print("ai dat is fout")
elif m == ("B") or m == ("b"):
    print("ai dat is fout")

print("dan zijn we alweer bij de 3e vraag aangekomen!")
print("wat is martijn's favoriete gerecht?")
print("de keuzes: A: witlof, B: lasagne, C: kip kerrie")

z = input("jou antwoord:")

if z == ("B") or z == ("b"):
    print("dat is helemaal goed!")
elif z == "A" or z == "a":
    print("ai dat is fout")
elif z == "C" or z == "c":
    print("ai dat is fout")

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

