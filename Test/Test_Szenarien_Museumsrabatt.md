# Test-Szenarien für Tarifauskunftsrechner Museum

## Übersicht

Diese Datei enthält detaillierte Test-Szenarien für den Tarifauskunftsrechner mit Fokus auf verschiedene Benutzergruppen und Rabattstufen.

---

## Test-Szenario 1: Kinder unter 14 Jahren

**Beschreibung:** Kinder erhalten einen ermäßigten Eintrittspreis, unabhängig von einer Mitgliedschaft.

| Schritt | Aktion | Erwartetes Ergebnis |
|---------|--------|---------------------|
| 1 | Alter eingeben: 13 | System zeigt "### Eintritt Kinder ###" |
| 2 | - | Preis: 2,5 Euro |
| 3 | - | Keine Abfrage nach Museumsclub-Mitgliedschaft |

**Erwartetes Verhalten:**
- Preis: 2,5 Euro
- Keine Mitgliedschaftsabfrage
- Erwachsenenzähler wird nicht erhöht

---

## Test-Szenario 2: Jugendliche (14-17 Jahre)

**Beschreibung:** Jugendliche zahlen einen speziellen Jugendtarif.

| Schritt | Aktion | Erwartetes Ergebnis |
|---------|--------|---------------------|
| 1 | Alter eingeben: 15 | System zeigt "### Eintritt Jugendliche ###" |
| 2 | - | Preis: 3,5 Euro |
| 3 | - | Keine Abfrage nach Museumsclub-Mitgliedschaft |

**Erwartetes Verhalten:**
- Preis: 3,5 Euro
- Keine Mitgliedschaftsabfrage
- Erwachsenenzähler wird nicht erhöht

---

## Test-Szenario 3: Erwachsene mit Premium-Mitgliedschaft

**Beschreibung:** Erwachsene mit Premium-Mitgliedschaft erhalten den höchsten Rabatt.

| Schritt | Aktion | Erwartetes Ergebnis |
|---------|--------|---------------------|
| 1 | Alter eingeben: 18 | System fragt nach Museumsclub-Mitgliedschaft |
| 2 | Eingabe: p | System zeigt "### Eintritt Premium-Mitglied ###" |
| 3 | - | Preis: 3,0 Euro |

**Erwartetes Verhalten:**
- Preis: 3,0 Euro
- Erwachsenenzähler wird um 1 erhöht
- Berechtigt für Sekt-Angebot

---

## Test-Szenario 4: Erwachsene mit Basis-Mitgliedschaft

**Beschreibung:** Erwachsene mit Basis-Mitgliedschaft erhalten einen Rabatt.

| Schritt | Aktion | Erwartetes Ergebnis |
|---------|--------|---------------------|
| 1 | Alter eingeben: 25 | System fragt nach Museumsclub-Mitgliedschaft |
| 2 | Eingabe: b | System zeigt "### Eintritt Basis-Mitglied ###" |
| 3 | - | Preis: 4,0 Euro |

**Erwartetes Verhalten:**
- Preis: 4,0 Euro
- Erwachsenenzähler wird um 1 erhöht
- Berechtigt für Sekt-Angebot

---

## Test-Szenario 5: Erwachsene ohne Mitgliedschaft

**Beschreibung:** Erwachsene ohne Mitgliedschaft zahlen den vollen Preis.

| Schritt | Aktion | Erwartetes Ergebnis |
|---------|--------|---------------------|
| 1 | Alter eingeben: 30 | System fragt nach Museumsclub-Mitgliedschaft |
| 2 | Eingabe: n (oder beliebige Taste außer p/b) | System zeigt "### Eintritt Erwachsene (voller Preis) ###" |
| 3 | - | Preis: 5,0 Euro |

**Erwartetes Verhalten:**
- Preis: 5,0 Euro
- Erwachsenenzähler wird um 1 erhöht
- Berechtigt für Sekt-Angebot

---

## Test-Szenario 6: Mehrere Tickets

**Beschreibung:** Berechnung mehrerer Tickets mit verschiedenen Tarifen.

| Schritt | Aktion | Erwartetes Ergebnis |
|---------|--------|---------------------|
| 1 | Alter eingeben: 12 | Preis: 2,5 Euro |
| 2 | Weitere Karte: j | System fragt nach nächstem Alter |
| 3 | Alter eingeben: 18, Mitgliedschaft: p | Preis: 3,0 Euro |
| 4 | Weitere Karte: j | System fragt nach nächstem Alter |
| 5 | Alter eingeben: 35, Mitgliedschaft: n | Preis: 5,0 Euro |
| 6 | Weitere Karte: n | System geht zur Sekt-Abfrage |
| 7 | - | Gesamtpreis: 10,5 Euro |

**Erwartetes Verhalten:**
- Gesamtpreis: 10,5 Euro (2,5 + 3,0 + 5,0)
- Erwachsenenzähler: 2
- Sekt-Angebot für max. 2 Personen

