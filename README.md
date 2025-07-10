# Predictive-Analysis

📊 Cardiovascular Health Data Exploration and Preprocessing

This project performs an in-depth exploratory data analysis (EDA) and preprocessing of a cardiovascular health dataset to understand variable distributions, relationships, and prepare data transformations suitable for further modeling or statistical analysis.

📝 Key Objectives
	•	Clean and preprocess raw health data.
	•	Generate descriptive statistics and visualizations to summarize distributions and detect outliers.
	•	Explore multivariate correlations and patterns.
	•	Apply data transformation techniques, including binning, normalization, and discretization.

⸻

🛠️ Data Processing and Analysis Steps

1. Data Cleaning
	•	Converted age from days to years (age_years).
	•	Binarized categorical Yes/No columns (smoke, alco, active, cardio) to numerical values (1/0).

⸻

2. Descriptive Statistics and Visualization
	•	Summary Statistics:
	•	Computed count, mean, standard deviation, quartiles, and range for continuous variables:
	•	age_years, height, weight, ap_hi, ap_lo
	•	Exported statistics to Excel for documentation.
	•	Univariate Visualizations:
	•	Histograms and Kernel Density Estimates (KDE) for continuous variables.
	•	Boxplots to visualize distributions and identify outliers.
	•	Bar charts for categorical variable frequencies:
	•	gender, cholesterol, gluc, smoke, alco, active, cardio

⸻

3. Multivariate Analysis
	•	Correlation Analysis:
	•	Computed Pearson correlation matrix across numeric and binary attributes.
	•	Generated a heatmap to highlight relationships (e.g., age vs. blood pressure, weight vs. cholesterol).
	•	Pairwise Relationships:
	•	Developed a pairplot (scatterplot matrix) stratified by the cardio outcome variable to explore clustering and separation patterns.

⸻

4. Feature Engineering and Transformation
	•	Height Binning:
	•	Created two types of height bins:
	•	Equal-width binning (5 intervals of fixed range)
	•	Equal-depth (quantile) binning (5 bins with balanced record counts)
	•	Weight Normalization:
	•	Applied:
	•	Min-Max Scaling (range 0–1)
	•	Z-score Standardization (mean 0, variance 1)
	•	Age Discretization:
	•	Classified age into 5 life stages:
	•	Young
	•	Early Adulthood
	•	Early Middle Age
	•	Late Middle Age
	•	Late Adulthood
	•	Tabulated and exported frequency counts per age group.
	•	Smoke Binarization:
	•	Verified correct encoding of smoking status into binary format.

⸻

💾 Outputs

All processed data, summaries, and transformation results are saved as:
	•	Individual Excel sheets (fda_a2_25528908.xlsx)
	•	Visual plots (.png files) for histograms, boxplots, bar charts, heatmaps, and pairplots.

⸻

🔧 Technologies and Libraries
	•	Python 3
	•	Pandas: data manipulation and cleaning
	•	Seaborn & Matplotlib: visualization
	•	Scikit-learn: normalization and scaling
	•	OpenPyXL: Excel export

⸻

✅ Usage

This workflow serves as a template for:
	•	Preliminary EDA of health-related datasets.
	•	Preprocessing pipelines before machine learning.
	•	Reporting and visualization of demographic and clinical indicators.
