import pandas as pd

# from Supplementary_script_class_Linear_Reg_Diagnostic import Linear_Reg_Diagnostic



#### A. Step-1: Data tidying  ####

### A.1. Economic dataset
### A.1.1. Data import
Economic_variables_DF = pd.read_excel('Economic variables.xlsx')
col_number_initial = len(Economic_variables_DF.columns)  
row_number_initial = len(Economic_variables_DF)   
Economic_variables_DF = Economic_variables_DF.rename(columns={'Unnamed: 1':'Eco_var','Unnamed: 2':'Unit'})

## adding a comment

## A.2. VMT dataset
VMT_DF = pd.read_excel('Historical VMT.xlsx')
VMT_DF.columns.values[1] = 'VMT'   
VMT_2020_2021 = VMT_DF['VMT'].to_numpy()
row_VMT_DF = len(VMT_DF)
VMT_DF = VMT_DF.drop(VMT_DF.index[row_VMT_DF-1])   # deleting the last row (i.e. row for the year 2021)

### checking for push option again