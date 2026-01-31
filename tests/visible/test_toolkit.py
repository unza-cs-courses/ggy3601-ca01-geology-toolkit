"""
Coding Assignment 1 Visible Tests - Geology Toolkit
====================================================

These tests verify basic functionality of the geology_toolkit module.
Hidden tests will cover additional edge cases and integration scenarios.
"""

import sys
import math
from pathlib import Path

import pytest

# Add src to path for imports
SRC_DIR = Path(__file__).parent.parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from geology_toolkit import (
    calculate_density,
    calculate_porosity,
    classify_ore_grade,
    estimate_drilling_cost,
    calculate_sample_statistics,
    load_samples_from_file,
    process_samples_and_save
)


# =============================================================================
# DENSITY CALCULATION TESTS
# =============================================================================

class TestDensity:
    """Tests for calculate_density function."""

    def test_basic_calculation(self):
        """Should correctly calculate density."""
        result = calculate_density(15.5, 5.0)
        assert result == pytest.approx(3.1, rel=0.01)

    def test_different_values(self):
        """Should handle various mass and volume combinations."""
        assert calculate_density(10.0, 4.0) == pytest.approx(2.5)
        assert calculate_density(25.0, 10.0) == pytest.approx(2.5)
        assert calculate_density(100.0, 50.0) == pytest.approx(2.0)

    def test_returns_float(self):
        """Should return a float value."""
        result = calculate_density(10.0, 4.0)
        assert isinstance(result, float)

    def test_negative_mass_raises_error(self):
        """Should raise ValueError for negative mass."""
        with pytest.raises(ValueError):
            calculate_density(-5.0, 2.0)

    def test_zero_volume_raises_error(self):
        """Should raise ValueError for zero volume."""
        with pytest.raises(ValueError):
            calculate_density(10.0, 0.0)

    def test_negative_volume_raises_error(self):
        """Should raise ValueError for negative volume."""
        with pytest.raises(ValueError):
            calculate_density(10.0, -2.0)


# =============================================================================
# POROSITY CALCULATION TESTS
# =============================================================================

class TestPorosity:
    """Tests for calculate_porosity function."""

    def test_basic_calculation(self):
        """Should correctly calculate porosity."""
        # Porosity = (1 - 2400/2650) * 100 = 9.43%
        result = calculate_porosity(2400, 2650)
        assert result == pytest.approx(9.43, rel=0.01)

    def test_zero_porosity(self):
        """Should return 0 when bulk equals grain density."""
        result = calculate_porosity(2650, 2650)
        assert result == pytest.approx(0.0)

    def test_high_porosity(self):
        """Should handle high porosity values."""
        # Porosity = (1 - 1500/2500) * 100 = 40%
        result = calculate_porosity(1500, 2500)
        assert result == pytest.approx(40.0)

    def test_returns_float(self):
        """Should return a float value."""
        result = calculate_porosity(2400, 2650)
        assert isinstance(result, float)

    def test_negative_bulk_density_raises_error(self):
        """Should raise ValueError for negative bulk density."""
        with pytest.raises(ValueError):
            calculate_porosity(-100, 2650)

    def test_bulk_greater_than_grain_raises_error(self):
        """Should raise ValueError when bulk > grain density."""
        with pytest.raises(ValueError):
            calculate_porosity(3000, 2650)


# =============================================================================
# ORE CLASSIFICATION TESTS
# =============================================================================

