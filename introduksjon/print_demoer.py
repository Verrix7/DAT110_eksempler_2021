print("Test", end=" ")
print("En test til")
print("Tredje test")
print("Tester linjeskift. \nDette kommer på en ny linje. \n\tEtter tabulator")
print("Spesialtegn: \" \\ ")

tall = 5/3
test = "to"
streng = format(tall,"10.2f")
print(streng)
print(f"tallet er {tall:1.4f} og strengen er {test}")

# Formateringskoder
# 5.2f: Flyttall med 5 siffer (inkludert kommaet), hvorav 2 er bak kommaet
# 8d: Heltall på vanlig format hvor den setter av 8 siffer
