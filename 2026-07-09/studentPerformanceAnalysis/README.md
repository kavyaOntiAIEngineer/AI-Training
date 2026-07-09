# Student Performance Analysis using Python

##  Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) on the Student Performance dataset collected from Kaggle.

The main objective of this project is to analyze different factors that influence student academic performance and understand the relationship between student background information and exam scores.

The complete analysis includes data preprocessing, displaying data in tabular format, visualization, and extracting meaningful insights.

---

##  Dataset Information

The dataset contains student information and their exam performance in three subjects.

### Features:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- VS Code Jupyter Cells
- Git
- GitHub

---

##  Libraries Used

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

---

# Project Workflow

## 1. Data Loading

The dataset was loaded using Pandas.

```python
pd.read_csv()
```

The first few records were displayed in tabular format using:

```python
df.head()
```

---

# 2. Data Understanding

Performed initial exploration:

- Checked dataset dimensions
- Viewed column information
- Checked data types
- Generated statistical summary


Methods used:

```python
df.shape

df.info()

df.describe()
```

---

# 3. Data Preprocessing

Data cleaning steps performed:

- Checked missing values
- Removed duplicate records
- Renamed columns for better readability
- Verified data types
- Created new calculated features


### Feature Engineering

A new feature was created:

**Average Score**

Using:

Math Score + Reading Score + Writing Score


This helped analyze overall student performance.

---

# 4. Tabular Data Representation

Before every visualization, related data was displayed in table format.

Example:

Gender Performance Table

| Gender | Average Score |
|---|---|
| Female | Score value |
| Male | Score value |


Purpose:

- Understand actual data values
- Compare features easily
- Support visualization results

---

# Exploratory Data Analysis (EDA)

EDA was divided into three parts:

1. Univariate Analysis
2. Bivariate Analysis
3. Multivariate Analysis


---

# 1. Univariate Analysis

Analyzing a single variable independently.

## Visualizations:

### Gender Distribution

Purpose:

To analyze the number of male and female students.

Graph Used:

- Count Plot


### Math Score Distribution

Purpose:

To understand how mathematics scores are distributed among students.

Graph Used:

- Histogram


### Reading Score Distribution

Purpose:

To analyze student reading performance.

Graph Used:

- Histogram


### Parent Education Distribution

Purpose:

To understand students' family educational background.

Graph Used:

- Count Plot


---

# 2. Bivariate Analysis

Analyzing relationships between two variables.


## Gender vs Average Score

Purpose:

To compare performance differences between male and female students.

Graph Used:

- Bar Plot


## Test Preparation vs Performance

Purpose:

To check whether completing preparation courses improves scores.

Graph Used:

- Box Plot


## Lunch Type vs Performance

Purpose:

To analyze the effect of lunch type on student scores.

Graph Used:

- Bar Plot


## Math Score vs Reading Score

Purpose:

To identify relationships between subject performances.

Graph Used:

- Scatter Plot


---

# 3. Multivariate Analysis

Analyzing multiple variables together.


## Correlation Analysis

Purpose:

To identify relationships among numerical features.

Graph Used:

- Heatmap


## Score Relationship Analysis

Purpose:

To compare math, reading, writing, and average scores together.

Graph Used:

- Pair Plot


## Gender + Test Preparation + Score Analysis

Purpose:

To analyze the combined effect of gender and preparation on performance.

Graph Used:

- Grouped Bar Plot


---

# Key Insights

- Students who completed test preparation scored higher on average.

- Reading score and writing score showed strong correlation.

- Academic performance varies based on multiple factors.

- Feature relationships were identified using visualization techniques.

- Data visualization helped understand student performance patterns.


---

# Conclusion

This project demonstrates how Exploratory Data Analysis can be used to understand student performance trends.

Using preprocessing, tabular analysis, and visualization techniques, important factors affecting academic results were identified.