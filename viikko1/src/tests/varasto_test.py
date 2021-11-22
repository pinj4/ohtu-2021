import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_otetaan_liikaa(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(10)

        self.assertEqual(saatu_maara, 5)
    
    def test_laitetaan_liikaa(self):
        self.varasto.lisaa_varastoon(20)
        
        maara = self.varasto.saldo

        self.assertEqual(maara, 10)
    
    def test_ei_voi_lisätä_negatiivista(self):
        self.varasto.lisaa_varastoon(-2)

        maara = self.varasto.saldo

        self.assertEqual(maara, 0)
    
    def test_ei_voi_ottaa_negatiivista(self):
        self.varasto.ota_varastosta(-2)

        maara = self.varasto.saldo

        self.assertEqual(maara, 0)

    def test_ei_voi_asettaa_neg_tilavuutta(self):
        self.varasto = Varasto(-2)

        maara = self.varasto.tilavuus

        self.assertEqual(maara, 0)
    
    def test_ei_voi_asettaa_neg_saldoa(self):
        self.varasto = Varasto(5, -2)

        maara = self.varasto.saldo

        self.assertEqual(maara, 0)
    
    def test_saldo_oikein(self):
        self.varasto = Varasto(10, 20)

        maara = self.varasto.saldo

        self.assertEqual(maara, 10)
    
    def test_printtaa_oikein(self):
        self.varasto.lisaa_varastoon(5)

        printattu = str(self.varasto)

        self.assertAlmostEqual("saldo = 5, vielä tilaa 5", printattu)
