preis_erwachsene = 5.0
preis_kinder = 2.5
preis_premium = 3.0
preis_basis = 4.0
preis_jugendlich = 3.5
glas_sekt_preis = 0.75
erwachsene_gesamt = 0
gesamt_preis = 0.0


def tarif_abfragen():
    global erwachsene_gesamt
    global gesamt_preis
    print(" Hallo, geben Sie bitte Ihr Alter ein.")
    alter_gast = int(input())

    if alter_gast < 14:
        print(" ### Eintritt Kinder ### ")
        print(" Preis: ", preis_kinder, " Euro ")
        gesamt_preis = gesamt_preis + preis_kinder

    elif 14 <= alter_gast <= 17:
        print(" ### Eintritt Jugendliche ### ")
        print(" Preis: ", preis_jugendlich, " Euro ")
        gesamt_preis = gesamt_preis + preis_jugendlich

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
            gesamt_preis = gesamt_preis + preis_premium

        elif antwort_rabatt == "b":
            print(" ### Eintritt Basis-Mitglied ### ")
            print(" Preis: ", preis_basis, " Euro ")
            gesamt_preis = gesamt_preis + preis_basis
        else:
            print(" ### Eintritt Erwachsene (voller Preis) ### ")
            print(" Preis: ", preis_erwachsene, " Euro")
            gesamt_preis = gesamt_preis + preis_erwachsene


print(" ### Tarifauskunftsrechner Museum XXX ### ")
tarif_abfragen()

print(" Möchten Sie noch eine weitere Karte berechnen? (j/n) ")
weitere_karte = input()
while weitere_karte == "j":
    tarif_abfragen()
    print(" Möchten Sie noch eine weitere Karte berechnen? (j/n) ")
    weitere_karte = input()

if erwachsene_gesamt > 0:
    print(" Möchten die Erwachsenen ein Glas Sekt je 0,75 Euro dazu? (j/n) ")
    antwort_sekt = input()

    if antwort_sekt == "j":
        if erwachsene_gesamt == 1:
            gesamt_preis = gesamt_preis + 0.75
            print(" Ein Sektglas wurde zum Gesamtpreis hinzugefügt. ")
        else:
            print(" Wie viele von den", erwachsene_gesamt , " Erwachsenen möchten Sekt? ")
            anzahl_sekt = int(input())
            if anzahl_sekt > erwachsene_gesamt:
                anzahl_sekt = erwachsene_gesamt
                print("Man kann nur einen Sekt pro Erwachsenen nehmen")
                print("Es werden nur", anzahl_sekt, " Sektgläser berechnet.")
            sekt_preis_gesamt = anzahl_sekt * glas_sekt_preis
            gesamt_preis = gesamt_preis + sekt_preis_gesamt
    else:
        print(" Kein Sekt gewählt. ")

print("Der Gesamtpreis beträgt: ", gesamt_preis, " Euro ")
print("Viel Spaß!")
