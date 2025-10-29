# 📋 Lastenheft Tarifauskunftsrechner

## 1. 🎯 Visionen und Ziele

Für unseren Kassenbereich benötigen wir einen **Tarifrechner**, der mithilfe von Kundeneingaben je nach Alter oder Rabatt-Berechtigungen entsprechende Preise anzeigt. Hiermit möchten wir die **Warteschlangen an den Kassen verkürzen**.

---

## 2. 🎭 Rahmenbedingungen

**Zielgruppe:** Der Tarifrechner soll von den Kund:innen eigenständig bedient werden.

---

## 3. 🖥️ Kontext und Überblick

Der Tarifrechner soll als **Konsolenprogramm** (d.h. ohne grafische Benutzerschnittstelle) entwickelt werden, um den Besucher:innen bereits im Eingangsbereich ein authentisches Erlebnis zu ermöglichen.

---

## 4. ⚙️ Funktionale Anforderungen

### 4.1 ✅ Muss-Kriterien

#### 4.1.1 Alterseingabe
Alterseingabe von Kund:innen soll möglich sein

#### 4.1.2 Preiskategorien nach Alter
Auf Basis der Alterseingabe: Unterscheidung nach Kinder- und Erwachsenenpreis (und Konsolenausgabe):

| Alter | Kategorie | Preis |
|-------|-----------|-------|
| < 14 | Kinderpreis | 2,50 € |
| > 18 | Erwachsenenpreis | siehe 4.1.3 |

#### 4.1.3 Erwachsenen-Tarife nach Mitgliedschaft
Nur für Erwachsene: Unterscheidung nach folgenden Kategorien und entsprechende Konsolenausgabe des Eintrittspreises:

| Mitgliedschaft | Preis |
|----------------|-------|
| ⭐ Premiummitgliedschaft | 3 € |
| 🔹 Basismitgliedschaft | 4 € |
| ❌ Keine Mitgliedschaft | 5 € |

#### 4.1.4 Jugendtarif
Ermäßigung für Jugendliche ab 14 und älter bis einschließlich 17: **3,50 €**

#### 4.1.5 Abschlussnachricht
Zusätzliche Bildschirmausgabe am Ende der Ticketabfrage:
> **"Viel Spaß!"**

#### 4.1.6 Wiederholte Abfrage
Wiederholte Abfrage nach Ausgabe eines Tarifs:
> **"Wollen Sie einen weiteren Tarif abfragen?"**

---

### 4.2 💡 Wunsch-Kriterien

#### 4.2.1 Sekt-Option für Premium-Mitglieder
Die erwachsenen Premium-Mitglieder sollen gefragt werden, ob sie für **0,75 € Aufpreis** ein Glas Sekt trinken möchten.

#### 4.2.2 Tagesticket-Option
Nach der Alterseingabe außerdem nach einem Ticket für einen **halben oder ganzen Tag** fragen:

**Tagesticket** (der "normale Preis" gilt für einen halben Tag):

| Kategorie | Halber Tag | Ganzer Tag | Besonderheit |
|-----------|------------|------------|--------------|
| Erwachsene (ohne Mitgliedschaft) | 5 € | 10 € | - |
| Erwachsene (Premium) | 3 € | 6 € | Sekt möglich |
| Erwachsene (Basis) | 4 € | 8 € | - |
| Kinder (< 14) | 2,50 € | 5 € | - |
| Jugendliche (14-17) | 3,50 € | 6 € | - |

#### 4.2.3 Gesamtsummen-Berechnung
Bei mehreren Ticketabfragen soll die Frage erscheinen:
> **"Möchten Sie den Ticketpreis zur Gesamtsumme addieren?"**

Zum Ende soll die **Gesamtsumme** der addierten Ticketpreise auf der Konsole ausgegeben werden.

#### 4.2.4 Grafische Gestaltung
Grafisch ansprechende Gestaltung auf der Konsole (z.B: Logo des Museums und / oder der OHMega.IT auf der Konsole "zeichnen")

#### 4.2.5 Mehrsprachigkeit
Zu Beginn auf Wunsch von Kund:innen Umstellung auf **Englisch**

---

## 5. 🏆 Qualitätsanforderungen

Keine besonderen Anforderungen.

---

## 📝 Notizen

- Projekt: Tarifauskunftsrechner für Museumsbereich
- Entwicklung: Konsolenprogramm (CLI)
- Sprache: Python