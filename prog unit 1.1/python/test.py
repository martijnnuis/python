from platform import java_ver


x = input("gebruiker zegt: ")

if x == ("ja"):
    print("uw antwoord is ja")
elif x == ("nee"):
    print("uw antwoord is geen ja")
else: 
    print("fout opgetreden antwoord met ja of nee")