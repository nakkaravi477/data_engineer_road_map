import pandas as pd

people = pd.read_csv('sample_data.csv')
depts = pd.read_csv('departments.csv')

# Merge on name (inner by default: only matching names will be included)
merged = pd.merge(people, depts, on='name')
print(merged)

# Left join: keep all people, add department info if present
merged_left = pd.merge(people, depts, on='name', how='left')
print(merged_left)

# Pivot: mean salary by department and gender
pivot = merged.pivot_table(
    index='department',
    columns='gender',
    values='salary',
    aggfunc='mean'
)
print(pivot)

data = {
    'name': ['Alice', 'Bob', 'Carol'],
    'hire_date': ['2020-03-10', '2019-07-22', '2021-02-18']
}
df = pd.DataFrame(data)
df['hire_date'] = pd.to_datetime(df['hire_date'])

# Extract features
df['year'] = df['hire_date'].dt.year
df['month'] = df['hire_date'].dt.month
df['day_of_week'] = df['hire_date'].dt.day_name()
print(df)
