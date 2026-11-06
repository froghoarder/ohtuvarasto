"""Demonstration script for the storage class."""

from varasto import Varasto


def print_initial_state(mehua, olutta):
    """Print the initial storage state."""
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")


def print_reading_values(olutta):
    """Print the stock values and remaining capacity."""
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def print_addition_case(mehua):
    """Demonstrate adding and removing stock."""
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")


def print_error_cases():
    """Display invalid storage initialization scenarios."""
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def print_olut_overflow_case(olutta):
    """Display the overflow scenario for beer storage."""
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")


def print_mehu_overflow_case(mehua):
    """Display the invalid addition scenario for juice storage."""
    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")


def print_overflow_cases(olutta, mehua):
    """Display overflow and negative-addition behavior."""
    print_olut_overflow_case(olutta)
    print_mehu_overflow_case(mehua)


def print_olut_removal_case(olutta):
    """Display the removal scenario for beer storage."""
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")


def print_mehu_removal_case(mehua):
    """Display the invalid removal scenario for juice storage."""
    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


def print_removal_cases(olutta, mehua):
    """Display valid and invalid stock-removal behavior."""
    print_olut_removal_case(olutta)
    print_mehu_removal_case(mehua)


def main():
    """Run the demonstration script for the storage class."""
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print_initial_state(mehua, olutta)
    print_reading_values(olutta)
    print_addition_case(mehua)
    print_error_cases()
    print_overflow_cases(olutta, mehua)
    print_removal_cases(olutta, mehua)


if __name__ == "__main__":
    main()
