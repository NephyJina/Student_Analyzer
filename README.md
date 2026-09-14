# Student Grade & Attendance Analyzer

A Python and Pandas tool that cleans raw student data, calculates performance metrics, flags at-risk students, and generates visual reports.

## Features
- Data cleaning (duplicates, missing values, formatting fixes)
- Automatic Pass/Fail status and class ranking
- At-risk student detection (low marks + low attendance)
- Visualizations: grade distribution and attendance-vs-marks scatter plot

## Tech Stack
Python, Pandas, Matplotlib, Seaborn

## Project Structure

Student_Analyzer/
│

├── code.py # Main script

├── data.csv # Raw input data

├── cleaned_student_marks.csv # Cleaned dataset (output)

├── summary.csv # Final summary report (output)

├── Total Marks of Students.png # Grade distribution chart

├── Total by Attendance_Pct.png # Attendance vs marks chart

└── README.md

## Sample Output
![Grade Distribution](Total%20Marks%20of%20Students.png)
![Attendance vs Marks](Total%20by%20Attendance_Pct.png)

## How to Run
1. Clone the repo
2. `pip install pandas matplotlib seaborn`
3. Run `python code.py`

## What I Learned

Building this project helped me practice real pandas workflows — data cleaning with `fillna`, `clip`, and `to_numeric`, row-wise logic with `apply(axis=1)`, aggregation with `groupby`, and merging tables to build a clean summary report.

## Author

**Nephy**  
Final-year IT student | Learning Python & Data Analysis  
[LinkedIn](https://www.linkedin.com/in/nephy-jina-dev)
