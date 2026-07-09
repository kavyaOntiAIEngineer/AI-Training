# World Happiness Report Analysis using Python

## 📌 Project Overview

This project performs Exploratory Data Analysis on the World Happiness Report dataset from Kaggle.

The objective is to analyze different economic and social factors affecting happiness levels across countries.

The project includes data preprocessing, tabular representation, visualization, and extracting insights.

---

# Dataset Information

The dataset contains happiness-related information of different countries.

Features:

- Overall Rank
- Country or Region
- Happiness Score
- GDP Per Capita
- Social Support
- Healthy Life Expectancy
- Freedom to Make Life Choices
- Generosity
- Perceptions of Corruption

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- VS Code Jupyter Cells
- Git
- GitHub

---

# Libraries Used

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

---

# Project Workflow


## 1. Data Loading

Loaded the dataset using:

```python
pd.read_csv()
```

Displayed dataset in tabular format:

```python
df.head()
```

---

# 2. Data Understanding

Performed:

- Dataset shape analysis
- Column information checking
- Statistical analysis


Functions:

```python
df.shape

df.info()

df.describe()
```

---

# 3. Data Preprocessing

Steps performed:

- Cleaned column names
- Checked missing values
- Removed duplicate records
- Verified data types
- Prepared data for analysis


---

# 4. Tabular Data Representation

Before each visualization, selected features were displayed as tables.


Example:

GDP and Happiness Table

| Country | GDP Per Capita | Happiness Score |
|-|-|-|
|Country Name|GDP Value|Score Value|


Benefits:

- Easy comparison
- Better understanding
- Supports graphical insights

---

# Exploratory Data Analysis

The analysis is divided into:

- Univariate Analysis
- Bivariate Analysis
- Multivariate Analysis


---

# 1. Univariate Analysis

Studying individual features.


## Happiness Score Distribution

Purpose:

To analyze happiness score distribution among countries.

Graph Used:

- Histogram


## GDP Distribution

Purpose:

To understand economic differences among countries.

Graph Used:

- Histogram


## Top Happiest Countries

Purpose:

To identify countries with highest happiness scores.

Graph Used:

- Bar Plot


---

# 2. Bivariate Analysis

Analyzing two variables together.


## GDP vs Happiness Score

Purpose:

To understand how economic strength affects happiness.

Graph Used:

- Scatter Plot


## Healthy Life Expectancy vs Happiness

Purpose:

To analyze the relationship between health and happiness.

Graph Used:

- Scatter Plot


## Freedom vs Happiness

Purpose:

To understand the impact of freedom on happiness.

Graph Used:

- Regression Plot


---

# 3. Multivariate Analysis


## Correlation Analysis

Purpose:

To find relationships between all numerical factors.

Graph Used:

- Heatmap


## Multiple Feature Comparison

Features analyzed:

- Happiness Score
- GDP
- Social Support
- Health
- Freedom


Graph Used:

- Pair Plot


## GDP + Health + Happiness Analysis

Purpose:

To understand combined effects of economic and health factors.

Graph Used:

- Multivariate Scatter Plot


---

# Key Insights

- Countries with higher GDP generally have higher happiness scores.

- Healthy life expectancy positively impacts happiness.

- Social support contributes strongly to happiness.

- Freedom to make life choices improves happiness levels.

- Happiness depends on multiple economic and social factors.


---

# Conclusion

This project demonstrates the use of Exploratory Data Analysis to study global happiness patterns.

Through preprocessing, tabular representation, and visualization, important factors influencing happiness across countries were identified.