class TestOreClassification:
    """Tests for classify_ore_grade function."""

    def test_gold_high_grade(self):
        """Should classify high gold grades correctly."""
        assert classify_ore_grade(5.0, 'gold') == 'High'
        assert classify_ore_grade(10.0, 'gold') == 'High'

    def test_gold_medium_grade(self):
        """Should classify medium gold grades correctly."""
        assert classify_ore_grade(2.0, 'gold') == 'Medium'
        assert classify_ore_grade(3.5, 'gold') == 'Medium'
        assert classify_ore_grade(4.9, 'gold') == 'Medium'

    def test_gold_low_grade(self):
        """Should classify low gold grades correctly."""
        assert classify_ore_grade(0.5, 'gold') == 'Low'
        assert classify_ore_grade(1.0, 'gold') == 'Low'
        assert classify_ore_grade(1.9, 'gold') == 'Low'

    def test_gold_subeconomic(self):
        """Should classify sub-economic gold grades correctly."""
        assert classify_ore_grade(0.1, 'gold') == 'Sub-economic'
        assert classify_ore_grade(0.4, 'gold') == 'Sub-economic'

    def test_returns_string(self):
        """Should return a string classification."""
        result = classify_ore_grade(3.0, 'gold')
        assert isinstance(result, str)

    def test_invalid_commodity_raises_error(self):
        """Should raise ValueError for unknown commodity."""
        with pytest.raises(ValueError):
            classify_ore_grade(3.0, 'platinum')

    def test_default_commodity_is_gold(self):
        """Should default to gold commodity."""
        assert classify_ore_grade(3.0) == classify_ore_grade(3.0, 'gold')


# =============================================================================
# DRILLING COST TESTS
# =============================================================================

class TestDrillingCost:
    """Tests for estimate_drilling_cost function."""

    def test_soft_rock_cost(self):
        """Should calculate cost for soft rock correctly."""
        # Cost = 75 * 100 * 1.0 * 1.0 = 7500
        result = estimate_drilling_cost(100, 'soft')
        assert result == pytest.approx(7500.0, rel=0.1)

    def test_medium_rock_cost(self):
        """Should calculate cost for medium rock correctly."""
        # Cost = 75 * 100 * 1.5 * 1.0 = 11250
        result = estimate_drilling_cost(100, 'medium')
        assert result == pytest.approx(11250.0, rel=0.1)

    def test_hard_rock_cost(self):
        """Should calculate cost for hard rock correctly."""
        # Cost = 75 * 100 * 2.0 * 1.0 = 15000
        result = estimate_drilling_cost(100, 'hard')
        assert result == pytest.approx(15000.0, rel=0.1)

    def test_larger_diameter_increases_cost(self):
        """Should increase cost for larger diameter."""
        standard = estimate_drilling_cost(100, 'soft', 0.076)
        larger = estimate_drilling_cost(100, 'soft', 0.152)
        # Diameter doubled = cost * 4
        assert larger > standard * 3

    def test_returns_float(self):
        """Should return a float value."""
        result = estimate_drilling_cost(100, 'medium')
        assert isinstance(result, float)

    def test_invalid_hardness_raises_error(self):
        """Should raise ValueError for invalid hardness."""
        with pytest.raises(ValueError):
            estimate_drilling_cost(100, 'super_hard')

    def test_negative_depth_raises_error(self):
        """Should raise ValueError for negative depth."""
        with pytest.raises(ValueError):
            estimate_drilling_cost(-100, 'medium')


# =============================================================================
# STATISTICS TESTS
# =============================================================================

class TestStatistics:
    """Tests for calculate_sample_statistics function."""

    def test_basic_statistics(self):
        """Should calculate all statistics correctly."""
        grades = [1.0, 2.0, 3.0, 4.0, 5.0]
        stats = calculate_sample_statistics(grades)

        assert stats['count'] == 5
        assert stats['mean'] == pytest.approx(3.0)
        assert stats['min'] == pytest.approx(1.0)
        assert stats['max'] == pytest.approx(5.0)

    def test_returns_dict(self):
        """Should return a dictionary."""
        stats = calculate_sample_statistics([1.0, 2.0, 3.0])
        assert isinstance(stats, dict)

    def test_dict_has_required_keys(self):
        """Should have all required keys."""
        stats = calculate_sample_statistics([1.0, 2.0, 3.0])
        required_keys = ['count', 'mean', 'min', 'max', 'std']
        for key in required_keys:
            assert key in stats, f"Missing key: {key}"

    def test_single_value(self):
        """Should handle single value list."""
        stats = calculate_sample_statistics([5.0])
        assert stats['count'] == 1
        assert stats['mean'] == pytest.approx(5.0)
        assert stats['min'] == pytest.approx(5.0)
        assert stats['max'] == pytest.approx(5.0)
        assert stats['std'] == pytest.approx(0.0)

    def test_standard_deviation(self):
        """Should calculate sample standard deviation correctly."""
        # Sample std of [1,2,3,4,5] = sqrt(10/4) = 1.581
        grades = [1.0, 2.0, 3.0, 4.0, 5.0]
        stats = calculate_sample_statistics(grades)
        assert stats['std'] == pytest.approx(1.581, rel=0.01)

    def test_empty_list_raises_error(self):
        """Should raise ValueError for empty list."""
        with pytest.raises(ValueError):
            calculate_sample_statistics([])


