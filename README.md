# Pygame Drawing Application

This is a Python application that uses Pygame to create an interactive drawing environment with menu options for drawing, erasing, exporting coordinates, and hiding the menu.

## Installation

### Prerequisites
Ensure you have Python installed (Python 3.x recommended). You can download it from [python.org](https://www.python.org/downloads/).

### Install Dependencies
Use the following command to install the required dependencies:

```sh
pip install pygame
```

## Running the Application
To start the application, run the following command in your terminal or command prompt:

```sh
python main.py
```

## Features
- Draw on the screen within a defined perimeter box.
- Erase the drawing.
- Export drawn coordinates to `FlightCoordinates.csv`.
- Toggle the menu visibility.

## File Structure
```
project_directory/
│-- main.py  # Main application script
│-- config.py  # Configuration settings
│-- draw.py  # Drawing utility functions
```

## Exported Data
When exporting, a file `FlightCoordinates.csv` will be created with the following format:

```
"X","Y"
"100","200"
"150","250"
...
```

## Controls
- **Left Click**: Start drawing (if in DRAW mode) or erase (if in ERASE mode).
- **Mouse Scroll Up/Down**: Zoom in/out.
- **Menu Options**: Click on menu options to switch between modes.
- **Close Button**: Exit the application.

## License
This project is for educational purposes. Modify and expand as needed!
