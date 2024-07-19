# Unit Converter

This is a PyQt5-based unit converter application that allows you to convert values between different units of time, distance, speed, and area.

## Features

- Convert units of Time: Seconds, Minutes, Hours, Days
- Convert units of Distance: Millimeters, Centimeters, Meters, Kilometers
- Convert units of Speed: m/s, km/h, mph, ft/s
- Convert units of Area: sq.mm, sq.cm, sq.m, sq.km, hectares

## Prerequisites

- Python 3.x
- PyQt5

## Installation

1. Install Python 3 from the [official website](https://www.python.org/).

2. Install PyQt5 using pip:
    ```bash
    pip install PyQt5
    ```

3. Download or clone this repository.

## Usage

1. Navigate to the directory where the script is located.

2. Run the script:
    ```bash
    python main.py
    ```

3. The unit converter window will appear. Select the category, the units to convert from and to, input the value, and click the "Convert" button to see the result.

## Code Explanation

### Main Window

The main window of the application is created using the `UnitConverter` class which is a subclass of `QWidget`. It initializes the UI components, such as input fields, combo boxes for unit selection, and the convert button.

### Unit Categories

The application supports four categories of units: Time, Distance, Speed, and Area. Depending on the selected category, the units available for conversion are updated.

### Conversion Logic

Each category has its own conversion logic implemented in separate methods: `convert_time`, `convert_distance`, `convert_speed`, and `convert_area`. These methods use dictionaries to map units to their conversion factors and perform the conversion based on the input value and selected units.

## License

[This project is licensed under the MIT License.](LICENSE).
