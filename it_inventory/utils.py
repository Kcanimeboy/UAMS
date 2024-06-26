import pandas as pd

def read_excel(file_path):
    try:
        df = pd.read_excel(file_path, skiprows=1)  # Skip the first row (header)
        df = df.fillna('')  # Replace NaN values with empty string or appropriate value
        
        # Convert all column names to strings
        df.columns = df.columns.astype(str)

        # Convert DataFrame to list of dictionaries
        data = df.to_dict(orient='records')

        return data
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return []  # Return empty list if there's an error
