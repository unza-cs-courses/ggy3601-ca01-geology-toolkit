"""
GGY3601 Geology Calculation Toolkit
===================================

A comprehensive toolkit for geological calculations including:
- Physical property calculations (density, porosity)
- Ore grade classification
- Drilling cost estimation
- Statistical analysis of sample data
- File I/O operations

This module is designed for the GGY3601 Coding Assignment 1.

Author: [YOUR NAME]
Student ID: [YOUR ID]
"""

import csv
import math
from typing import List, Dict, Any, Optional


# =============================================================================
# CONSTANTS
# =============================================================================

# Default base drilling rate (dollars per meter)
BASE_DRILLING_RATE = 75  # Override with your assigned value

# Hardness multipliers for drilling cost estimation
HARDNESS_MULTIPLIERS = {
    'soft': 1.0,
    'medium': 1.5,
    'hard': 2.0,
    'very_hard': 2.5
}

# Ore grade classification thresholds by commodity
GRADE_THRESHOLDS = {
    'gold': {
        'high': 5.0,     # g/t
        'medium': 2.0,   # g/t
        'low': 0.5       # g/t
    },
    'copper': {
        'high': 2.0,     # %
        'medium': 1.0,   # %
        'low': 0.3       # %
    },
    'iron': {
        'high': 60.0,    # %
        'medium': 50.0,  # %
        'low': 40.0      # %
    }
}

# Default borehole diameter (meters)
DEFAULT_DIAMETER = 0.076  # 76mm


# =============================================================================
# PHYSICAL PROPERTY CALCULATIONS
# =============================================================================

def calculate_density(mass: float, volume: float) -> float:
    """
    Calculate the density of a sample.

    Density is calculated as mass divided by volume. This is a fundamental
    property used in various geological calculations.

    Args:
        mass: Mass of the sample in kilograms (must be positive)
        volume: Volume of the sample in cubic meters (must be positive)

    Returns:
        Density in kg/m^3

    Raises:
        ValueError: If mass or volume is zero or negative

    Example:
        >>> calculate_density(15.5, 5.2)
        2.980769230769231
    """
    # TODO: Implement this function
    # 1. Validate inputs (mass and volume must be positive)
    # 2. Calculate density using the formula: density = mass / volume
    # 3. Return the result
    pass


def calculate_porosity(bulk_density: float, grain_density: float) -> float:
    """
    Calculate the porosity of a rock sample.

    Porosity represents the fraction of void space in a rock and is calculated
    from the bulk and grain densities.

    Formula: porosity = (1 - bulk_density / grain_density) * 100

    Args:
        bulk_density: Bulk density in kg/m^3 (must be positive)
        grain_density: Grain density in kg/m^3 (must be positive and >= bulk_density)

    Returns:
        Porosity as a percentage (0-100)

    Raises:
        ValueError: If densities are invalid or bulk_density > grain_density

    Example:
        >>> calculate_porosity(2400, 2650)
        9.433962264150944
    """
    # TODO: Implement this function
    # 1. Validate inputs
    # 2. Check that bulk_density <= grain_density (physically meaningful)
    # 3. Calculate porosity using the formula
    # 4. Return the result
    pass


# =============================================================================
# ORE GRADE CLASSIFICATION
# =============================================================================

def classify_ore_grade(grade: float, commodity: str = 'gold') -> str:
    """
    Classify an ore grade as High, Medium, Low, or Sub-economic.

    Classification thresholds vary by commodity type. The function uses
    predefined thresholds for gold, copper, and iron.

    Args:
        grade: Ore grade value (units depend on commodity)
        commodity: Commodity type ('gold', 'copper', or 'iron')

    Returns:
        Classification string: 'High', 'Medium', 'Low', or 'Sub-economic'

    Raises:
        ValueError: If commodity is not recognized or grade is negative

    Example:
        >>> classify_ore_grade(3.5, 'gold')
        'Medium'
        >>> classify_ore_grade(1.5, 'copper')
        'Medium'
    """
    # TODO: Implement this function
    # 1. Validate the commodity type
    # 2. Validate the grade value
    # 3. Get the appropriate thresholds for the commodity
    # 4. Compare grade against thresholds and return classification
    pass


# =============================================================================
# DRILLING COST ESTIMATION
# =============================================================================

def estimate_drilling_cost(depth: float, rock_hardness: str,
                          diameter: float = DEFAULT_DIAMETER) -> float:
    """
    Estimate the cost of drilling a borehole.

    Cost is calculated based on depth, rock hardness, and borehole diameter.

    Formula: cost = base_rate * depth * hardness_multiplier * (diameter/0.076)^2

    Args:
        depth: Drilling depth in meters (must be positive)
        rock_hardness: Rock hardness category ('soft', 'medium', 'hard', 'very_hard')
        diameter: Borehole diameter in meters (default: 0.076m = 76mm)

    Returns:
        Estimated drilling cost in dollars

    Raises:
        ValueError: If depth is invalid or hardness category is not recognized

    Example:
        >>> estimate_drilling_cost(100, 'medium')
        11250.0
    """
    # TODO: Implement this function
    # 1. Validate depth (must be positive)
    # 2. Validate rock_hardness (must be in HARDNESS_MULTIPLIERS)
    # 3. Get the hardness multiplier
    # 4. Calculate cost using the formula
    # 5. Consider adding depth bonus for deep holes (see ASSIGNMENT.md)
    # 6. Return the result
    pass


