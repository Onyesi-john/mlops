
import os
import pandas as pd
from src.train import load_data  # Assuming you refactor data loading into a function

def test_data_loading():
    # Mock a small dataset
    data = pd.DataFrame({
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'label': [0, 1, 0]
    })
    # Temporarily save this data to a CSV file
    temp_path = 'temp_data.csv'
    data.to_csv(temp_path, index=False)
    
    loaded_data = load_data(temp_path)
    
    # Cleanup the temporary file
    os.remove(temp_path)
    
    assert not loaded_data.empty, "Data loading failed, dataframe is empty"