import pythagoras

class Wiskunde:
    def Wortel(getal):
        return pow(getal,0.5)
    def BerekenAfstandTussenPunten(x1, y1, x2, y2):
        hor_afstand = x1 - x2
        ver_afstand = y1 - y2
        afstand = pythagoras.Pythagoras.KrijgSchuineZijde(hor_afstand, ver_afstand)
        return afstand