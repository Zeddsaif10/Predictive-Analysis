#  IMPORTS 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# LOAD DATA 
df = pd.read_csv("32130_AT2_25528908.csv")

# BASIC CLEANING
df['age_years'] = (df['age'] / 365).astype(int)
yes_no_columns = ['smoke', 'alco', 'active', 'cardio']
for col in yes_no_columns:
    df[col] = df[col].map({'Yes': 1, 'No': 0})

# SUMMARY STATS & HISTOGRAMS 
continuous_cols = ['age_years', 'height', 'weight', 'ap_hi', 'ap_lo']
summary_stats = df[continuous_cols].describe(percentiles=[.25, .5, .75]).T
summary_stats.to_excel("1A_summary_stats.xlsx")

# Histograms 
for col in continuous_cols:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col], bins=30, kde=True)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig(f"{col}_hist.png")
    plt.close()

# Boxplots 
for col in continuous_cols:
    plt.figure(figsize=(4, 5))
    sns.boxplot(y=df[col])
    plt.title(f'Boxplot of {col}')
    plt.ylabel(col)
    plt.tight_layout()
    plt.savefig(f"{col}_box.png")
    plt.close()

# Bar charts 
categorical_cols = ['gender', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio']
for col in categorical_cols:
    plt.figure(figsize=(5, 4))
    sns.countplot(x=col, data=df)
    plt.title(f'Frequency of {col}')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(f"{col}_bar.png")
    plt.close()

# MULTIVARIATE EXPLORATION
numeric_cols = ['age_years', 'height', 'weight', 'ap_hi', 'ap_lo',
                'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio']

plt.figure(figsize=(10, 8))
correlation_matrix = df[numeric_cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()

pairplot_cols = ['age_years', 'weight', 'ap_hi', 'ap_lo', 'cardio']
sns.pairplot(df[pairplot_cols], hue='cardio', diag_kind='hist')
plt.savefig("pairplot_clusters.png")
plt.close()

# HEIGHT BINNING 
df['height_bin_equiwidth'] = pd.cut(df['height'], bins=5, labels=[1, 2, 3, 4, 5])
df['height_bin_eqdepth'] = pd.qcut(df['height'], q=5, labels=[1, 2, 3, 4, 5])

with pd.ExcelWriter("fda_a2_25528908.xlsx", engine='openpyxl', mode='w') as writer:
    df[['height', 'height_bin_equiwidth']].to_excel(writer, sheet_name='1B_Height_EquiWidth', index=False)
    df[['height', 'height_bin_eqdepth']].to_excel(writer, sheet_name='1B_Height_EquiDepth', index=False)

# WEIGHT NORMALIZATION 
minmax_scaler = MinMaxScaler()
df['weight_minmax'] = minmax_scaler.fit_transform(df[['weight']])

zscore_scaler = StandardScaler()
df['weight_zscore'] = zscore_scaler.fit_transform(df[['weight']])

with pd.ExcelWriter("fda_a2_25528908.xlsx", engine='openpyxl', mode='a') as writer:
    df[['weight', 'weight_minmax']].to_excel(writer, sheet_name='1B_Weight_MinMax', index=False)
    df[['weight', 'weight_zscore']].to_excel(writer, sheet_name='1B_Weight_Zscore', index=False)

# AGE DISCRETIZATION 
bins = [0, 21, 34, 44, 64, 200]
labels = ['Young', 'Early Adulthood', 'Early Middle Age', 'Late Middle Age', 'Late Adulthood']
df['age_group'] = pd.cut(df['age_years'], bins=bins, labels=labels)

age_group_freq = df['age_group'].value_counts().sort_index()
print(age_group_freq)

with pd.ExcelWriter("fda_a2_25528908.xlsx", engine='openpyxl', mode='a') as writer:
    df[['age_years', 'age_group']].to_excel(writer, sheet_name='1B_Age_Discretized', index=False)
    age_group_freq.to_frame(name='Frequency').to_excel(writer, sheet_name='1B_Age_Group_Frequency')

# SMOKE BINARIZATION 
print("Smoke values:", df['smoke'].unique())  

with pd.ExcelWriter("fda_a2_25528908.xlsx", engine='openpyxl', mode='a') as writer:
    df[['smoke']].to_excel(writer, sheet_name='1B_Smoke_Binarized', index=False)