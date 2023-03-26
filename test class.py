
class Batiments :

    def __init__(self, etages, adresse):
        self.etages = etages
        self.adresse = adresse
    
    def get_etages(self):
        return self.etages
    
    def get_adresse(self):
        return self.adresse
    
class Immeuble(Batiments):

    def __init__(self, etages, adresse, balcons):
        super().__init__(etages, adresse)
        self.balcons = balcons
    
    def get_balcons(self):
        return self.balcons
    
class Marcket(Batiments):

    def __init__(self, etages, adresse, rayons):
        super().__init__(etages, adresse)
        self.rayons = rayons
    
    def get_rayons(self):
        return self.rayons

class Bank(Batiments):

    def __init__(self, etages, adresse, name, vaults):
        super().__init__(etages, adresse)
        self.name = name
        self.vaults = vaults

    def get_name(self):
        return self.name

    def get_vaults(self):
        return self.vaults


imeuble1 = Immeuble(4, "3 rue des chanteurs", 13)
imeuble2 = Immeuble(3, "5 rue du paysan", 16)
imeuble3 = Immeuble(6, "9 rue mr.noname", 18)
imeuble4 = Immeuble(8, "17 rue du canal", 4)

sup1 = Marcket(1, "10 avenu lafarge", 4)
sup2 = Marcket(2, "7 avenu margesim", 45)

banque = Bank(3, "4 rue du pain", "banque de France", 42)

print(banque.get_name())