import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox, QHBoxLayout

class UnitConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Unit Converter')
        self.setGeometry(100, 100, 400, 200)  
        
        self.input_field = QLineEdit(self)
        
        self.output_field = QLineEdit(self)
        self.output_field.setReadOnly(True)
         
        self.categories = ["Time", "Distance", "Speed", "Area"]
        self.category_combo = QComboBox(self)
        self.category_combo.addItems(self.categories)
        self.category_combo.currentIndexChanged.connect(self.updateUnits)
        
        self.unit_from_combo = QComboBox(self)
        self.unit_to_combo = QComboBox(self)
        self.updateUnits()  
        
        self.convert_button = QPushButton('Convert', self)
        self.convert_button.clicked.connect(self.convert)
        
        vbox = QVBoxLayout()
        vbox.addWidget(QLabel('Select category:', self))
        vbox.addWidget(self.category_combo)
        
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel('From:', self))
        hbox.addWidget(self.unit_from_combo)
        hbox.addWidget(QLabel('To:', self))
        hbox.addWidget(self.unit_to_combo)
        
        vbox.addLayout(hbox)
        vbox.addWidget(QLabel('Value:', self))
        vbox.addWidget(self.input_field)
        vbox.addWidget(self.convert_button)
        vbox.addWidget(QLabel('Result:', self))
        vbox.addWidget(self.output_field)
        
        self.setLayout(vbox)
    
    def updateUnits(self):
        category = self.category_combo.currentText()
        if category == "Time":
            units = ["Seconds", "Minutes", "Hours", "Days"]
        elif category == "Distance":
            units = ["Millimeters", "Centimeters", "Meters", "Kilometers"]
        elif category == "Speed":
            units = ["m/s", "km/h", "mph", "ft/s"]
        elif category == "Area":
            units = ["sq.mm", "sq.cm", "sq.m", "sq.km", "hectares"]
        else:
            units = []
        
        self.unit_from_combo.clear()
        self.unit_to_combo.clear()
        self.unit_from_combo.addItems(units)
        self.unit_to_combo.addItems(units)
    
    def convert(self):
        category = self.category_combo.currentText()
        unit_from = self.unit_from_combo.currentText()
        unit_to = self.unit_to_combo.currentText()
        value = float(self.input_field.text())
        
        if category == "Time":
            result = self.convert_time(value, unit_from, unit_to)
        elif category == "Distance":
            result = self.convert_distance(value, unit_from, unit_to)
        elif category == "Speed":
            result = self.convert_speed(value, unit_from, unit_to)
        elif category == "Area":
            result = self.convert_area(value, unit_from, unit_to)
        
        self.output_field.setText(str(result))
    
    def convert_time(self, value, unit_from, unit_to):
        
        time_units = {"Seconds": 1, "Minutes": 60, "Hours": 3600, "Days": 86400}
        return value * time_units[unit_from] / time_units[unit_to]
    
    def convert_distance(self, value, unit_from, unit_to):
        
        distance_units = {"Millimeters": 0.001, "Centimeters": 0.01, "Meters": 1, "Kilometers": 1000}
        return value * distance_units[unit_from] / distance_units[unit_to]
    
    def convert_speed(self, value, unit_from, unit_to):
        
        speed_units = {"m/s": 1, "km/h": 0.277778, "mph": 0.44704, "ft/s": 0.3048}
        return value * speed_units[unit_from] / speed_units[unit_to]
    
    def convert_area(self, value, unit_from, unit_to):
        
        area_units = {"sq.mm": 1e-6, "sq.cm": 1e-4, "sq.m": 1, "sq.km": 1e6, "hectares": 1e4}
        return value * area_units[unit_from] / area_units[unit_to]

def main():
    app = QApplication(sys.argv)
    converter = UnitConverter()
    converter.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
