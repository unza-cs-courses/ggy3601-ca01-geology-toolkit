# Your Assignment Parameters

These are your unique values for Coding Assignment 1. Use these exact values in your implementation.

## Your Configuration

| Parameter | Your Value |
|-----------|------------|
| Primary Commodity | {commodity} |
| Rock Hardness Options | {hardness_options} |
| Base Drilling Rate | ${base_drilling_rate} per meter |
| Depth Bonus Threshold | {depth_bonus_threshold} meters |
| Number of Test Samples | {num_test_samples} |

## Implementation Requirements

### Commodity-Specific Thresholds

Your toolkit must use the correct thresholds for your assigned commodity: **{commodity}**

#### Gold Classification (if commodity = 'gold')
- High: grade >= 5.0 g/t
- Medium: grade >= 2.0 g/t
- Low: grade >= 0.5 g/t
- Sub-economic: grade < 0.5 g/t

#### Copper Classification (if commodity = 'copper')
- High: grade >= 2.0%
- Medium: grade >= 1.0%
- Low: grade >= 0.3%
- Sub-economic: grade < 0.3%

#### Iron Classification (if commodity = 'iron')
- High: grade >= 60%
- Medium: grade >= 50%
- Low: grade >= 40%
- Sub-economic: grade < 40%

### Drilling Cost Calculation

Use your assigned base rate: **${base_drilling_rate}/meter**

Your available hardness options: **{hardness_options}**

| Hardness | Multiplier |
|----------|------------|
| soft | 1.0 |
| medium | 1.5 |
| hard | 2.0 |
| very_hard | 2.5 |

**Formula:** `cost = {base_drilling_rate} * depth * hardness_multiplier * (diameter / 0.076)^2`

**Depth Bonus:** For depths greater than {depth_bonus_threshold} meters, add a 25% surcharge to account for increased complexity.

### Data Processing

Your sample dataset contains **{num_test_samples}** records.

The `sample_data.csv` file has the following columns:
- `sample_id`: Unique identifier (e.g., "GEO-001")
- `rock_type`: Rock classification
- `grade`: Ore grade value
- `depth`: Sample depth in meters
- `mass`: Sample mass in kg
- `volume`: Sample volume in cubic meters

## Tasks

### Task 1: Physical Calculations (25 marks)

Implement `calculate_density()` and `calculate_porosity()`:

```python
# Example usage with your values
density = calculate_density(mass=15.5, volume=5.2)
print(f"Density: {density:.2f} kg/m^3")

porosity = calculate_porosity(bulk_density=2400, grain_density=2650)
print(f"Porosity: {porosity:.1f}%")
```

**Requirements:**
- Validate inputs (no negative or zero values)
- Raise ValueError with descriptive messages
- Return float values with appropriate precision

### Task 2: Ore Classification (20 marks)

Implement `classify_ore_grade()` using **{commodity}** thresholds:

```python
# Example usage
grade = 3.5
classification = classify_ore_grade(grade, commodity='{commodity}')
print(f"Grade {grade} is classified as: {classification}")
```

**Requirements:**
- Support your assigned commodity: {commodity}
- Handle edge cases (exactly on threshold values)
- Return one of: 'High', 'Medium', 'Low', 'Sub-economic'

### Task 3: Drilling Cost Estimation (20 marks)

Implement `estimate_drilling_cost()` with base rate ${base_drilling_rate}:

```python
# Example usage with your hardness options
cost = estimate_drilling_cost(
    depth=500,
    rock_hardness='{hardness_options}'.split(', ')[0],  # Use your first option
    diameter=0.076
)
print(f"Estimated cost: ${cost:.2f}")
```

**Requirements:**
- Use base rate: {base_drilling_rate}
- Support hardness options: {hardness_options}
- Apply 25% surcharge for depths > {depth_bonus_threshold}m
- Validate hardness input

### Task 4: Statistical Analysis (15 marks)

Implement `calculate_sample_statistics()`:

```python
# Example usage
grades = [1.2, 3.4, 2.1, 4.5, 0.8, 2.9, 1.5, 3.2]
stats = calculate_sample_statistics(grades)
print(f"Mean: {stats['mean']:.2f}")
print(f"Std Dev: {stats['std']:.2f}")
```

**Requirements:**
- Return dict with: count, mean, min, max, std
- Handle empty list (raise ValueError)
- Calculate std using sample standard deviation

### Task 5: File Processing (20 marks)

Implement `load_samples_from_file()` and `process_samples_and_save()`:

```python
# Example usage
samples = load_samples_from_file('data/sample_data.csv')
print(f"Loaded {len(samples)} samples")

count = process_samples_and_save('data/sample_data.csv', 'output/results.csv')
print(f"Processed {count} samples")
```

**Requirements:**
- Parse CSV correctly
- Calculate density for each sample
- Classify each sample's grade
- Save results with new columns

## Testing Your Implementation

Run the visible tests:

```bash
pytest tests/visible/ -v
```

Expected output:
```
tests/visible/test_toolkit.py::TestDensity::test_basic_calculation PASSED
tests/visible/test_toolkit.py::TestDensity::test_validation PASSED
...
```

## Demonstration Program

Update `src/main.py` to demonstrate your toolkit using your unique values:

```python
from geology_toolkit import *

# Use YOUR assigned values
print("=" * 50)
print("GGY3601 Geology Toolkit Demonstration")
print("Commodity:", "{commodity}")
print("Base Drilling Rate: ${base_drilling_rate}/m")
print("=" * 50)

# Demonstrate each function...
```

## Submission Checklist

Before submitting, verify:

- [ ] All seven functions implemented in `geology_toolkit.py`
- [ ] Functions have proper docstrings
- [ ] Error handling for invalid inputs
- [ ] `main.py` demonstrates all functions
- [ ] All visible tests pass
- [ ] Code follows PEP 8 style

Push your code to GitHub before the deadline.
