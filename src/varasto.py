"""Warehouse storage logic with capacity and stock constraints."""


class Varasto:
    """Track stock levels within a maximum capacity."""

    def __init__(self, tilavuus, alku_saldo=0):
        self.tilavuus = self._validate_tilavuus(tilavuus)
        self.saldo = self._calculate_initial_balance(alku_saldo)

    @staticmethod
    def _validate_tilavuus(tilavuus):
        """Return a non-negative capacity value."""
        if tilavuus > 0.0:
            return tilavuus
        return 0.0

    def _calculate_initial_balance(self, alku_saldo):
        """Return a valid initial balance within the storage volume."""
        if alku_saldo < 0.0:
            return 0.0
        if alku_saldo <= self.tilavuus:
            return alku_saldo
        return self.tilavuus

    def paljonko_mahtuu(self):
        """Return remaining free space in the storage."""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """Add stock to the storage, ignoring negative inputs."""
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo += maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """Remove stock from storage and return the removed amount."""
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0
            return kaikki_mita_voidaan

        self.saldo -= maara
        return maara

    def __str__(self):
        """Return a human-readable description of the storage state."""
        return (
            f"saldo = {self.saldo}, "
            f"vielä tilaa {self.paljonko_mahtuu()}"
        )
