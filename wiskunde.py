import pythagoras

class Wiskunde:
    def Wortel(getal):
        return pow(getal,0.5)
    def BerekenAfstandTussenPunten(punt1, punt2):
        hor_afstand = punt1.x - punt2.x
        ver_afstand = punt1.y - punt2.y
        afstand = pythagoras.Pythagoras.KrijgSchuineZijde(hor_afstand, ver_afstand)
        return afstand