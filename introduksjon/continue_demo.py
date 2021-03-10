# Skriv ut all tall 1-30 bortsett fra  de som er delelige på 13

for tall in range(1,31):
    if tall % 13 == 0:
        continue
    else:
        print(tall)