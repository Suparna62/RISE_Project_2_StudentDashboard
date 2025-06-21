import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('student_data.csv')

# Summary
print("\n=== Basic Stats ===")
print(df.describe())

# Correlation heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df[['Marks', 'Attendance(%)', 'Logins']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig('output.png')  # Save heatmap
plt.show()

# Top performers
top_students = df[df['Marks'] >= 75]
print("\nTop Performing Students:\n", top_students[['Name', 'Marks']])

# Struggling students
low_students = df[df['Marks'] < 50]
print("\nStruggling Students:\n", low_students[['Name', 'Marks']])

# Bar chart: Marks
plt.figure(figsize=(8,4))
plt.bar(df['Name'], df['Marks'], color='skyblue')
plt.title('Student Marks Comparison')
plt.ylabel('Marks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('marks_bar.png')  # Save bar chart
plt.show()
