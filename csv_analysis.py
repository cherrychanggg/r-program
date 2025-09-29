#!/usr/bin/env python3
"""
CSV Data Analysis Script
Demonstrates loading and analyzing data from CSV files.
"""

import csv
from data_analysis import DataAnalyzer

def load_csv_data(filename: str) -> dict:
    """Load data from a CSV file."""
    data = {'x': [], 'y': [], 'category': []}
    
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data['x'].append(float(row['x']))
                data['y'].append(float(row['y']))
                data['category'].append(row['category'])
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def analyze_csv_data(filename: str = 'sample_data.csv'):
    """Analyze data from a CSV file."""
    print(f"=== CSV Data Analysis: {filename} ===\n")
    
    # Load data
    data = load_csv_data(filename)
    if not data:
        return False
    
    print(f"Loaded {len(data['x'])} data points from {filename}")
    
    # Analyze X values
    print("\n--- X Variable Analysis ---")
    x_analyzer = DataAnalyzer(data['x'])
    x_stats = x_analyzer.summary_stats()
    for key, value in x_stats.items():
        if value is not None and isinstance(value, (int, float)):
            print(f"   {key.capitalize()}: {value:.4f}")
    
    # Analyze Y values
    print("\n--- Y Variable Analysis ---")
    y_analyzer = DataAnalyzer(data['y'])
    y_stats = y_analyzer.summary_stats()
    for key, value in y_stats.items():
        if value is not None and isinstance(value, (int, float)):
            print(f"   {key.capitalize()}: {value:.4f}")
    
    # Perform regression analysis
    print("\n--- Regression Analysis (X vs Y) ---")
    try:
        slope, intercept, r_squared = x_analyzer.linear_regression(data['x'], data['y'])
        print(f"   Equation: y = {slope:.4f}x + {intercept:.4f}")
        print(f"   R-squared: {r_squared:.4f}")
        print(f"   Correlation: {'Strong' if r_squared > 0.7 else 'Moderate' if r_squared > 0.3 else 'Weak'}")
        
        # Predict some values
        print("\n--- Predictions ---")
        test_x_values = [5, 10, 15]
        for x_val in test_x_values:
            y_pred = slope * x_val + intercept
            print(f"   When x = {x_val}, predicted y = {y_pred:.2f}")
            
    except Exception as e:
        print(f"   Regression analysis failed: {e}")
    
    # Category analysis
    print("\n--- Category Analysis ---")
    categories = set(data['category'])
    for category in sorted(categories):
        cat_x = [x for x, cat in zip(data['x'], data['category']) if cat == category]
        cat_y = [y for y, cat in zip(data['y'], data['category']) if cat == category]
        
        print(f"   Category {category}:")
        print(f"     Count: {len(cat_x)}")
        if cat_x:
            print(f"     X mean: {sum(cat_x)/len(cat_x):.2f}")
            print(f"     Y mean: {sum(cat_y)/len(cat_y):.2f}")
    
    print("\n=== Analysis Complete ===")
    return True

if __name__ == "__main__":
    success = analyze_csv_data()
    if success:
        print("\n✅ CSV analysis completed successfully!")
    else:
        print("\n❌ CSV analysis encountered errors.")