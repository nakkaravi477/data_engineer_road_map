import pandas as pd # type: ignore

def load_and_explore():
    df = pd.read_csv("sample_data.csv")
    print("First 3 rows:\n", df.head(3))
    print("\nInfo:")
    print(df.info())
    print("\nMissing values per column:\n", df.isnull().sum())
    return df

def clean_and_transform(df):
    df['age'] = df['age'].fillna(df['age'].median())
    df['salary'] = df['salary'].fillna(df['salary'].median())

    bins = [0, 24, 34, 44, 150]
    labels = ['<25', '25-34', '35-44', '45+']
    df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

    print("\nCleaned DataFrame:\n", df)
    return df

def aggregation_examples(df):
    print("\nSalary stats by gender:")
    print(df.groupby('gender')['salary'].agg(['mean', 'min', 'max', 'count']))

    print("\nPeople with salary over 70,000:")
    print(df[df['salary'] > 70000][['name', 'salary']])

if __name__ == "__main__":
    df = load_and_explore()
    df = clean_and_transform(df)
    aggregation_examples(df)

