# Skriv inn et antall tall, så skal den gjøre 1 + 2 + 3 + ... + antall
tall = 1
resultat = 0
antall_tall = int(input("skriv inn et antall tall"))
while tall <= antall_tall:
    resultat += tall
    tall += 1
    print("foreløpig resultat " + str(resultat))
print(f"resultatet ble: {resultat}")