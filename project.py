import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("student_data.csv")

print("========== ORIGINAL DATASET ==========")
print(df)

# ----------------------------------
# 1. Check Missing Values
# ----------------------------------
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Fill Missing Values with Mean
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# ----------------------------------
# 2. Remove Duplicate Records
# ----------------------------------
duplicates = df.duplicated().sum()
print("\nNumber of Duplicate Rows:", duplicates)

df = df.drop_duplicates()

# ----------------------------------
# 3. Detect Outliers using IQR
# ----------------------------------
Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[(df["Age"] < lower_limit) |
              (df["Age"] > upper_limit)]

print("\n========== OUTLIERS ==========")
print(outliers)

# ----------------------------------
# 4. Summary Statistics
# ----------------------------------
print("\n========== SUMMARY ==========")
print(df.describe())

# ----------------------------------
# Visualization 1
# Marks Distribution
# ----------------------------------
plt.figure(figsize=(6,4))
plt.hist(df["Marks"], bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()

# ----------------------------------
# Visualization 2
# Gender-wise Average Marks
# ----------------------------------
gender_marks = df.groupby("Gender")["Marks"].mean()

plt.figure(figsize=(5,4))
gender_marks.plot(kind="bar")
plt.title("Gender-wise Average Marks")
plt.xlabel("Gender")
plt.ylabel("Average Marks")
plt.show()

# ----------------------------------
# Visualization 3
# Attendance vs Marks
# ----------------------------------
plt.figure(figsize=(6,4))
plt.scatter(df["Attendance"], df["Marks"])
plt.title("Attendance vs Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Marks")
plt.show()

# ----------------------------------
# Visualization 4
# Age Box Plot
# ----------------------------------
plt.figure(figsize=(5,4))
plt.boxplot(df["Age"])
plt.title("Age Distribution")
plt.ylabel("Age")
plt.show()

# ----------------------------------
# Final Cleaned Dataset
# ----------------------------------
print("\n========== CLEANED DATASET ==========")
print(df)

# Save Cleaned Dataset
df.to_csv("cleaned_student_data.csv", index=False)

print("\nCleaned dataset saved successfully!")
