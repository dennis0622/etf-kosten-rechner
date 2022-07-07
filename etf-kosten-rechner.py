#Eingabe der Portfoliodaten

etf_namen = []
etf_kosten = []
etf_gewichtung = []
i = 0
weiter = 'Ja'

print('Hallo, bitte geben Sie bis zu 3 ETFs mit den entsprechenden Kosten und deren Gewichtung im Portfolio ein.\n')

while i <= 2:
    etf_namen.append(input('Wie heißt der ETF? ').upper())
    etf_kosten.append(float(input('Wie teuer ist der ETF? ')))
    etf_gewichtung.append(float(input('Welchen Anteil hat der ETF am Gesamtportfolio? ')))
    print()
    i +=1

print('ETFs:', etf_namen)
print('ETF Kosten:', etf_kosten)
print('ETF Gewichtung:', etf_gewichtung)
print()


#Gesamtkosten berechnen

i2 = 0
index = 0
zähler = 0.0

while i2 <= 2:
    zähler += etf_kosten[index] * etf_gewichtung[index]
    index += 1
    i2 += 1

nenner = sum(etf_gewichtung)
gew_ges_kosten = float(zähler / nenner)


print('Die TER-Gesamtkosten für das eingegebene Portfolio betragen {} %.'.format(gew_ges_kosten))
