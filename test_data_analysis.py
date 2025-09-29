#!/usr/bin/env python3
"""
Test suite for the data analysis program.
"""

import unittest
from data_analysis import DataAnalyzer, generate_sample_data

class TestDataAnalyzer(unittest.TestCase):
    """Test cases for the DataAnalyzer class."""
    
    def setUp(self):
        """Set up test data."""
        self.test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.analyzer = DataAnalyzer(self.test_data)
    
    def test_summary_stats(self):
        """Test summary statistics calculation."""
        stats = self.analyzer.summary_stats()
        
        self.assertEqual(stats['count'], 10)
        self.assertAlmostEqual(stats['mean'], 5.5, places=2)
        self.assertAlmostEqual(stats['median'], 5.5, places=2)
        self.assertAlmostEqual(stats['min'], 1)
        self.assertAlmostEqual(stats['max'], 10)
        self.assertAlmostEqual(stats['range'], 9)
    
    def test_linear_regression_perfect_correlation(self):
        """Test linear regression with perfect correlation."""
        x_data = [1, 2, 3, 4, 5]
        y_data = [2, 4, 6, 8, 10]  # y = 2x
        
        slope, intercept, r_squared = self.analyzer.linear_regression(x_data, y_data)
        
        self.assertAlmostEqual(slope, 2.0, places=2)
        self.assertAlmostEqual(intercept, 0.0, places=2)
        self.assertAlmostEqual(r_squared, 1.0, places=4)
    
    def test_linear_regression_with_intercept(self):
        """Test linear regression with non-zero intercept."""
        x_data = [1, 2, 3, 4, 5]
        y_data = [3, 5, 7, 9, 11]  # y = 2x + 1
        
        slope, intercept, r_squared = self.analyzer.linear_regression(x_data, y_data)
        
        self.assertAlmostEqual(slope, 2.0, places=2)
        self.assertAlmostEqual(intercept, 1.0, places=2)
        self.assertAlmostEqual(r_squared, 1.0, places=4)
    
    def test_empty_data(self):
        """Test behavior with empty data."""
        empty_analyzer = DataAnalyzer([])
        stats = empty_analyzer.summary_stats()
        
        self.assertEqual(stats, {})
    
    def test_single_data_point(self):
        """Test behavior with single data point."""
        single_analyzer = DataAnalyzer([5.0])
        stats = single_analyzer.summary_stats()
        
        self.assertEqual(stats['count'], 1)
        self.assertEqual(stats['mean'], 5.0)
        self.assertEqual(stats['median'], 5.0)
        self.assertEqual(stats['std_dev'], 0)
        self.assertEqual(stats['variance'], 0)
    
    def test_add_data(self):
        """Test adding data to existing analyzer."""
        analyzer = DataAnalyzer([1, 2, 3])
        analyzer.add_data([4, 5, 6])
        
        stats = analyzer.summary_stats()
        self.assertEqual(stats['count'], 6)
        self.assertAlmostEqual(stats['mean'], 3.5, places=2)
    
    def test_regression_error_cases(self):
        """Test linear regression error handling."""
        # Mismatched data lengths
        with self.assertRaises(ValueError):
            self.analyzer.linear_regression([1, 2], [1])
        
        # Insufficient data points
        with self.assertRaises(ValueError):
            self.analyzer.linear_regression([1], [1])
        
        # Identical X values
        with self.assertRaises(ValueError):
            self.analyzer.linear_regression([1, 1, 1], [1, 2, 3])

class TestSampleDataGeneration(unittest.TestCase):
    """Test cases for sample data generation."""
    
    def test_generate_sample_data(self):
        """Test sample data generation."""
        x_data, y_data = generate_sample_data(10)
        
        self.assertEqual(len(x_data), 10)
        self.assertEqual(len(y_data), 10)
        
        # Data should be numeric
        for x, y in zip(x_data, y_data):
            self.assertIsInstance(x, (int, float))
            self.assertIsInstance(y, (int, float))

def main():
    """Run all tests."""
    unittest.main()

if __name__ == "__main__":
    main()