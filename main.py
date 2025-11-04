preis_erwachsene = 5.0
preis_kinder = 2.5
preis_premium = 3.0
preis_basis = 4.0
preis_jugendlich = 3.5
glas_sekt_preis = 0.75
erwachsene_gesamt = 0


def tarif_abfragen():
    global erwachsene_gesamt
    print(" Hallo, geben Sie bitte Ihr Alter ein.")
    alter_gast = int(input())

    if alter_gast < 14:
        print(" ### Eintritt Kinder ### ")
        print(" Preis: ", preis_kinder, " Euro ")

    elif 14 <= alter_gast <= 17:
        print(" ### Eintritt Jugendliche ### ")
        print(" Preis: ", preis_jugendlich, " Euro ")

    else:
        print(" Sind Sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich) ")
        print(" Wenn Sie Premium-Mitglied sind, geben Sie 'p' ein.")
        print(" Wenn Sie Basis-Mitglied sind, geben Sie 'b' ein.")
        print(" Wenn Sie kein Mitglied sind, drücken Sie eine beliebige andere Taste. ")
        antwort_rabatt = input()
        erwachsene_gesamt = erwachsene_gesamt + 1

        if antwort_rabatt == "p":
            print(" ### Eintritt Premium-Mitglied ### ")
            print(" Preis: ", preis_premium, " Euro ")

        elif antwort_rabatt == "b":
            print(" ### Eintritt Basis-Mitglied ### ")
            print(" Preis: ", preis_basis, " Euro ")
        else:
            print(" ### Eintritt Erwachsene (voller Preis) ### ")
            print(" Preis: ", preis_erwachsene, " Euro")


print(" ### Tarifauskunftsrechner Museum XXX ### ")
tarif_abfragen()

weitere_karte = ""
print(" Möchten Sie noch eine weitere Karte berechnen? (j/n) ")
weitere_karte = input()
while weitere_karte == "j":
    tarif_abfragen()
    print(" Möchten Sie noch eine weitere Karte berechnen? (j/n) ")
    weitere_karte = input()

print(" Möchten die Erwachsenen ein Glas Sekt je 0,75 Euro dazu? (j/n) ")
antwort_sekt = input()

if antwort_sekt == "j":
    print(" Wie viele von den", erwachsene_gesamt , " Erwachsenen möchten Sekt? ")
    anzahl_sekt = int(input())
    sekt_preis_gesamt = anzahl_sekt * glas_sekt_preis

    gesamt_preis = preis_erwachsene + sekt_preis_gesamt
    print(" Gesamtpreis: ", gesamt_preis, " Euro ")
else:
    print(" Kein Sekt gewählt. ")

print("Viel Spaß!")
