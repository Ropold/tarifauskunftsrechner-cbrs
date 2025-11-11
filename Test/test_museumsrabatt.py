import unittest
import sys
import os

# Add parent directory to path to import main module functions
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def berechne_eintrittspreis(alter: int, mitgliedschaft: str = None) -> float:
    """
    Berechnet den Eintrittspreis basierend auf Alter und Museumsclub-Mitgliedschaft.

    Args:
        alter: Alter des Gastes
        mitgliedschaft: 'p' für Premium, 'b' für Basis, None oder anderer Wert für keine Mitgliedschaft

    Returns:
        Der Eintrittspreis in Euro
    """
    preis_erwachsene = 5.0
    preis_kinder = 2.5
    preis_premium = 3.0
    preis_basis = 4.0
    preis_jugendlich = 3.5

    if alter < 14:
        # Kinder
        return preis_kinder
    elif 14 <= alter <= 17:
        # Jugendliche
        return preis_jugendlich
    else:
        # Erwachsene - Mitgliedschaft wird berücksichtigt
        if mitgliedschaft == "p":
            return preis_premium
        elif mitgliedschaft == "b":
            return preis_basis
        else:
            return preis_erwachsene


class TestMuseumsrabatt(unittest.TestCase):
    """
    Unit Tests für Museumsrabatt basierend auf Testfälle_Whiteboxtest_Museumsrabatt.md
    """

    def test_T1_kind_13_jahre(self):
        """
        T1: Alter 13, Mitgliedschaft nicht relevant
        Erwartet: 2,5 Euro (Kinderpreis)
        Bemerkung: lt. Kundenvorgabe ist die Mitgliedschaft nur für Erwachsene zu berücksichtigen.
        """
        preis = berechne_eintrittspreis(alter=13, mitgliedschaft=None)
        self.assertEqual(preis, 2.5, "Kinder unter 14 zahlen 2,5 Euro")

    def test_T2_jugendlich_15_jahre(self):
        """
        T2: Alter 15, Mitgliedschaft nicht relevant
        Erwartet: 3,5 Euro (Jugendpreis)
        """
        preis = berechne_eintrittspreis(alter=15, mitgliedschaft=None)
        self.assertEqual(preis, 3.5, "Jugendliche (14-17 Jahre) zahlen 3,5 Euro")

    def test_T3_erwachsener_18_jahre_premium(self):
        """
        T3: Alter 18, Premium-Mitgliedschaft
        Erwartet: 3 Euro (Premium-Rabatt)
        """
        preis = berechne_eintrittspreis(alter=18, mitgliedschaft="p")
        self.assertEqual(preis, 3.0, "Erwachsene mit Premium-Mitgliedschaft zahlen 3 Euro")

    def test_T4_erwachsener_18_jahre_basis(self):
        """
        T4: Alter 18, Basis-Mitgliedschaft
        Erwartet: 4 Euro (Basis-Rabatt)
        """
        preis = berechne_eintrittspreis(alter=18, mitgliedschaft="b")
        self.assertEqual(preis, 4.0, "Erwachsene mit Basis-Mitgliedschaft zahlen 4 Euro")

    def test_T5_erwachsener_18_jahre_kein_mitglied(self):
        """
        T5: Alter 18, keine Mitgliedschaft
        Erwartet: 5 Euro (voller Preis)
        """
        preis = berechne_eintrittspreis(alter=18, mitgliedschaft=None)
        self.assertEqual(preis, 5.0, "Erwachsene ohne Mitgliedschaft zahlen 5 Euro")


if __name__ == '__main__':
    unittest.main()