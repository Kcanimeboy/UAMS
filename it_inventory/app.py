from flask import Flask, jsonify, render_template, request
import pandas as pd

app = Flask(__name__, static_url_path='/static')

# Function to read Excel file and return data as list of dictionaries
def read_excel(file_path):
    try:
        df = pd.read_excel(file_path, skiprows=0)  # Assuming headers are in the first row
        df = df.fillna('')  # Replace NaN values with empty string or appropriate value
        
        # Convert all column names to strings (if not already)
        df.columns = df.columns.astype(str)

        # Convert DataFrame to list of dictionaries
        data = df.to_dict(orient='records')

        return data
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return []  # Return empty list if there's an error

# Route to render index.html template
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch all data from Excel file
@app.route('/data')
def get_data():
    file_path = r'C:\Users\kcanimeboy\Desktop\UAMS\asset_inventory.xlsx'  # Replace with your actual file path
    data = read_excel(file_path)
    return jsonify(data)

# Route to show asset details based on asset code
@app.route('/details')
def show_details():
    asset_code = request.args.get('asset')

    # Logic to fetch specific asset details from data
    file_path = r'C:\Users\kcanimeboy\Desktop\UAMS\asset_inventory.xlsx'  # Replace with your actual file path
    data = read_excel(file_path)

    # Find the asset data based on asset_code
    asset_data = next((row for row in data if row['Asset Code'] == asset_code), None)

    if asset_data:
        return render_template('details.html', asset=asset_data)
    else:
        return 'Asset not found', 404

if __name__ == '__main__':
    app.run(debug=True)
