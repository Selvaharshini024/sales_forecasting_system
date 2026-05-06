import pandas as pd

def load_data(path):
    df = pd.read_excel(path)   # keep excel if you fixed file

    print("Columns:", df.columns)

    # ✅ Rename columns correctly
    df = df.rename(columns={
        'State': 'state',
        'Date': 'date',
        'Total': 'sales'
    })

    # ✅ Convert date
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # ✅ Remove invalid dates
    df = df.dropna(subset=['date'])

    # ✅ Sort
    df = df.sort_values(['state', 'date'])

    return df
def fill_missing_dates(df):
    def fill(group):
        group = group.set_index('date').asfreq('D')
        group['sales'] = group['sales'].fillna(method='ffill')
        return group.reset_index()
    
    return df.groupby('state').apply(fill).reset_index(drop=True)