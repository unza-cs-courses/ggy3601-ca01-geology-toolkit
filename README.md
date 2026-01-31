# GGY3601 Coding Assignment 1: Geology Calculation Toolkit

**Weight:** 15% of final grade
**Due:** Week 7
**Type:** Open-ended design assignment

## Purpose

This coding assignment challenges you to design and implement a comprehensive geology calculation toolkit. Unlike the structured labs, this assignment gives you freedom to design your own solution while meeting the specified requirements.

## Learning Outcomes

By completing this assignment, you will be able to:
- Design and implement a modular Python toolkit
- Apply geological calculation formulas programmatically
- Process and analyze geological sample data from files
- Implement robust error handling and input validation
- Write comprehensive documentation for your code

## Assignment Overview

You will create a Python module (`geology_toolkit.py`) that provides functions for common geological calculations and data processing. The toolkit must handle:

1. **Physical property calculations** (density, porosity)
2. **Ore grade classification** based on commodity thresholds
3. **Drilling cost estimation** with variable parameters
4. **Statistical analysis** of sample datasets
5. **File I/O** for loading and saving processed data

## Your Personalized Assignment

**See `ASSIGNMENT.md` for your unique parameters and test values.**

The ASSIGNMENT.md file contains your student-specific values including:
- Primary commodity for classification
- Rock hardness options
- Base drilling rate
- Depth thresholds
- Number of test samples

## Repository Structure

```
.
├── src/
│   ├── geology_toolkit.py    # Your toolkit module (implement this)
│   └── main.py               # Demonstration program
├── tests/
│   └── visible/              # Automated tests (visible to you)
├── data/
│   └── sample_data.csv       # Sample data for processing
├── ASSIGNMENT.md             # Your unique assignment parameters
└── README.md                 # This file
```

## Required Functions

Your `geology_toolkit.py` must implement these functions:

### 1. calculate_density(mass, volume)
Calculate the density of a sample.

**Formula:** `density = mass / volume`

**Parameters:**
- `mass` (float): Mass in kilograms
- `volume` (float): Volume in cubic meters

**Returns:** float - Density in kg/m^3

**Raises:** ValueError for invalid inputs (negative or zero values)

### 2. calculate_porosity(bulk_density, grain_density)
Calculate the porosity of a rock sample.

**Formula:** `porosity = (1 - bulk_density / grain_density) * 100`

**Parameters:**
- `bulk_density` (float): Bulk density in kg/m^3
- `grain_density` (float): Grain density in kg/m^3

**Returns:** float - Porosity as a percentage (0-100)

**Raises:** ValueError for invalid inputs

### 3. classify_ore_grade(grade, commodity='gold')
Classify an ore grade as High, Medium, Low, or Sub-economic.

**Thresholds (Gold):**
- High: grade >= 5.0 g/t
- Medium: grade >= 2.0 g/t
- Low: grade >= 0.5 g/t
- Sub-economic: grade < 0.5 g/t

**Parameters:**
- `grade` (float): Ore grade value
- `commodity` (str): Commodity type (default: 'gold')

**Returns:** str - Classification ('High', 'Medium', 'Low', 'Sub-economic')

### 4. estimate_drilling_cost(depth, rock_hardness, diameter=0.076)
Estimate the cost of drilling a borehole.

**Formula:** `cost = base_rate * depth * hardness_multiplier * (diameter / 0.076)^2`

**Hardness Multipliers:**
- soft: 1.0
- medium: 1.5
- hard: 2.0
- very_hard: 2.5

**Parameters:**
- `depth` (float): Drilling depth in meters
- `rock_hardness` (str): Rock hardness category
- `diameter` (float): Borehole diameter in meters (default: 0.076m = 76mm)

**Returns:** float - Estimated cost

**Raises:** ValueError for invalid hardness category

### 5. calculate_sample_statistics(grades)
Calculate statistical summary of a list of grade values.

**Parameters:**
- `grades` (list): List of numeric grade values

**Returns:** dict with keys:
- `count`: Number of samples
- `mean`: Average grade
- `min`: Minimum grade
- `max`: Maximum grade
- `std`: Standard deviation

**Raises:** ValueError for empty list

### 6. load_samples_from_file(filename)
Load sample data from a CSV file.

**Parameters:**
- `filename` (str): Path to CSV file

**Returns:** list of dict - Each dict represents one sample record

**Raises:** FileNotFoundError, ValueError for invalid format

### 7. process_samples_and_save(input_file, output_file)
Load samples, calculate density for each, classify grades, and save results.

**Parameters:**
- `input_file` (str): Path to input CSV
- `output_file` (str): Path to output CSV

**Returns:** int - Number of samples processed

## Design Requirements

This is an **open-ended assignment**. You have flexibility in:

1. **Implementation approach** - Choose your own algorithms and data structures
2. **Error handling strategy** - Design robust error handling
3. **Code organization** - Structure your code for clarity and maintainability
4. **Additional helper functions** - Create private helper functions as needed

### Minimum Requirements

- All seven required functions must be implemented
- Functions must have proper docstrings
- Functions must validate inputs and raise appropriate exceptions
- Code must follow PEP 8 style guidelines

### Quality Criteria (Grading Rubric)

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Correctness | 40% | Functions produce correct results |
| Error Handling | 20% | Robust handling of edge cases and invalid inputs |
| Code Quality | 20% | Clean, readable, well-organized code |
| Documentation | 10% | Clear docstrings and comments |
| Testing | 10% | Visible tests pass |

## Getting Started

1. Clone this repository to your local machine
2. Read `ASSIGNMENT.md` for your unique parameters
3. Study the function stubs in `src/geology_toolkit.py`
4. Implement each function following the specifications
5. Test your code: `pytest tests/visible/ -v`
6. Use `src/main.py` to demonstrate your toolkit

## Key Formulas Reference

| Calculation | Formula |
|-------------|---------|
| Density | mass / volume |
| Porosity | (1 - bulk_density / grain_density) * 100 |
| Drilling Cost | base_rate * depth * hardness_mult * (diameter/0.076)^2 |

## Testing Your Code

Run the automated tests locally:

```bash
pytest tests/visible/ -v
```

Push to GitHub to see your score on the Actions tab.

**Note:** Hidden tests will be run after submission. They test additional edge cases and integration scenarios.

## Submission

Push your completed code to this repository before the deadline.

Your final grade combines:
- Visible test results (shown in GitHub Actions)
- Hidden test results (run after deadline)
- Code quality review

## Academic Integrity

- **ALLOWED:** Lecture notes, official Python documentation, asking tutors
- **NOT ALLOWED:** Copying code, AI tools, sharing solutions

All submissions are checked with plagiarism detection software.
