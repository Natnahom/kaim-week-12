import pandas as pd

# Load data
def load_data(file_path):
    """
    Load the dataset from the given file path.
    """
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
