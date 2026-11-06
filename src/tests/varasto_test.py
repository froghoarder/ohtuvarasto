"""Unit tests for the warehouse storage class."""

import unittest

from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """Verify the storage class behavior for valid and invalid inputs."""

    def setUp(self):
        """Create a fresh storage instance for each test."""
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """A newly created storage should start empty."""
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivinen_tilavuus(self):
        """A negative capacity should be treated as zero."""
        self.varasto = Varasto(-457698498)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """The created storage should have the configured volume."""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uudella_varastolla_oikea_saldo(self):
        """The initial balance should be zero."""
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_liikaa_saldoa(self):
        """A starting balance above capacity should be capped."""
        self.varasto = Varasto(10, 25)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_uudella_varastolla_vaara_saldo(self):
        """A negative starting balance should be treated as zero."""
        self.varasto = Varasto(10, -387)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_saldoa(self):
        """Adding stock should increase the balance."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_liikaa_saldoa(self):
        """Adding more than capacity should fill the storage."""
        self.varasto.lisaa_varastoon(300)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_negatiivista_saldoa(self):
        """Negative additions should be ignored."""
        self.varasto.lisaa_varastoon(-3)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """After adding stock, free space should decrease accordingly."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Removing stock should return the removed quantity."""
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Removing stock should create free space."""
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_vaaralla_maaralla(self):
        """Negative removal requests should be ignored."""
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(-4)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_ottaminen_liian_suurella_maaralla(self):
        """Removing more than present should empty the storage."""
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_string(self):
        """The human-readable representation should match expected text."""
        self.assertAlmostEqual(
            str(self.varasto),
            "saldo = 0, vielä tilaa 10",
        )
