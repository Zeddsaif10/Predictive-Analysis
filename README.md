📊 Cardiovascular Health Data Analysis and Preprocessing

This project presents a complete workflow for exploratory data analysis (EDA), feature engineering, and data preprocessing on a cardiovascular health dataset. The pipeline includes cleaning, descriptive statistics, visualization, discretization, normalization, and export of results for reporting and downstream modeling.

⸻

🎯 Objectives
	•	Clean and transform raw data into an analysis-ready format.
	•	Summarize and visualize key distributions and relationships.
	•	Engineer new features through discretization and normalization.
	•	Generate clear reports and visual artifacts to support interpretation.

⸻

🟢 Workflow Overview

1️⃣ Data Import and Preparation
	•	Loaded the dataset (CSV) into a pandas DataFrame.
	•	Converted age from days to integer years (age_years).
	•	Recoded binary categorical features (smoke, alco, active, cardio) to 0/1 indicators.

⸻

2️⃣ Descriptive Statistics & Univariate Analysis
	•	Computed summary statistics (mean, standard deviation, quartiles) for continuous variables and saved to Excel.
	•	Generated and exported:
	•	Histograms with KDE curves to illustrate distributions.
	•	Boxplots to identify outliers.
	•	Bar charts to show category frequencies for categorical variables.

⸻

3️⃣ Multivariate Exploration
	•	Calculated a correlation matrix and visualized it with a heatmap to assess linear relationships.
	•	Created a pairplot to explore variable interactions and potential clusters by the cardio target.

⸻

4️⃣ Feature Engineering
	•	Height Binning:
	•	Equi-width binning: Divided height into 5 intervals of equal range.
	•	Equi-depth binning: Created 5 quantile-based bins.
	•	Results saved to Excel for comparison.
	•	Weight Normalization:
	•	Min-Max scaling: Rescaled weight to the [0, 1] range.
	•	Z-score standardization: Standardized weight to have mean 0 and unit variance.
	•	Normalized data exported to Excel.
	•	Age Discretization:
	•	Grouped age_years into 5 meaningful age categories:
	•	Young
	•	Early Adulthood
	•	Early Middle Age
	•	Late Middle Age
	•	Late Adulthood
	•	Computed and saved frequency counts of each group.
	•	Smoke Binarization:
	•	Verified and exported binary encoding of smoking status.

⸻

📂 Generated Outputs
	•	Excel Reports:
	•	1A_summary_stats.xlsx: Descriptive statistics of continuous features.
	•	fda_a2_25528908.xlsx: Contains:
	•	Height binning results (equi-width and equi-depth)
	•	Weight normalization outputs
	•	Age discretization and frequency table
	•	Smoke binarization results
	•	Visualizations (PNG):
	•	Histograms of continuous variables
	•	Boxplots highlighting outliers
	•	Bar charts of categorical distributions
	•	Correlation heatmap
	•	Pairplot of selected variables colored by cardio status

⸻

🛠 Technologies Used
	•	Python 3
	•	pandas
	•	NumPy
	•	Matplotlib
	•	Seaborn
	•	scikit-learn
	•	openpyxl

⸻
 
⚙️ Reproducibility

To reproduce the analysis:
	1.	Install dependencies:
      pip install pandas numpy matplotlib seaborn scikit-learn openpyxl

  2.	Place the CSV dataset in your working directory.
	3.	Run the script to automatically generate all outputs.

⸻

💡 Next Steps
	•	Build predictive models for cardiovascular disease risk.
	•	Apply advanced feature selection and dimensionality reduction.
	•	Explore additional data cleaning and imputation strategies.


