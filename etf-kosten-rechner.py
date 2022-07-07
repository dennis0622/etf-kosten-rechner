#Eingabe der Portfoliodaten

etf_namen = []
etf_kosten = []
etf_gewichtung = []
i = 0
weiter = 'Ja'

print('Hallo, bitte geben Sie bis zu 3 ETFs mit den entsprechenden Kosten und deren Gewichtung im Portfolio ein.\n')

while i <= 2 and weiter == 'Ja':
    if weiter == 'Ja':
        etf_namen.append(input('\nWie heißt der ETF? ').upper())
        etf_kosten.append(float(input('Wie teuer ist der ETF in Prozent (z.B. 0.3)? ')))
        etf_gewichtung.append(float(input('Welchen Anteil hat der ETF am Gesamtportfolio in Prozent (z.B. 55)? ')))
        weiter = input('ETF eingeben (Ja oder Nein)?  ').title()
        i +=1




print()
print('ETFs:', etf_namen)
print('ETF Kosten:', etf_kosten)
print('ETF Gewichtung:', etf_gewichtung)
print()


#Gesamtkosten berechnen


index = 0
zähler = 0.0

for k in etf_kosten:
    zähler += etf_kosten[index] * etf_gewichtung[index]
    index += 1


nenner = sum(etf_gewichtung)
gew_ges_kosten = float(zähler / nenner)


print('Die TER-Gesamtkosten für das eingegebene Portfolio betragen {:.2f}%.'.format(gew_ges_kosten))
