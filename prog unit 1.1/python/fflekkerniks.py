import time
from turtle import delay
import sys

naam = input("wat is je naam: ")
print("hallo " + naam)

print("welk verhaal wil je kiezen")
print("verhaal A, verhaal B, verhaal C")

verhaal = input("verhaal:")

if verhaal == "A" or verhaal == "a":
    print("oke goede keuze! luister dan goed naar dit verhaal")
    time.sleep(2)
    blah = "iets leuks joh"
    for I in blah:
        sys.stdout.write(I)
        sys.stdout.flush()
        time.sleep(0.2)
elif verhaal == "B" or "b":
    print("oke goede keuze! luister dan goed naar dit verhaal")
elif verhaal == "C" or "c":
    print("oke goede keuze! luister dan goed naar dit verhaal")