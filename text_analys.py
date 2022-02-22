
from text import *

reg_uzivatel = \
    {
    "USER": "PASSWORD",
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
    }

oddelovac = "-" * 40

jmeno = input("Zadej uzivatelske jmeno: ")
heslo = input("Zadej heslo: ")

print(oddelovac)

if reg_uzivatel.get(jmeno) == heslo:
    print(f"Welcome to the app {jmeno}")
    print("We have 3 texts to be analyzed.")
else:
    print("unregistered user, terminating the program..")
    exit()

print(oddelovac)

acceptables = [1, 2, 3]
try:
    vyber = int(input("Enter a number btw. 1 and 3 to select: "))
except ValueError:
    print("It's not a number!")
    exit()
if vyber not in acceptables:
    print("Only 1,2,3")
    exit()

print(oddelovac)

r = [slovo.strip(",.()") for slovo in TEXTS[vyber-1].split()]
print (r)

pocet_slov = len(r)
print(f"There are {pocet_slov} word in the selected text.")

pocet_slov_prvni_velke = [i for i in r if i.istitle()]
prvni_velke = len(pocet_slov_prvni_velke)
print(f"There are {prvni_velke} titlecase words.")

pocet_slov_cele_velke = [i for i in r if i.isupper()]
cele_velke = len(pocet_slov_cele_velke)
print(f"There are {cele_velke} uppercase words.")

pocet_slov_cele_male = [i for i in r if i.islower()]
cele_male = len(pocet_slov_cele_male)
print(f"There are {cele_male} lowercase words.")

pocet_cisel = [i for i in r if i.isdigit()]
pc = len(pocet_cisel)
print(f"There are {pc} numeric strings.")

soucet_cisel = [int(i) for i in r if i.isdigit()]
soucet = sum(soucet_cisel)
print(f"The sum of all the numbers {soucet}")

print(oddelovac)

print (f"LEN |OCCURENCES | NR.")

print(oddelovac)

delka_slova = {}
for slovo in r:
    delka_slova[slovo] = len(slovo.strip())

vycuc = sorted(delka_slova.values())
counts = {}
for i in vycuc:
    counts[str(i)] = (counts.setdefault(str(i), 0) + 1)

hvezdicka = "*"
maximalni_delka = max(len(delka) for delka in delka_slova)

for delka, cetnost in counts.items():
    print(f"{delka:4}|{cetnost*hvezdicka:{maximalni_delka}}|{cetnost}")