import pandas as pd
import os

def parse_csv(filepath):
    """
    Reads a CSV file and assumes the first row is the header.
    Returns:
       - columns: list of column names
       - data: list of records (dicts)
       - numerical_columns: list of columns that are numeric
    """
    try:
        df = pd.read_csv(filepath)
        
        # Identify numerical columns for charting
        numerical_cols = df.select_dtypes(include=['number']).columns.tolist()
        
        # Convert to dictionary for easy template rendering
        # orient='records' gives [{col1: val1, col2: val2}, ...]
        data = df.to_dict(orient='records')
        columns = df.columns.tolist()
        
        # Prepare chart data (simple structure: label=row index/first col, value=col value)
        # For simplicity, we'll organize chart data by column
        chart_data = {}
        stats = {}
        for col in numerical_cols:
            values = df[col].tolist()
            chart_data[col] = values
            stats[col] = {
                'min': df[col].min(),
                'max': df[col].max(),
                'mean': df[col].mean()
            }
            
        return {
            'columns': columns,
            'data': data[:10], # Preview first 10 rows
            'numerical_columns': numerical_cols,
            'chart_data': chart_data,
            'stats': stats
        }
    except Exception as e:
        print(f"Error parsing CSV: {e}")
        return None
