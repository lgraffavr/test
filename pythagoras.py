import wiskunde
import punt
class Pythagoras:
    def KrijgSchuineZijde(rechte_zijde_a, rechte_zijde_b):
        c_kwadraat = pow(rechte_zijde_a,2) + pow(rechte_zijde_b,2)
        c = wiskunde.Wiskunde.Wortel(c_kwadraat)
        return c
    

