# truth2logic-tc

A minimal command-line tool for generating simplified Boolean logic expressions from a given truth table.

Designed for logic learners, circuit designers, and players of logic-based games like Turing Complete.

## Features

- Read truth table from JSON file
- Supports any number of input variables
- Outputs simplified Boolean expressions using and, or, not
- Outputs include fully parenthesized expressions for clarity

## Usage

Prepare a JSON file containing a list of truth table rows. Each row must include input values and a single "out" field.

Example: truth_table.json

[
    {"A": 0, "B": 0, "out": 0},
    {"A": 0, "B": 1, "out": 1},
    {"A": 1, "B": 0, "out": 0},
    {"A": 1, "B": 1, "out": 0}
]

Run the tool:

python main.py truth_table.json

Expected output:

OUT = (not A and B)

## Applications

- Boolean algebra simplification
- Digital logic verification
- Game logic design (e.g. Turing Complete)
- Teaching and learning logic circuits

## License

MIT License
