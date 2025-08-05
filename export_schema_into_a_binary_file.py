import pyodbc
import subprocess


# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=Amazon;"
    "UID=SA;"
    "PWD=your-password;"
    "TrustServerCertificate=yes;" # to bypass SSL verification
)

# Get diagram binary
cursor = conn.cursor()
cursor.execute("SELECT definition FROM dbo.sysdiagrams WHERE name = 'Amazon_Diagram'")
diagram_data = cursor.fetchone()[0]

# Save binary file
with open('Amazon_Diagram.bin', 'wb') as f:
    f.write(diagram_data)

print("Diagram binary saved as Amazon_Diagram.bin")
