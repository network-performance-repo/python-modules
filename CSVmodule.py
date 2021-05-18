import pandas as pd
import numpy as np


def replace_csvfile(file, column, update_from, update_to):
    df = pd.read_csv(file, header=1, sep=',', low_memory = False)
    df[column] = df[column].replace(update_from, update_to)
    return df


def filter_csvfile(file, column,  exclude_values=[], include_values=[]):
    df = pd.read_csv(file, header=1, sep=',', low_memory=False)
    if exclude_values:
        df = df[np.logical_not(df[column].isin(exclude_values))]
    if include_values:
        df = df[df[column].isin(include_values)]
    return df


def pvot_csvfile(file, column):
    df = pd.read_csv(file, header=1, sep=',', low_memory=False)
    df1 = df.groupby([column]).count()
    return df1


def vlookup_csvfile(file, column, lookup_file, lookup_column, table_array):
    left_df = pd.read_csv(file, header=1, sep=',', low_memory=False)
    columns = list(left_df.columns)
    right_df = pd.read_csv(lookup_file, header=1, sep=',', low_memory=False)
    right_df.rename(columns={lookup_column: column}, inplace=True)
    columns.append(list(right_df.columns)[table_array])
    result = pd.merge(left_df, right_df, how='left', on=column, left_index=False, right_index=False)
    return result[columns]
