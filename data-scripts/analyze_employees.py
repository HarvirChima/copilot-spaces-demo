"""
Data Analysis Script for Employee Data
Processes employee JSON data and generates insights
"""

import json
from collections import defaultdict
from datetime import datetime

def load_employee_data(filename='employees.json'):
    """Load employee data from JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)

def calculate_department_stats(employees):
    """Calculate statistics by department"""
    dept_stats = defaultdict(lambda: {
        'count': 0,
        'total_salary': 0,
        'avg_rating': 0,
        'employees': []
    })
    
    for emp in employees:
        dept = emp['department']
        dept_stats[dept]['count'] += 1
        dept_stats[dept]['total_salary'] += emp['salary']
        dept_stats[dept]['avg_rating'] += emp['performance_rating']
        dept_stats[dept]['employees'].append(emp['name'])
    
    # Calculate averages
    for dept in dept_stats:
        count = dept_stats[dept]['count']
        dept_stats[dept]['avg_salary'] = dept_stats[dept]['total_salary'] / count
        dept_stats[dept]['avg_rating'] = dept_stats[dept]['avg_rating'] / count
    
    return dict(dept_stats)

def find_top_performers(employees, n=3):
    """Find top N performers by rating"""
    sorted_employees = sorted(employees, key=lambda x: x['performance_rating'], reverse=True)
    return sorted_employees[:n]

def calculate_tenure(hire_date):
    """Calculate years of tenure"""
    hire = datetime.strptime(hire_date, '%Y-%m-%d')
    today = datetime.now()
    return (today - hire).days / 365.25

def analyze_tenure(employees):
    """Analyze employee tenure"""
    tenure_data = []
    for emp in employees:
        years = calculate_tenure(emp['hire_date'])
        tenure_data.append({
            'name': emp['name'],
            'years': round(years, 1),
            'department': emp['department']
        })
    
    return sorted(tenure_data, key=lambda x: x['years'], reverse=True)

def generate_report(employees):
    """Generate comprehensive employee report"""
    print("="*60)
    print("EMPLOYEE DATA ANALYSIS REPORT")
    print("="*60)
    print(f"\nTotal Employees: {len(employees)}")
    
    # Department Statistics
    print("\n--- Department Statistics ---")
    dept_stats = calculate_department_stats(employees)
    for dept, stats in dept_stats.items():
        print(f"\n{dept}:")
        print(f"  Employees: {stats['count']}")
        print(f"  Average Salary: ${stats['avg_salary']:,.2f}")
        print(f"  Average Rating: {stats['avg_rating']:.2f}")
    
    # Top Performers
    print("\n--- Top Performers ---")
    top_performers = find_top_performers(employees)
    for i, emp in enumerate(top_performers, 1):
        print(f"{i}. {emp['name']} - Rating: {emp['performance_rating']} ({emp['department']})")
    
    # Tenure Analysis
    print("\n--- Longest Tenure ---")
    tenure_analysis = analyze_tenure(employees)
    for i, emp in enumerate(tenure_analysis[:5], 1):
        print(f"{i}. {emp['name']} - {emp['years']} years ({emp['department']})")
    
    # Salary Statistics
    salaries = [emp['salary'] for emp in employees]
    print(f"\n--- Salary Statistics ---")
    print(f"Minimum Salary: ${min(salaries):,}")
    print(f"Maximum Salary: ${max(salaries):,}")
    print(f"Average Salary: ${sum(salaries)/len(salaries):,.2f}")
    
    print("\n" + "="*60)

if __name__ == '__main__':
    employees = load_employee_data()
    generate_report(employees)
