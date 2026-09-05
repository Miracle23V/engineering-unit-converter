"""
Engineering Unit Converter
---------------------------
A command-line tool that converts between units commonly used in
mechanical engineering coursework and industry: length, temperature,
pressure, and torque.

Built because I kept reaching for online converters during my
engineering coursework and internships — this puts them all in one
simple tool.

Usage:
    python converter.py
"""

def mm_to_inch(mm: float) -> float:
    return mm / 25.4


def inch_to_mm(inch: float) -> float:
    return inch * 25.4


def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9


def psi_to_bar(psi: float) -> float:
    return psi * 0.0689476


def bar_to_psi(bar: float) -> float:
    return bar / 0.0689476


def nm_to_lbft(nm: float) -> float:
    """Newton-metres to pound-feet (torque)."""
    return nm * 0.737562


def lbft_to_nm(lbft: float) -> float:
    return lbft / 0.737562


CONVERSIONS = {
    "1": ("mm -> inch", mm_to_inch),
    "2": ("inch -> mm", inch_to_mm),
    "3": ("Celsius -> Fahrenheit", celsius_to_fahrenheit),
    "4": ("Fahrenheit -> Celsius", fahrenheit_to_celsius),
    "5": ("PSI -> bar", psi_to_bar),
    "6": ("bar -> PSI", bar_to_psi),
    "7": ("N.m -> lb-ft (torque)", nm_to_lbft),
    "8": ("lb-ft -> N.m (torque)", lbft_to_nm),
}


def print_menu():
    print("\n" + "=" * 40)
    print("ENGINEERING UNIT CONVERTER")
    print("=" * 40)
    for key, (label, _) in CONVERSIONS.items():
        print(f"  {key}. {label}")
    print("  0. Exit")


def main():
    while True:
        print_menu()
        choice = input("\nChoose a conversion (0-8): ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        if choice not in CONVERSIONS:
            print("Invalid choice, try again.")
            continue

        label, func = CONVERSIONS[choice]
        try:
            value = float(input(f"Enter value for {label}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        result = func(value)
        print(f"Result: {value} -> {result:.4f}")


if __name__ == "__main__":
    main()
