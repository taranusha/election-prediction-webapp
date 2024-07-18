
import pandas as pd

data_path = "https://raw.githubusercontent.com/lauramauricio/election-prediction-webapp/efe5785ebf31c3bf48d528e9aa2b6ebc7fa46d29/merged_dataset.csv"
df = pd.read_csv(data_path)

# Replace "NaN" values with 0 for both numeric and categorical data
df_clean = df.fillna(0)

column_drop = ["year", "userid", "party", "total_gewahlt", "total_men", "total_women", "lr1", "pid2b", "sc7a", "weighttot", "trust1"]
df_clean = df_clean.drop(column_drop, axis=1)

# Convert vdn1b to a categorical text variable
df_clean['vdn1b'] = df_clean['vdn1b'].astype('category')

# Verify the conversion
df_clean['vdn1b'].dtype  # Should show 'category'


# Dictionary to rename categories
category_rename_mapping = {
    0: 'unknown',  # Example for numeric 0
    'GLP/Vert\'libéraux': "GLP",
    'bdp': 'BDP',
    'centre parties': 'Centre Parties',
    'csp/pcs': 'CSP',
    'cvp/pdc': 'CVP',
    'edu/udf': 'EDU',
    'evp/pep': 'EVP',
    'fdp/prd': 'FDP',
    'fga/avf': 'FGA',
    'fps/psl': 'FPS',
    'gps/pes': 'GPS',
    'ldu/adi': 'LdU',
    'left parties': 'Left Parties',
    'lega': 'Lega',
    'lps/pls': 'LPS',
    'mcg': 'MCG',
    'other comments': 'Other Comments',
    'other parties': 'Other Parties',
    'pda/pdt': 'PdA',
    'poch': 'POCH',
    'psa (psu)': 'PSA',
    'rep. (& vigil.)': 'Rep',
    'right parties': 'Right Parties',
    'sd/ds': 'SD',
    'sol.': 'Sol',
    'sps/pss': 'SP',
    'svp/udc': 'SVP',
    'voted blank': 'Voted Blank'
}

# Ensure the dictionary keys are matching the current categories
print("Category rename mapping keys:", category_rename_mapping.keys())

# Rename categories
df_clean['vdn1b'] = df_clean['vdn1b'].cat.rename_categories(category_rename_mapping)

# Verify the renaming
print("Renamed categories:", df_clean['vdn1b'].cat.categories)

# Change LPS to FDP
df_clean['vdn1b'] = df_clean['vdn1b'].replace({'LPS': 'FDP'})
print(df_clean.head())


subset = df_clean[df_clean['vdn1b'].isin(['FDP','CVP','CSP','SP','SVP','EVP',
                                                        "PdA", "GLP"])]


# save subset data
subset.to_csv('subset.csv', index=False)