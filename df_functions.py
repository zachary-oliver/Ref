# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
Created on 9/18/17
@author: Zachary Oliver
"""

import pandas as pd
from os_functions import create_Folders_Along_Path, evaluate_If_File_Exists

'''********************************************
**********************EXPORT*******************
***********************************************
'''
def df_export_csv(df, path, include_index=False):
    create_Folders_Along_Path(path)
    df.to_csv(path, index=include_index)

'''********************************************
**********************READ*********************
***********************************************
'''
def df_read_csv(relative_path, DF_INDEX_CSV_COLUMN_NUMBER=0):
    if evaluate_If_File_Exists(relative_path):
        df = pd.read_csv(relative_path, index_col=DF_INDEX_CSV_COLUMN_NUMBER)
        if df_is_empty(df):
            return None
        return df
    else:
        return None

def df_read_dict(dict):
    df = pd.DataFrame.from_dict(dict)
    return df

def df_read_mongodb(cursor):
    df = pd.DataFrame(list(cursor))
    return df

# issue: if there are any comments in the sql file this will not read
def df_read_sql(sql, conn):
    return pd.read_sql_query(sql, conn)

'''********************************************
*********************PRINT*********************
***********************************************
'''
def df_print_columns_all_rows(df,list):
    print df[list]

def df_print_rows_all_columns(df,first,last):
    print df[first:last]

def df_print_rows_columns(df,first,last,list):
    print df[first:last,list]

def df_print_columns(df):
    for x in df.columns.values:
        print x

def df_print_top(df,top):
    print df.head(top)

def df_print_bottom(df,bottom):
    print df.tail(bottom)

def df_print_random_sample(df,size):
    print df.sample(n=size, random_state=1)

def df_print_details():
    print 

'''********************************************
**********************GET**********************
***********************************************
'''
def df_get_column_name(df, index):
    if df_is_empty(df):
        return None
    return df.columns[index]

def df_get_columns_all_rows(df,columns_list):
    if df_is_empty(df):
        return None
    return df[columns_list]

def df_get_rows_all_columns(df,first,last):
    if df_is_empty(df):
        return None
    return df[first:last]

def df_get_rows_columns(df,first_row,last_row,columns_list):
    if df_is_empty(df):
        return None
    return df[first_row:last_row,columns_list]

def df_get_row_column(df,row,column):
    if df_is_empty(df):
        return None
    return df.iloc[row][column]

def df_get_top(df,top):
    if df_is_empty(df):
        return None
    return df.head(top)

def df_get_top_as_str(df,top):
    if df_is_empty(df):
        return None
    return df_get_top(df,top).to_string()

def df_get_bottom(df,bottom):
    if df_is_empty(df):
        return None
    return df.tail(bottom)

def df_get_rows_where_column_equals_value(df, column, value):
    return df.loc[(df[column] == value)]

def df_get_random_sample(df,size):
    if df_is_empty(df):
        return None
    return df.sample(n=size, random_state=1)

# AS_TYPE: https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.dtype.html#numpy.dtype
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Index.astype.html#pandas.Index.astype
def df_get_indexes(df, AS_TYPE=False):
    if AS_TYPE:
        return df.index.astype(AS_TYPE)
    return df.index.values

# UNIT TESTED
def df_get_cell(df, str_index, str_column):
    return df.at[str_index, str_column]

def df_get_list_from_column(df, column):
    return df[column].tolist()

def df_get_list_of_list(df):
    return df.values.tolist()

# UNIT TESTED
def df_get_details(df):
    return {
            'column_data_types': df.dtypes,
            'dataframe_shape': df.shape,
            'data_descriptions': df.describe(include='all')
            }

'''********************************************
********************CHANGE********************
***********************************************
'''
def df_change_cell(df, str_index, str_column, value):
    df.at[str_index, str_column] = value

'''********************************************
********************COMBINE********************
***********************************************
'''
#place the dfs on top of each other with axis=0
# https://stackoverflow.com/questions/50501787/python-pandas-user-warning
def df_concat(df1, df2, AXIS=1, SORT=True):
    return pd.concat([df1, df2], axis=AXIS, sort=SORT)

# https://www.shanelynn.ie/merge-join-dataframes-python-pandas-index-1/
# https://www.codeproject.com/KB/database/Visual_SQL_Joins/Visual_SQL_JOINS_orig.jpg
def df_merge(df1, df2):
    return pd.merge(df1, df2, left_index=True, right_index=True)

'''********************************************
********************REMOVE********************
***********************************************
'''
def df_remove_column(df, column):
    return df.drop(column, axis=1, inplace=True)

def df_remove_column_by_index(df, index):
    return df.drop(df.columns[index], axis=1, inplace=True)

# https://stackoverflow.com/questions/18172851/deleting-dataframe-row-in-pandas-based-on-column-value
def df_remove_row_by_query(df, str_query):
    return df.query(str_query)

def df_remove_row_by_value(df, str_column, value):
    return df[df[str_column] != value]

def df_remove_row_by_values(df, str_column, values):
    for v in values:
        df = df[df[str_column] != v]
    return df

'''********************************************
********************RENAME********************
***********************************************
'''
def df_rename_column(df, orig_column, new_column):
    df.rename(columns={orig_column:new_column}, inplace=True)

'''********************************************
*********************COUNT*********************
***********************************************
'''
def df_get_index_counts(df, debug=False):
    if debug:
        print df.value_counts() #always displays highest to lowest
    return df.value_counts()

def df_get_row_count(df, debug=False):
    if debug:
        print df.shape[0]
    return df.shape[0] #gives number of row count

def df_get_column_count(df, debug=False):
    if debug:
        print df.shape[1]
    return df.shape[1] #gives number of column count

'''********************************************
**********************SET**********************
***********************************************
'''
def df_set_index(df, column):
    df.set_index([column], inplace=True) #always displays highest to lowest

'''********************************************
*********************SORT**********************
***********************************************
'''
# https://stackoverflow.com/questions/22211737/python-pandas-how-to-sort-dataframe-by-index
def df_sort_by_index(df):
    df.sort_index(inplace=True)

# http://cmdlinetips.com/2018/02/how-to-sort-pandas-dataframe-by-columns-and-row/
def df_sort_by_column(df, str_column, sort_ascending=False):
    df.sort_values(str_column, ascending=sort_ascending, inplace=True)

'''********************************************
********************FORMAT*********************
***********************************************
'''
def df_format_object_to_date(df, str_column):
    df[str_column] = pd.to_datetime(df[str_column])

""" replace_null
replaces null in bed with 0 and returns the data frame
variables:
df -- dataframe you want to clean
field -- name of attirbute you want to replace nulls with 0
"""
def df_format_replace_null(df, field, inPlace=True):
    if (inPlace):
        df[field].fillna(0, inplace=inPlace)
    else:
        df_new = df[field].fillna(0, inplace=inPlace)
        return df_new

""" replace_null
replaces null in bed with 0 and returns the data frame
variables:
df -- dataframe you want to clean
field -- name of attirbute you want to replace nulls with 0
"""
def df_format_replace_all_null(df):
    df.fillna(0, inplace=True)
    
def df_format_as_str(df):
    return df.to_string()

'''********************************************
********************CREATE*********************
***********************************************
'''
def df_create_df_dict(keys):
    return {elem : pd.DataFrame for elem in keys}

def df_create_blank_df(df_index, df_columns_list):
    return pd.DataFrame(index=df_index, columns=df_columns_list)

def df_create_blank():
    return pd.DataFrame({'A' : []})

# UNIT TESTED
def df_create_basic_int():
    return pd.DataFrame(data=[1,2,3,4], index=range(0,4), columns=['A'])

# UNIT TESTED
def df_create_basic_str():
    return pd.DataFrame(data=['a','b','c','d'], index=range(0,4), columns=['A'])

'''********************************************
*********************CHECK*********************
***********************************************
'''
def df_is_empty(df):
    return df.empty

'''********************************************
*********************SEARCH********************
***********************************************
'''
# https://stackoverflow.com/questions/23549231/check-if-a-value-exists-in-pandas-dataframe-index
def df_search_indexes(df, value):
    return value in df.index






'''*******************************************************************
********************       UNIT TESTS      ***************************
**********************************************************************
'''
def UNIT_TESTING():
    df_int = df_create_basic_int()
    dict_details_df_int = df_get_details(df_int)
    if dict_details_df_int['dataframe_shape'][0] != 4 or dict_details_df_int['dataframe_shape'][1] != 1:
        print 'df_functions FAILED: df_create_basic_int, df_get_details dataframe_shape not correct'
    if df_get_cell(dict_details_df_int['data_descriptions'], 'count', 'A') != 4.0 or df_get_cell(dict_details_df_int['data_descriptions'], 'mean', 'A') != 2.5:
        print 'df_functions FAILED: df_get_cell, df_get_details data_descriptions not correct'

    df_str = df_create_basic_str()
    dict_details_df_str = df_get_details(df_str)
    if dict_details_df_str['dataframe_shape'][0] != 4 or dict_details_df_str['dataframe_shape'][1] != 1:
        print 'df_functions FAILED: df_create_basic_int, df_get_details shape not correct'
    if df_get_cell(dict_details_df_str['data_descriptions'], 'count', 'A') != 4 or df_get_cell(dict_details_df_str['data_descriptions'], 'top', 'A') != 'd':
        print 'df_functions FAILED: df_get_cell, df_get_details data_descriptions not correct'

UNIT_TESTING()
