
print("Skriv inn teksten, avslutt med tom linje")
linje = input("> ")
resultat = ""
while linje != "":
    resultat += linje + "\n"
    linje = input("> ")
print(resultat)