# =============================================================================
# FILE I/O TESTS
# =============================================================================

class TestFileOperations:
    """Tests for file I/O functions."""

    def test_load_returns_list(self, sample_data_path):
        """Should return a list of samples."""
        if not sample_data_path.exists():
            pytest.skip("Sample data file not found")
        samples = load_samples_from_file(str(sample_data_path))
        assert isinstance(samples, list)

    def test_load_returns_dicts(self, sample_data_path):
        """Should return list of dictionaries."""
        if not sample_data_path.exists():
            pytest.skip("Sample data file not found")
        samples = load_samples_from_file(str(sample_data_path))
        assert len(samples) > 0
        assert isinstance(samples[0], dict)

    def test_samples_have_required_fields(self, sample_data_path):
        """Each sample should have required fields."""
        if not sample_data_path.exists():
            pytest.skip("Sample data file not found")
        samples = load_samples_from_file(str(sample_data_path))
        required_fields = ['sample_id', 'rock_type', 'grade', 'depth']
        for field in required_fields:
            assert field in samples[0], f"Missing field: {field}"

    def test_nonexistent_file_raises_error(self):
        """Should raise FileNotFoundError for missing file."""
        with pytest.raises(FileNotFoundError):
            load_samples_from_file('/nonexistent/path/file.csv')

    def test_process_returns_count(self, sample_data_path, temp_output_path):
        """Should return count of processed samples."""
        if not sample_data_path.exists():
            pytest.skip("Sample data file not found")
        count = process_samples_and_save(str(sample_data_path), str(temp_output_path))
        assert isinstance(count, int)
        assert count > 0

    def test_process_creates_output_file(self, sample_data_path, temp_output_path):
        """Should create output file."""
        if not sample_data_path.exists():
            pytest.skip("Sample data file not found")
        process_samples_and_save(str(sample_data_path), str(temp_output_path))
        assert temp_output_path.exists()


# =============================================================================
# INTEGRATION TESTS
# =============================================================================

class TestIntegration:
    """Integration tests combining multiple functions."""

    def test_density_in_expected_range(self):
        """Calculated densities should be in realistic geological range."""
        # Typical rock densities: 2000-3500 kg/m^3
        density = calculate_density(15.0, 5.5)  # ~2727 kg/m^3
        assert 1500 < density < 4000

    def test_porosity_in_valid_range(self):
        """Porosity should be between 0 and 100."""
        porosity = calculate_porosity(2200, 2650)
        assert 0 <= porosity <= 100

    def test_classification_consistency(self):
        """Higher grades should not get lower classifications."""
        # Gold thresholds: High >= 5.0, Medium >= 2.0, Low >= 0.5
        low = classify_ore_grade(0.5, 'gold')
        medium = classify_ore_grade(2.0, 'gold')
        high = classify_ore_grade(5.0, 'gold')

        assert low in ['Low', 'Sub-economic']
        assert medium in ['Low', 'Medium', 'High']
        assert high == 'High'

    def test_drilling_cost_increases_with_depth(self):
        """Deeper holes should cost more."""
        shallow = estimate_drilling_cost(100, 'medium')
        deep = estimate_drilling_cost(500, 'medium')
        assert deep > shallow

    def test_drilling_cost_increases_with_hardness(self):
        """Harder rock should cost more."""
        soft = estimate_drilling_cost(100, 'soft')
        hard = estimate_drilling_cost(100, 'hard')
        assert hard > soft
