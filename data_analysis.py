#!/usr/bin/env python3
"""
Data Analysis Program - R-style data analysis in Python
This program demonstrates data analysis capabilities similar to R.
"""

import math
import statistics
import random
from typing import List, Dict, Tuple

class DataAnalyzer:
    """A class for performing statistical analysis on data."""
    
    def __init__(self, data: List[float] = None):
        """Initialize the analyzer with optional data."""
        self.data = data or []
    
    def add_data(self, values: List[float]) -> None:
        """Add data points to the analyzer."""
        self.data.extend(values)
    
    def summary_stats(self) -> Dict[str, float]:
        """Calculate summary statistics for the data."""
        if not self.data:
            return {}
        
        return {
            'count': len(self.data),
            'mean': statistics.mean(self.data),
            'median': statistics.median(self.data),
            'mode': statistics.mode(self.data) if len(set(self.data)) < len(self.data) else None,
            'std_dev': statistics.stdev(self.data) if len(self.data) > 1 else 0,
            'variance': statistics.variance(self.data) if len(self.data) > 1 else 0,
            'min': min(self.data),
            'max': max(self.data),
            'range': max(self.data) - min(self.data)
        }
    
    def linear_regression(self, x_data: List[float], y_data: List[float]) -> Tuple[float, float, float]:
        """Perform simple linear regression and return slope, intercept, and R-squared."""
        if len(x_data) != len(y_data) or len(x_data) < 2:
            raise ValueError("X and Y data must have the same length and at least 2 points")
        
        n = len(x_data)
        x_mean = statistics.mean(x_data)
        y_mean = statistics.mean(y_data)
        
        # Calculate slope and intercept
        numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_data, y_data))
        denominator = sum((x - x_mean) ** 2 for x in x_data)
        
        if denominator == 0:
            raise ValueError("Cannot perform regression: all X values are identical")
        
        slope = numerator / denominator
        intercept = y_mean - slope * x_mean
        
        # Calculate R-squared
        y_pred = [slope * x + intercept for x in x_data]
        ss_res = sum((y - y_p) ** 2 for y, y_p in zip(y_data, y_pred))
        ss_tot = sum((y - y_mean) ** 2 for y in y_data)
        
        r_squared = 1 - (ss_res / ss_tot) if ss_tot != 0 else 1
        
        return slope, intercept, r_squared

def generate_sample_data(n: int = 50) -> Tuple[List[float], List[float]]:
    """Generate sample data for demonstration."""
    random.seed(42)  # For reproducible results
    x_data = [i + random.uniform(-0.5, 0.5) for i in range(n)]
    y_data = [2 * x + 1 + random.uniform(-2, 2) for x in x_data]
    return x_data, y_data

def main():
    """Main function to demonstrate the data analysis capabilities."""
    print("=== R-Style Data Analysis Program ===\n")
    
    # Generate sample data
    print("1. Generating sample data...")
    x_data, y_data = generate_sample_data(30)
    combined_data = x_data + y_data
    
    # Initialize analyzer
    analyzer = DataAnalyzer(combined_data)
    
    # Calculate summary statistics
    print("\n2. Summary Statistics:")
    stats = analyzer.summary_stats()
    for key, value in stats.items():
        if value is not None:
            if isinstance(value, float):
                print(f"   {key.capitalize()}: {value:.4f}")
            else:
                print(f"   {key.capitalize()}: {value}")
    
    # Perform linear regression
    print("\n3. Linear Regression Analysis:")
    try:
        slope, intercept, r_squared = analyzer.linear_regression(x_data, y_data)
        print(f"   Equation: y = {slope:.4f}x + {intercept:.4f}")
        print(f"   R-squared: {r_squared:.4f}")
        print(f"   Correlation strength: {'Strong' if r_squared > 0.7 else 'Moderate' if r_squared > 0.3 else 'Weak'}")
    except ValueError as e:
        print(f"   Error: {e}")
    
    # Additional analysis
    print("\n4. Data Distribution Analysis:")
    quartiles = [sorted(combined_data)[int(len(combined_data) * q)] for q in [0.25, 0.5, 0.75]]
    print(f"   Q1 (25th percentile): {quartiles[0]:.4f}")
    print(f"   Q2 (50th percentile): {quartiles[1]:.4f}")
    print(f"   Q3 (75th percentile): {quartiles[2]:.4f}")
    print(f"   IQR (Interquartile Range): {quartiles[2] - quartiles[0]:.4f}")
    
    print("\n=== Analysis Complete ===")
    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("\n✅ Program executed successfully!")
    else:
        print("\n❌ Program encountered errors.")