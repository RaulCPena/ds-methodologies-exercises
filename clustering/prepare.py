


# remove unwanted columns

def remove_columns(df, cols_to_remove):
    df = df.drop(columns=cols_to_remove)

    return df

# Remove rows & columns based on a minimum percentage of values available for each row/columns:

def handle_missing_values(df, prop_required_column = .5, prop_required_row = .75):

    columns_missing = int(round(prop_required_column*len(df.index)))
    df.dropna(axis=1, thresh=columns_missing, inplace=True)
    rows_missing = int(round(prop_required_row*len(df.columns)))
    df.dropna(axis=0, thresh=rows_missing, inplace=True)

    return df

# put it all toghether

def data_prep(df, cols_to_remove=[], prop_required_column=.5, prop_required_row=.75):
    df = remove_columns(df, cols_to_remove)
    df = handle_missing_values(df, prop_required_column, prop_required_row)

    return df

# filter out properties by the following
def filter_single_unit_properties(df):
    df = (df[(df['propertylandusedesc'] == 'Single Family Residential') | (df['propertylandusedesc'] == 'Planned Unit Development') | (df['propertylandusedesc'] == 'Manufactured, Modular, Prefabricated Homes')])

    return df
