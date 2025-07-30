# Hirst Spot Painting

This project recreates a spot painting inspired by artist Damien Hirst using Python's Turtle graphics library. The program extracts a palette of colors from an image file (`hirt_painting.jpg`) using the `colorgram` library, then uses these colors to draw a grid of colored dots on the screen.

## Features
- Extracts 10 colors from a reference image
- Draws a 10x10 grid of dots, each spaced 50 pixels apart
- Each dot is randomly colored from the extracted palette
- Uses Turtle graphics for visual output

## How It Works
1. The program loads `hirt_painting.jpg` and extracts 10 colors.
2. It sets up the Turtle graphics window and prepares the turtle.
3. The turtle draws 10 rows and 10 columns of dots, moving right for each column and up for each new row.
4. Each dot is drawn with a random color from the palette.

## Requirements
- Python 3
- `turtle` (standard library)
- `colorgram.py` (install via `pip install colorgram.py`)

## How to Run
1. Make sure you have `hirt_painting.jpg` in the project folder.
2. Install dependencies:
   ```
   pip install colorgram.py
   ```
3. Run `main.py`:
   ```
   python main.py
   ```
4. Click the Turtle window to exit when finished.

## Inspiration
This project is inspired by the colorful spot paintings of Damien Hirst, using code to generate art with random colors and patterns.