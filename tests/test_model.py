
import torch
from src.model import SimpleNN

def test_model_initialization():
    model = SimpleNN()
    assert model is not None, "Model initialization failed"

def test_model_forward_pass():
    model = SimpleNN()
    input_tensor = torch.rand(1, 10)  # Assuming input size is 10
    output = model(input_tensor)
    assert output is not None, "Model forward pass failed"