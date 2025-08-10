import pandas as pd

### Extract the required GDP data from the given URL using Web Scraping.

URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

# Extract tables from webpage using Pandas. Retain table number 3 as the required dataframe.
tables = pd.read_html(URL)
df = tables[3]
print(tables)

# To print each DataFrame individually, you can use a loop
print("\n--- Displaying each table separately ---\n")
for i, table in enumerate(tables):
    print(f"--- Table {i} ---\n")
    print(table)
    print("\n")
# Replace the column headers with column numbers
df.columns = range(df.shape[1])

# Retain columns with index 0 and 2 (name of country and value of GDP quoted by IMF)
df = df[[0,2]]

# Retain the Rows with index 1 to 10, indicating the top 10 economies of the world.
df = df.iloc[1:11,:]

# Assign column names as "Country" and "GDP (Million USD)"
df.columns = ['Country','GDP (Million USD)']

