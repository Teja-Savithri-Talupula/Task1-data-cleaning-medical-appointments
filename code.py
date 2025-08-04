import pandas as pd
from IPython.display import FileLink, display

file_path = "Medical Appointment No Shows.csv"  
df = pd.read_csv(file_path)

print(" Missing values per column:")
print(df.isnull().sum())

df = df.drop_duplicates()

df['Gender'] = df['Gender'].replace({'F': 'Female', 'M': 'Male'})
df['No-show'] = df['No-show'].replace({'No': 'Showed Up', 'Yes': 'No Show'})

df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay']).dt.strftime('%d-%m-%Y')
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay']).dt.strftime('%d-%m-%Y')

df.columns = [col.strip().lower().replace(' ', '_').replace('-', '_') for col in df.columns]

excel_file_name = "Cleaned_Medical_Appointment.xlsx"
df.to_excel(excel_file_name, index=False)

print("\n Cleaned Dataset Preview (first 10 rows):")
display(df.head(10))

print("\n Click below to download the cleaned Excel file:")
display(FileLink(excel_file_name))