# =============================================================================
# STATISTICAL ANALYSIS
# =============================================================================

def calculate_sample_statistics(grades: List[float]) -> Dict[str, float]:
    """
    Calculate statistical summary of a list of grade values.

    Computes count, mean, minimum, maximum, and standard deviation
    of the provided grade values.

    Args:
        grades: List of numeric grade values

    Returns:
        Dictionary with keys:
        - 'count': Number of samples
        - 'mean': Average grade
        - 'min': Minimum grade
        - 'max': Maximum grade
        - 'std': Sample standard deviation

    Raises:
        ValueError: If the list is empty

    Example:
        >>> stats = calculate_sample_statistics([1.0, 2.0, 3.0, 4.0, 5.0])
        >>> stats['mean']
        3.0
        >>> stats['std']
        1.5811388300841898
    """
    # TODO: Implement this function
    # 1. Validate input (list must not be empty)
    # 2. Calculate count
    # 3. Calculate mean
    # 4. Calculate min and max
    # 5. Calculate sample standard deviation
    #    Formula: sqrt(sum((x - mean)^2 for x in grades) / (n - 1))
    #    Note: For n=1, std should be 0
    # 6. Return dictionary with all statistics
    pass


# =============================================================================
# FILE I/O OPERATIONS
# =============================================================================

def load_samples_from_file(filename: str) -> List[Dict[str, Any]]:
    """
    Load sample data from a CSV file.

    Reads a CSV file containing sample data and returns a list of dictionaries,
    where each dictionary represents one sample record.

    Expected CSV columns:
    - sample_id: Unique identifier
    - rock_type: Rock classification
    - grade: Ore grade value
    - depth: Sample depth in meters
    - mass: Sample mass in kg
    - volume: Sample volume in cubic meters

    Args:
        filename: Path to the CSV file

    Returns:
        List of dictionaries, each containing sample data

    Raises:
        FileNotFoundError: If the file does not exist
        ValueError: If the file format is invalid

    Example:
        >>> samples = load_samples_from_file('data/sample_data.csv')
        >>> len(samples)
        50
        >>> samples[0]['sample_id']
        'GEO-001'
    """
    # TODO: Implement this function
    # 1. Open the CSV file
    # 2. Read the header row
    # 3. Validate that required columns exist
    # 4. Read each data row and convert to dictionary
    # 5. Convert numeric fields to appropriate types
    # 6. Handle errors gracefully
    # 7. Return the list of sample dictionaries
    pass


def process_samples_and_save(input_file: str, output_file: str) -> int:
    """
    Load samples, process them, and save results to a new file.

    For each sample:
    - Calculate density from mass and volume
    - Classify the ore grade
    - Add calculated values as new columns

    Args:
        input_file: Path to input CSV file
        output_file: Path to output CSV file

    Returns:
        Number of samples successfully processed

    Raises:
        FileNotFoundError: If input file does not exist
        ValueError: If input file format is invalid

    Example:
        >>> count = process_samples_and_save('data/sample_data.csv', 'output/results.csv')
        >>> print(f"Processed {count} samples")
        Processed 50 samples
    """
    # TODO: Implement this function
    # 1. Load samples using load_samples_from_file
    # 2. For each sample:
    #    a. Calculate density
    #    b. Classify ore grade
    #    c. Add new fields to the sample dictionary
    # 3. Write results to output CSV
    # 4. Return count of processed samples
    pass


# =============================================================================
# HELPER FUNCTIONS (Optional - add your own as needed)
# =============================================================================

# You can add private helper functions here to support your implementation.
# Prefix private functions with underscore, e.g., _validate_positive()


# =============================================================================
# MODULE TEST (runs when executed directly)
# =============================================================================

if __name__ == "__main__":
    print("GGY3601 Geology Toolkit")
    print("=" * 40)
    print("This module provides geological calculation functions.")
    print("Import it in your code or run main.py for a demonstration.")
    print()
    print("Available functions:")
    print("  - calculate_density(mass, volume)")
    print("  - calculate_porosity(bulk_density, grain_density)")
    print("  - classify_ore_grade(grade, commodity)")
    print("  - estimate_drilling_cost(depth, rock_hardness, diameter)")
    print("  - calculate_sample_statistics(grades)")
    print("  - load_samples_from_file(filename)")
    print("  - process_samples_and_save(input_file, output_file)")
