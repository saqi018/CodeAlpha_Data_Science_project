# CodeAlpha Data Science Internship

This repository contains the projects completed during the CodeAlpha Data Science Internship. The tasks focus on applied machine learning classification and data pipeline processing for visualization.

## Task 1: Iris Flower Classification
**Status:** Completed (Compulsory Task)

### Objective
To train a machine learning model to classify Iris flower species (setosa, versicolor, virginica) based on their physical measurements (sepal and petal length/width).

### Approach & Results
* **Tools Used:** Python, Scikit-learn, Pandas.
* **Model:** Random Forest Classifier.
* **Process:** The built-in Iris dataset was loaded and split into an 80/20 training and testing set. The Random Forest model was trained on the 80% split.
* **Accuracy:** The model achieved **100.00% accuracy** on the test data, successfully predicting the correct species with zero false positives or negatives across all target classes.

---

## Task 2: Unemployment Analysis with Python
**Status:** Completed

### Objective
To analyze unemployment rate data in India, specifically investigating the impact of the COVID-19 pandemic and identifying regional trends.

### Approach & Results
As someone focused on building robust data engineering pipelines, I approached this task using an ETL (Extract, Transform, Load) methodology:
* **Tools Used:** Python, Pandas, Matplotlib, Seaborn.
* **Extract:** Loaded raw CSV data containing regional unemployment statistics.
* **Transform:** Cleaned the data by stripping hidden whitespace from column headers, dropping null values, and parsing raw date strings into standard Python datetime objects.
* **Load/Visualize:** Generated structured visualizations to highlight economic trends.
* **Insights:** The visualizations clearly demonstrate a massive, unprecedented spike in the average unemployment rate during the April/May 2020 COVID-19 lockdowns, followed by a gradual recovery period.

---
**Author:** Saqib Khan
