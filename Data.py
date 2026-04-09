import pandas as pd

# Creating a realistic mock dataset that simulates the 2020 COVID-19 spike
data = {
    'Region': [
        # Delhi Data
        'Delhi', 'Delhi', 'Delhi', 'Delhi', 'Delhi',
        # Maharashtra Data
        'Maharashtra', 'Maharashtra', 'Maharashtra', 'Maharashtra', 'Maharashtra',
        # Karnataka Data
        'Karnataka', 'Karnataka', 'Karnataka', 'Karnataka', 'Karnataka'
    ],
    'Date': [
        # Jan, Feb, April (Lockdown), May, June
        '31-01-2020', '29-02-2020', '30-04-2020', '31-05-2020', '30-06-2020',
        '31-01-2020', '29-02-2020', '30-04-2020', '31-05-2020', '30-06-2020',
        '31-01-2020', '29-02-2020', '30-04-2020', '31-05-2020', '30-06-2020'
    ],
    'Estimated Unemployment Rate (%)': [
        # Normal -> Spike -> Recovery
        8.5, 8.2, 24.1, 22.5, 12.1,
        7.2, 7.5, 25.3, 23.0, 10.5,
        6.1, 6.3, 21.0, 19.5, 9.8
    ]
}

# Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Save it as a CSV file in the current folder
df.to_csv('Unemployment in India.csv', index=False)

print("✅ Success! 'Unemployment in India.csv' has been created in your folder.")
