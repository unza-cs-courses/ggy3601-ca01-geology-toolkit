#!/usr/bin/env python3
"""
GGY3601 Coding Assignment 1: Geology Toolkit Demonstration
==========================================================

This program demonstrates the functionality of the geology_toolkit module.
It showcases each function with sample data and prints the results.

Update this file to use YOUR assigned values from ASSIGNMENT.md.

Author: [YOUR NAME]
Student ID: [YOUR ID]
"""

import os
import sys

# Add src directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from geology_toolkit import (
    calculate_density,
    calculate_porosity,
    classify_ore_grade,
    estimate_drilling_cost,
    calculate_sample_statistics,
    load_samples_from_file,
    process_samples_and_save
)


def print_header(title: str) -> None:
    """Print a formatted section header."""
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def print_subheader(title: str) -> None:
    """Print a formatted subsection header."""
    print()
    print(f"--- {title} ---")


def demonstrate_density_calculation() -> None:
    """Demonstrate the density calculation function."""
    print_subheader("Density Calculation")

    # Example samples
    samples = [
        {"name": "Granite core", "mass": 15.5, "volume": 5.8},
        {"name": "Basalt sample", "mass": 18.2, "volume": 6.1},
        {"name": "Sandstone piece", "mass": 12.0, "volume": 5.5},
    ]

    print("Calculating density for sample cores:\n")
    print(f"{'Sample':<20} {'Mass (kg)':<12} {'Volume (m^3)':<14} {'Density (kg/m^3)':<18}")
    print("-" * 64)

    for sample in samples:
        try:
            density = calculate_density(sample["mass"], sample["volume"])
            print(f"{sample['name']:<20} {sample['mass']:<12.1f} {sample['volume']:<14.2f} {density:<18.2f}")
        except ValueError as e:
            print(f"{sample['name']:<20} Error: {e}")

    # Demonstrate error handling
    print("\nTesting error handling:")
    try:
        calculate_density(-5.0, 2.0)
    except ValueError as e:
        print(f"  Invalid mass: {e}")

    try:
        calculate_density(10.0, 0)
    except ValueError as e:
        print(f"  Zero volume: {e}")


def demonstrate_porosity_calculation() -> None:
    """Demonstrate the porosity calculation function."""
    print_subheader("Porosity Calculation")

    rock_types = [
        {"type": "Dense granite", "bulk": 2600, "grain": 2650},
        {"type": "Porous sandstone", "bulk": 2100, "grain": 2650},
        {"type": "Weathered basalt", "bulk": 2300, "grain": 2900},
    ]

    print("Calculating porosity for different rock types:\n")
    print(f"{'Rock Type':<20} {'Bulk (kg/m^3)':<15} {'Grain (kg/m^3)':<16} {'Porosity (%)':<14}")
    print("-" * 65)

    for rock in rock_types:
        try:
            porosity = calculate_porosity(rock["bulk"], rock["grain"])
            print(f"{rock['type']:<20} {rock['bulk']:<15.0f} {rock['grain']:<16.0f} {porosity:<14.2f}")
        except ValueError as e:
            print(f"{rock['type']:<20} Error: {e}")


def demonstrate_ore_classification() -> None:
    """Demonstrate the ore grade classification function."""
    print_subheader("Ore Grade Classification")

    # TODO: Update with YOUR assigned commodity from ASSIGNMENT.md
    commodity = "gold"  # Change to your assigned commodity

    print(f"Classification for commodity: {commodity.upper()}\n")

    test_grades = [0.2, 0.5, 1.0, 2.0, 3.5, 5.0, 8.0]

    print(f"{'Grade':<10} {'Classification':<20}")
    print("-" * 30)

    for grade in test_grades:
        try:
            classification = classify_ore_grade(grade, commodity)
            print(f"{grade:<10.1f} {classification:<20}")
        except ValueError as e:
            print(f"{grade:<10.1f} Error: {e}")


