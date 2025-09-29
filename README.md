# R-Program: Data Analysis Tool

A Python-based data analysis program that provides R-style statistical analysis capabilities.

## Features

- **Summary Statistics**: Calculate mean, median, mode, standard deviation, variance, and range
- **Linear Regression**: Perform simple linear regression with R-squared calculation
- **Data Distribution Analysis**: Quartile analysis and interquartile range
- **Sample Data Generation**: Built-in sample data for testing and demonstration
- **CSV Data Processing**: Load and analyze data from CSV files
- **Category Analysis**: Group and analyze data by categories

## Requirements

- Python 3.6 or higher
- No external dependencies (uses Python standard library only)

## Usage

### Basic Usage

```bash
# Run the main program with demonstration data
python3 data_analysis.py

# Analyze CSV data
python3 csv_analysis.py

# Run tests
python3 test_data_analysis.py
```

### Using as a Module

```python
from data_analysis import DataAnalyzer

# Create analyzer with your data
data = [1.5, 2.3, 3.1, 4.2, 5.0, 6.1, 7.3, 8.2, 9.1, 10.5]
analyzer = DataAnalyzer(data)

# Get summary statistics
stats = analyzer.summary_stats()
print(f"Mean: {stats['mean']:.2f}")
print(f"Standard Deviation: {stats['std_dev']:.2f}")

# Perform linear regression
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 6, 8, 10]
slope, intercept, r_squared = analyzer.linear_regression(x_data, y_data)
print(f"Regression equation: y = {slope:.2f}x + {intercept:.2f}")
```

## Sample Output

```
=== R-Style Data Analysis Program ===

1. Generating sample data...

2. Summary Statistics:
   Count: 60
   Mean: 15.2841
   Median: 15.1234
   Std_dev: 8.7456
   Variance: 76.4857
   Min: 0.1234
   Max: 30.9876
   Range: 30.8642

3. Linear Regression Analysis:
   Equation: y = 2.0123x + 1.0456
   R-squared: 0.8734
   Correlation strength: Strong

4. Data Distribution Analysis:
   Q1 (25th percentile): 7.8901
   Q2 (50th percentile): 15.1234
   Q3 (75th percentile): 22.5678
   IQR (Interquartile Range): 14.6777

=== Analysis Complete ===

✅ Program executed successfully!
```

## License

This project is open source and available under the MIT License.