# Engineering Unit Converter

A simple command-line Python tool that converts between units commonly
used in mechanical engineering — length, temperature, pressure, and torque.

## What it does
Converts between:
- Millimeters ↔ Inches
- Celsius ↔ Fahrenheit
- PSI ↔ Bar
- Newton-metres ↔ Pound-feet (torque)

## Why I built this
During my mechanical engineering coursework and internships, I constantly
needed to convert between metric and imperial units — and often reached
for random online converters. This project brings the ones I use most
into a single, simple tool, and was also my way of practicing core Python
concepts: functions, dictionaries, and handling user input safely.

## How to run it
```bash
python converter.py
```

Then follow the on-screen menu — pick a conversion number and enter a value.

## Example
```
Choose a conversion (0-8): 3
Enter value for Celsius -> Fahrenheit: 100
Result: 100.0 -> 212.0000
```

## Possible next steps
- Add a simple GUI using Tkinter
- Add more unit categories (length in meters/feet, force, energy)
- Turn it into a small web app using Flask
