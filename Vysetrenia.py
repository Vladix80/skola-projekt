import pandas as pd
import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=(localdb)\\MSSQLLocalDB;"
    "DATABASE=Škola;"
    "Trusted_Connection=yes;"
)

dotaz = "SELECT * FROM dbo.Vysetrenia"
df = pd.read_sql(dotaz, conn)

pd.set_option('display.max_columns', None)
print(df.head())