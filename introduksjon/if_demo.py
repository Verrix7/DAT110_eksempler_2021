tall_streng = input("Skriv inn et tall: ")
tall = float(tall_streng)

if tall < 0.0:
    print("tallet er lavere enn 0")
elif tall == 0:
    print("tallet er eksakt lik 0")
else:
    print("tallet er større enn 0")
print("Avslutter")

#Ta inn en alder og sjekk om personen er tenåring: tallet er mellom 13 og 19

tall_streng = input("skriv inn en alder")
tall = float(tall_streng)
if tall >= 13 and tall <= 19:
    print("Personen er tenåring")
else:
    print("Personen er ikke tenåring")