linje = input("skriv inn første linje tekst")
resultat = ""
while linje != "":
    resultat += linje + "\n"
    linje = input("skriv inn neste linje tekst")
print(resultat)