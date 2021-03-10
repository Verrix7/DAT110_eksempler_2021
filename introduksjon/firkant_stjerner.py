# Eksempel: Ønsker å skrive ut en firkant av stjerner, hvor brukerne
# angir høyde og bredde
#
# bredde 5 og høyde 3
# * * * * *
# * * * * *
# * * * * *

bredde = int(input("Bredde: "))
hoyde = int(input("Høyde: "))
for linje in range(hoyde):
    for tall in range(bredde):
        print("*", end="")
    print()