---

## Test-Szenario 7: Sekt-Bestellung (Normal)

**Beschreibung:** Erwachsene bestellen Sekt im normalen Rahmen.

| Schritt | Aktion | Erwartetes Ergebnis |
|---------|--------|---------------------|
| 1 | 2 Erwachsene Tickets gekauft | Erwachsenenzähler: 2 |
| 2 | Sekt gewünscht: j | System fragt nach Anzahl |
| 3 | Anzahl Sekt: 2 | Sektpreis: 1,5 Euro (2 × 0,75) |
| 4 | - | Wird zum Gesamtpreis addiert |

**Erwartetes Verhalten:**
- Sektpreis: 1,5 Euro
- Keine Fehlermeldung
- Gesamtpreis wird korrekt erhöht

---

## Test-Szenario 8: Sekt-Bestellung (Überschreitung)

**Beschreibung:** Mehr Sekt bestellt als Erwachsene vorhanden.

| Schritt | Aktion | Erwartetes Ergebnis |
|---------|--------|---------------------|
| 1 | 2 Erwachsene Tickets gekauft | Erwachsenenzähler: 2 |
| 2 | Sekt gewünscht: j | System fragt nach Anzahl |
| 3 | Anzahl Sekt: 5 | System korrigiert auf 2 |
| 4 | - | Meldung: "Man kann nur einen Sekt pro Erwachsenen nehmen" |
| 5 | - | "Es werden nur 2 Sektgläser berechnet." |

**Erwartetes Verhalten:**
- Anzahl wird auf Erwachsenenzahl begrenzt
- Sektpreis: 1,5 Euro (2 × 0,75)
- Benutzer wird über Korrektur informiert

---

## Test-Szenario 9: Kein Sekt gewünscht

**Beschreibung:** Erwachsene lehnen Sekt-Angebot ab.

| Schritt | Aktion | Erwartetes Ergebnis |
|---------|--------|---------------------|
| 1 | 1 Erwachsener Ticket gekauft | Erwachsenenzähler: 1 |
| 2 | Sekt gewünscht: n | Meldung: "Kein Sekt gewählt." |
| 3 | - | Gesamtpreis bleibt unverändert |

**Erwartetes Verhalten:**
- Kein Aufpreis für Sekt
- Gesamtpreis nur aus Eintrittspreisen

---

## Test-Szenario 10: Nur Kinder (kein Sekt-Angebot)

**Beschreibung:** Wenn nur Kinder/Jugendliche Tickets kaufen, gibt es kein Sekt-Angebot.

| Schritt | Aktion | Erwartetes Ergebnis |
|---------|--------|---------------------|
| 1 | Alter eingeben: 10 | Preis: 2,5 Euro |
| 2 | Weitere Karte: j | System fragt nach nächstem Alter |
| 3 | Alter eingeben: 16 | Preis: 3,5 Euro |
| 4 | Weitere Karte: n | Kein Sekt-Angebot |
| 5 | - | Gesamtpreis: 6,0 Euro |

**Erwartetes Verhalten:**
- Keine Sekt-Abfrage
- Erwachsenenzähler: 0
- Gesamtpreis: 6,0 Euro

---

## Grenzwert-Tests

### Altersgrenze Kind/Jugendlicher

| Alter | Erwarteter Tarif | Preis |
|-------|------------------|-------|
| 13 | Kinder | 2,5 Euro |
| 14 | Jugendliche | 3,5 Euro |

### Altersgrenze Jugendlicher/Erwachsener

| Alter | Erwarteter Tarif | Preis (ohne Mitgliedschaft) |
|-------|------------------|------------------------------|
| 17 | Jugendliche | 3,5 Euro |
| 18 | Erwachsene | 5,0 Euro (mit Mitgliedschaftsabfrage) |

---

## Fehlerfall-Tests

### Ungültige Eingaben

| Test | Eingabe | Erwartetes Verhalten |
|------|---------|----------------------|
| Negativer Alter | -5 | Sollte Fehler abfangen (aktuell nicht implementiert) |
| Alter = 0 | 0 | Sollte Fehler abfangen (aktuell nicht implementiert) |
| Buchstabe statt Zahl | "abc" | Sollte Fehler abfangen (aktuell nicht implementiert) |
| Negative Sekt-Anzahl | -1 | Sollte Fehler abfangen (aktuell nicht implementiert) |

---

## Preisübersicht

| Kategorie | Preis |
|-----------|-------|
| Kinder (< 14) | 2,5 Euro |
| Jugendliche (14-17) | 3,5 Euro |
| Premium-Mitglied | 3,0 Euro |
| Basis-Mitglied | 4,0 Euro |
| Erwachsene (voller Preis) | 5,0 Euro |
| Glas Sekt | 0,75 Euro |