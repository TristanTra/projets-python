
def place_cine():
    age = int(input("quel est ton age ?"))
    if age < 18:
        prix = 7
    else:
        prix = 12
    pop = input("tu veux du popcorn ?(oui/non")
    if pop.upper() == "OUI":
        prix += 5
    elif pop.upper() != "OUI" and pop.upper() != "NON":
        while pop.upper() != "OUI" or pop.upper() != "NON":
            pop = input("rentre une réponse correcte stp")
            print(pop.upper())
            if pop.upper() == "NON":
                break
            elif pop.upper() == "OUI":
                prix += 5
                break
    print(f"ça fera {prix}€ stp")

place_cine()