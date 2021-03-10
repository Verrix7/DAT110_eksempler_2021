# break avbryter en løkke midt i
resultat = ""
while True:
    linje = input("skriv inn en linje ")
    if linje == "":
        break
    resultat += linje + "\n"

print(resultat)