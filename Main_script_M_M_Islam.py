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

