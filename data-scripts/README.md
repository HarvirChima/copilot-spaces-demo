# Data Analysis Scripts

Python scripts for analyzing employee and product data.

## Files

- `employees.json` - Sample employee data
- `products.csv` - Sample product inventory data
- `analyze_employees.py` - Employee data analysis script
- `analyze_products.py` - Product inventory analysis script

## Usage

### Employee Analysis
```bash
python analyze_employees.py
```

This will generate:
- Department statistics (count, average salary, average rating)
- Top performers by rating
- Longest tenure employees
- Salary statistics

### Product Analysis
```bash
python analyze_products.py
```

This will generate:
- Category breakdown with inventory values
- Low stock alerts
- High value inventory items
- Overall inventory statistics

## Demo Ideas for Copilot Spaces

1. **Add Visualization**: "Create matplotlib charts to visualize the employee salary distribution"
2. **Export to Excel**: "Add functionality to export the analysis results to an Excel file"
3. **Add Filtering**: "Add command-line arguments to filter by department or date range"
4. **Performance Prediction**: "Add a function to predict future performance ratings based on tenure"
5. **Inventory Alerts**: "Create a system to send email alerts for low stock items"
6. **Add Unit Tests**: "Write comprehensive pytest tests for all analysis functions"