def demonstrate_drilling_cost() -> None:
    """Demonstrate the drilling cost estimation function."""
    print_subheader("Drilling Cost Estimation")

    # TODO: Update with YOUR assigned base rate and hardness options from ASSIGNMENT.md
    print("Estimating drilling costs for various scenarios:\n")

    scenarios = [
        {"depth": 100, "hardness": "soft", "diameter": 0.076},
        {"depth": 200, "hardness": "medium", "diameter": 0.076},
        {"depth": 300, "hardness": "hard", "diameter": 0.076},
        {"depth": 500, "hardness": "hard", "diameter": 0.100},
    ]

    print(f"{'Depth (m)':<12} {'Hardness':<12} {'Diameter (m)':<14} {'Cost ($)':<12}")
    print("-" * 50)

    for s in scenarios:
        try:
            cost = estimate_drilling_cost(s["depth"], s["hardness"], s["diameter"])
            print(f"{s['depth']:<12} {s['hardness']:<12} {s['diameter']:<14.3f} {cost:<12,.2f}")
        except ValueError as e:
            print(f"{s['depth']:<12} {s['hardness']:<12} {s['diameter']:<14.3f} Error: {e}")


def demonstrate_statistics() -> None:
    """Demonstrate the statistical analysis function."""
    print_subheader("Sample Statistics")

    # Sample grade data
    grades = [1.2, 2.5, 3.8, 1.9, 4.2, 2.1, 3.5, 1.8, 2.9, 3.1]

    print("Analyzing sample grades:")
    print(f"Data: {grades}\n")

    try:
        stats = calculate_sample_statistics(grades)
        print(f"{'Statistic':<15} {'Value':<12}")
        print("-" * 27)
        print(f"{'Count':<15} {stats['count']:<12}")
        print(f"{'Mean':<15} {stats['mean']:<12.3f}")
        print(f"{'Minimum':<15} {stats['min']:<12.3f}")
        print(f"{'Maximum':<15} {stats['max']:<12.3f}")
        print(f"{'Std Dev':<15} {stats['std']:<12.3f}")
    except ValueError as e:
        print(f"Error: {e}")


def demonstrate_file_operations() -> None:
    """Demonstrate file I/O operations."""
    print_subheader("File Operations")

    # Paths relative to project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    input_file = os.path.join(project_dir, "data", "sample_data.csv")
    output_file = os.path.join(project_dir, "output", "processed_results.csv")

    print(f"Loading samples from: {input_file}")

    try:
        samples = load_samples_from_file(input_file)
        print(f"Successfully loaded {len(samples)} samples\n")

        # Show first few samples
        print("First 5 samples:")
        print(f"{'ID':<12} {'Rock Type':<15} {'Grade':<10} {'Depth (m)':<12}")
        print("-" * 49)
        for sample in samples[:5]:
            print(f"{sample.get('sample_id', 'N/A'):<12} "
                  f"{sample.get('rock_type', 'N/A'):<15} "
                  f"{sample.get('grade', 'N/A'):<10} "
                  f"{sample.get('depth', 'N/A'):<12}")

        print(f"\n... and {len(samples) - 5} more samples")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
        print("Make sure the sample_data.csv file exists in the data/ directory.")
    except ValueError as e:
        print(f"Error reading file: {e}")

    # Demonstrate processing
    print("\nProcessing samples and saving results...")
    try:
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        count = process_samples_and_save(input_file, output_file)
        print(f"Successfully processed {count} samples")
        print(f"Results saved to: {output_file}")
    except Exception as e:
        print(f"Error processing samples: {e}")


def main() -> None:
    """Main function demonstrating all toolkit capabilities."""
    print_header("GGY3601 GEOLOGY CALCULATION TOOLKIT DEMONSTRATION")

    # TODO: Update these with YOUR assigned values from ASSIGNMENT.md
    print("\nStudent Configuration:")
    print("  Commodity: gold")           # Update with your value
    print("  Base Drilling Rate: $75/m") # Update with your value
    print("  Depth Threshold: 500m")     # Update with your value

    # Run all demonstrations
    demonstrate_density_calculation()
    demonstrate_porosity_calculation()
    demonstrate_ore_classification()
    demonstrate_drilling_cost()
    demonstrate_statistics()
    demonstrate_file_operations()

    print_header("DEMONSTRATION COMPLETE")
    print("\nAll functions have been demonstrated.")
    print("Check the output above for results and any errors.")
    print("\nNext steps:")
    print("1. Implement the functions in geology_toolkit.py")
    print("2. Run tests: pytest tests/visible/ -v")
    print("3. Update this demo with your assigned values")


if __name__ == "__main__":
    main()
