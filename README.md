IT Employees Performance Dashboard
An end-to-end data analytics project: raw IT employee data → cleaning in Python → analysis with SQL (MySQL) → interactive 4-page dashboard in Power BI.
Objective
To understand workforce size, salary structure, attendance, ratings and productivity of IT employees across 5 departments (Development, DevOps, Data, QA, Support) and to give HR-focused recommendations.
Tools Used
Stage	Tool
Data cleaning	Python (pandas)
Data analysis	MySQL Workbench (16 SQL queries)
Visualization	Power BI Desktop (DAX measures, calculated columns)
Documentation	Word insight document
Dataset
`IT_employee_dataset.csv` – raw data
`it_employees_data_cleaned.csv` – cleaned data (966 employees)
Main columns: Employee_ID, Department, Experience_Years, Projects_Completed, Hours_Worked_Per_Week, Attendance_Percent, Performance_Rating, Productivity_Score, Monthly_Salary.
Data Cleaning (`data.py`)
Removed duplicate Employee_IDs
Filled missing numeric values with the median
Fixed data types (int / rounded decimals)
Productivity_Score outliers (values outside 0–100, max was 121297) replaced with the median
Removed 5 rows with invalid Performance_Rating (not 1–5) or Attendance_Percent (not 0–100)
Dashboard Pages
1. Employee Overview
![Employee Overview](screenshots_project/page1_overview.png)
2. Salary Analysis
![Salary Analysis](screenshots_project/page2_salary.png)
3. Attendance & Rating
![Attendance and Rating](screenshots_project/page3_rating.png)
4. Work Productivity
![Work Productivity](screenshots_project/page4_productivity.png)
Key Insights
966 employees, average salary 87.19K; departments are evenly spread (19%–21% each).
Support has the highest average salary (91K); Data (84K) and Development (85K) are the lowest.
281 employees (about 29%) have attendance below 80%.
8 employees have perfect attendance but a rating of 2 or below, which points to a skill or role-fit issue.
DevOps has the lowest average rating (2.91) and the most employees working above 55 hours (38), so burnout risk is highest there.
Average productivity score is 70.27 / 100; 161 employees work more than 55 hours a week.
Salary does not grow steadily with experience, so a clear increment policy is recommended.
Full details are in the insight document: `INSIGHT_DOCUMENT_Employee_Performance.docx`.
Features
Department slicer on every page
Left sidebar page navigation
Top 5 / Bottom 5 salary tables, salary rank by department (RANKX)
Salary band distribution, attendance vs rating analysis, hours > 55 analysis
Repository Structure
```
├── data.py                                  # Python cleaning script
├── IT_employee_dataset.csv                  # raw data
├── it_employees_data_cleaned.csv            # cleaned data
├── IT_Employees_Performance_Analysis.pbix   # Power BI file
├── INSIGHT_DOCUMENT_Employee_Performance.docx
├── sql_queries.sql                          # 16 SQL queries
└── screenshots_project/                     # dashboard screenshots
```
How to Open
Download `IT_Employees_Performance_Analysis.pbix`
Open it in Power BI Desktop (free)
Author
<Your Name> – BE Computer Science and Engineering graduate, Data Analytics (fresher)
LinkedIn: <your LinkedIn link>
