# Fakultet

# Ber brukeren om input og konverterer dette til et heltall
parameter = int(input("Hvilket tall vil du ha fakultet til?"))
while parameter < 0:
    print("fakultet av negativt tall finnes ikke")
    parameter = int(input("Hvilket tall vil du ha fakultet til?"))
# range går gjennom alle tall fra 0 til men ikke parameteren
resultat = 1
for tall in range(1, parameter+1):
    resultat *= tall
    print(f"Tall: {tall} foreløpig resultat {resultat}")
print(resultat)