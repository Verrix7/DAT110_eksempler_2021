#Oppgave: Ønsker å regne ut arealet til et rom hvor brukeren oppgir lengde og bredde

#Pseudokode
# Be brukeren om lengde
# Be brukeren om bredde
# Regne ut arealet
# Skrive ut arealet

lengde_streng = input("Lengden til rommet i meter: ")
lengde_flyttall = float(lengde_streng)
bredde_streng = input("bredden til rommet i meter: ")
bredde_flyttall = float(bredde_streng)
areal = lengde_flyttall * bredde_flyttall
print("Arealet av rommet er: " + str(round(areal)))