import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


try:
    df = pd.read_csv("data.csv", sep=",", on_bad_lines='skip', engine='python')
    print("Dataset loaded successfully.")
except Exception as e:
    print(" Error loading dataset:", e)
    exit()


print("\nFirst few rows of the dataset:")
print(df.head())

plt.figure(figsize=(10, 5))


if 'Age_Group' in df.columns and 'Population' in df.columns:
    sns.barplot(x='Age_Group', y='Population', data=df, palette='viridis')
    plt.title("Population Distribution by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Population")
elif 'Gender' in df.columns and 'Count' in df.columns:
    sns.barplot(x='Gender', y='Count', data=df, palette='pastel')
    plt.title("Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("Count")
elif 'Age' in df.columns:
    sns.histplot(df['Age'], bins=10, kde=True, color='skyblue')
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
else:
    print("\n Dataset does not contain expected columns like 'Age_Group', 'Population', 'Gender', 'Count', or 'Age'.")
    print("Please check your CSV column names.")
    exit()

plt.grid(axis='y')
plt.tight_layout()
plt.show()
