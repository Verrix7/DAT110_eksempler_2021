def fakultet(heltall):
    resultat = 1
    while heltall <= 0:
        print("Tallet kan ikke være minde eller lik 0")
        heltall = int(input("Hvilket tall vil du ha fakultetet til? "))
    else:
        for tall in range(1,heltall+1):
            resultat *= tall
        return resultat

# Sjekker om dette er hovedscriptet eller blir importert, kjører kun hvis
# Dette er ovedscriptet
if __name__ == "__main__":
    fakultet_av = int(input("Hvilket tall vil du ha fakultetet av? "))
    resultat = fakultet(fakultet_av)
    print({resultat})