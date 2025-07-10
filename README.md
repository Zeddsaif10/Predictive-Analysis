# 📊 Cardiovascular Health Data Exploration and Preprocessing

This project performs an in-depth exploratory data analysis (EDA) and preprocessing of a cardiovascular health dataset to understand variable distributions, relationships, and prepare data transformations suitable for further modeling or statistical analysis.

---

## 📝 Key Objectives

- Clean and preprocess raw health data.
- Generate descriptive statistics and visualizations to summarize distributions and detect outliers.
- Explore multivariate correlations and patterns.
- Apply data transformation techniques, including binning, normalization, and discretization.

---

## 🛠️ Data Processing and Analysis Steps

### 1️⃣ Data Cleaning
- Converted **age** from days to years (`age_years`).
- Binarized categorical `Yes/No` columns (`smoke`, `alco`, `active`, `cardio`) to numeric format (1 = Yes, 0 = No).

### 2️⃣ Descriptive Statistics and Visualization
- **Summary Statistics:**
  - Computed count, mean, standard deviation, quartiles, and ranges for continuous variables.
  - Exported results to Excel (`1A_summary_stats.xlsx`).
- **Univariate Visualizations:**
  - Histograms with KDE overlays for distributions.
  - Boxplots for identifying outliers.
  - Bar charts to display frequencies of categorical variables.

### 3️⃣ Multivariate Analysis
- **Correlation Matrix:**
  - Pearson correlations among numeric and binary variables.
  - Heatmap visualization.
- **Pairwise Relationships:**
  - Pairplot stratified by `cardio` outcome to observe clusters and potential predictors.

### 4️⃣ Feature Engineering and Transformation
- **Height Binning:**
  - Equal-width and equal-depth binning into 5 groups.
- **Weight Normalization:**
  - Min-Max scaling (0–1 range).
  - Z-score standardization (mean 0, SD 1).
- **Age Discretization:**
  - Categorized into 5 life stages:
    - Young
    - Early Adulthood
    - Early Middle Age
    - Late Middle Age
    - Late Adulthood
- **Smoke Binarization:**
  - Validated binary encoding.

---

## 💾 Outputs

The following files are generated:

| File | Description |
| --- | --- |
| `1A_summary_stats.xlsx` | Summary statistics for continuous variables |
| `fda_a2_25528908.xlsx` | All transformed datasets (binning, normalization, discretization) |
| `.png` images | Histograms, boxplots, bar charts, heatmaps, and pairplots |

---

## ⚙️ Installation

Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
