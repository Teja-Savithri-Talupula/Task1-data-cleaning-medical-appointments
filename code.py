import pandas as pd

file_path = "Medical Appointment No Shows.csv"  
df = pd.read_csv(file_path)

print("Missing values per column:")
print(df.isnull().sum())

df = df.drop_duplicates()

df['Gender'] = df['Gender'].replace({'F': 'Female', 'M': 'Male'})
df['No-show'] = df['No-show'].replace({'No': 'Showed Up', 'Yes': 'No Show'})

df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay']).dt.strftime('%d-%m-%Y')
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay']).dt.strftime('%d-%m-%Y')

df.columns = [col.strip().lower().replace(' ', '_').replace('-', '_') for col in df.columns]

print("\nData types after cleaning:")
print(df.dtypes)

print("\nCleaned dataset preview:")
print(df.head())

df.to_csv("Cleaned_Medical_Appointment.csv", index=False)
