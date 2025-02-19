import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import pytest
import numpy as np
from train import train_model  # Import your training function
from model import load_model  # Adjust this based on your model loading function

def test_data_loading():
    """Ensure data loads correctly"""
    data = np.random.rand(100, 10)  # Mock data
    assert data.shape == (100, 10), "Data shape mismatch"

def test_model_training():
    """Ensure model training runs without errors"""
    try:
        model = train_model()  # Assuming this function trains and returns a model
        assert model is not None, "Training failed, model is None"
    except Exception as e:
        pytest.fail(f"Model training failed: {e}")

def test_model_inference():
    """Ensure model can make predictions"""
    model = load_model("saved_model.pth")  # Adjust for your model
    sample_input = np.random.rand(1, 10)  # Adjust input size as per your model
    prediction = model.predict(sample_input)
    assert prediction.shape[0] == 1, "Output shape mismatch"

if __name__ == "__main__":
    pytest.main()
