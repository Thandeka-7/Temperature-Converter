# 🌡️ Temperature Converter

A beautiful, modern Django-based temperature converter application with stunning animations and a premium user interface.

## 📋 Overview

This is a fully functional temperature converter built with Django that allows users to convert temperatures between Celsius, Fahrenheit, and Kelvin. The application features a gorgeous gradient background, smooth animations, and an intuitive user experience.

## ✨ Features

- **Bidirectional Conversion** - Convert FROM and TO any temperature unit (Celsius, Fahrenheit, Kelvin)
- **Modern UI Design** - Beautiful animated gradient background with floating decorations
- **Smooth Animations** - Glowing labels, bouncing arrows, shimmer effects, and button ripples
- **Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices
- **Real-time Validation** - Form validation with required fields
- **Success Feedback** - Visual confirmation when conversion is successful
- **Django Integration** - Full backend processing with CSRF protection
- **Decorative Elements** - Floating thermometer icons, pulsing title lines, and corner borders

## 🛠️ Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3
- **Styling**: Custom CSS with advanced animations
- **Form Handling**: Django POST/GET methods

## 📁 Project Structure

```
temperature-converter/
│
├── main/
│   ├── views.py                    # Temperature conversion logic
│   ├── urls.py                     # URL routing
│   └── templates/
│       └── Home.html  # Main template
│
└── Temp/
    └── urls.py                     # Main URL configuration

## 🧮 Conversion Logic

The converter uses a two-step process:
1. Convert input temperature to Celsius (base unit)
2. Convert from Celsius to the desired output unit

### Supported Conversions:
- **Celsius ↔ Fahrenheit**: `F = C × 9/5 + 32`
- **Celsius ↔ Kelvin**: `K = C + 273.15`
- **Fahrenheit ↔ Kelvin**: Via Celsius intermediate

## 📱 Responsive Design

The application is fully responsive with special mobile optimizations:
- Stacked layout on mobile devices
- Rotated arrow (vertical) for mobile view
- Adjusted padding and font sizes
- Hidden background decorations on small screens

## 🎯 Usage

1. **Enter Temperature** - Input the temperature value
2. **Select Input Unit** - Choose from Celsius, Fahrenheit, or Kelvin
3. **Select Output Unit** - Choose the target unit for conversion
4. **Click Convert** - Get instant results
5. **Clear** - Reset the form for a new conversion

## 📄 License

© 2025 Temperature Converter - A Modern Django Application

**Made with ❤️ and Django**