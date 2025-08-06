# Use a variable q to store the column Price as a dataframe
q = df[['Price']]
q
# Assign the variable q to the dataframe that is made up of the column Product and Category:
q = df[['Product', 'Category']]
q

# Access the 2nd row and the 3rd column of df:
df.iloc[1, 2]

w_index=['a','b','c','d','e']
df_new=df
df_new.index=new_index
df_new.loc['a', 'CustomerCity']
df_new.loc['a':'d', 'CustomerCity']
