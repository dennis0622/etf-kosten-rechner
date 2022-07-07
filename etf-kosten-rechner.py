etf_namen = []
etf_kosten = []
etf_gewichtung = []
i = 0
weiter = 'Ja'

print('Hallo, bitte geben Sie bis zu 3 ETFs mit den entsprechenden Kosten und deren Gewichtung im Portfolio ein.\n')

while i <= 2:
    etf_namen.append(input('Wie heißt der ETF? '))
    etf_kosten.append(input('Wie teuer ist der ETF? '))
    etf_gewichtung.append(input('Welchen Anteil hat der ETF am Gesamtportfolio? '))
    print()
    i +=1

print(etf_namen)
print(etf_kosten)
print(etf_gewichtung)


#def etf_rechner(name,kosten,gewichtung):
