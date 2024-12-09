print("Ik zal de stelling van pythagoras voor je gebruiken om de afstand tussen twee punten te berekenen.")
#Gegevens vragen.
x1 = float(input("Wat is de x-coördinaat van het eerste punt?"))
y1 = float(input("Wat is de y-coördinaat van het eerste punt?"))
x2 = float(input("Wat is de x-coördinaat van het tweede punt?"))
y2 = float(input("Wat is de y-coördinaat van het tweede punt?"))

#Afstand berekenen.
import wiskunde
afstand = wiskunde.Wiskunde.BerekenAfstandTussenPunten(x1,y1,x2,y2)

#Antwoord geven
print(f"De afstand tussen deze punten is {afstand}.")