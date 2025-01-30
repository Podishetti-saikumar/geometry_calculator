# geometry_calculator

A CLI tool to define 2D shapes and query their measurements.
## Setup
1. Clone the repository.
2. Run `python main.py`.


## Features
- **Shapes**: Point, Line, Circle, Rectangle.
- **Queries**: Distance, area, perimeter/circumference.

## Design
- **Classes**: Each shape has methods for relevant calculations.
- **REPL**: Uses a controlled `eval` environment for safe execution.

## Assumptions
- Rectangles defined by diagonal points.
- Optional features (Union/Intersection) not implemented.

## Challenges
- Accurate geometric calculations.
- Handling shape interactions and edge cases.