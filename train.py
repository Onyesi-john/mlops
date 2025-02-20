"""
Train script for the SimpleNN model using PyTorch and MLflow.
"""

import os
import sys
import torch
from torch import nn, optim  # Updated import style
import pandas as pd
import mlflow
import mlflow.pytorch

# Ensure the script can find local modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from model import SimpleNN  # Local import should be placed last

# Set MLflow tracking URI to a directory where Jenkins has write access
mlflow.set_tracking_uri("file:///tmp/mlflow")
mlflow.set_experiment("dlops_experiment")

# Load training data
DATA_PATH = "data.csv"  # Updated to UPPER_CASE for constant naming convention

# Check if the file exists
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Dataset file {DATA_PATH} not found. Please make sure the file exists.")

data = pd.read_csv(DATA_PATH)

# Print out the first few rows of data to verify it's being loaded
print(f"Data preview:\n{data.head()}")

X = torch.tensor(data.iloc[:, :-1].values, dtype=torch.float32)
y = torch.tensor(data.iloc[:, -1].values, dtype=torch.float32).view(-1, 1)

# Verify shape of input data
print(f"Shape of X: {X.shape}, Shape of y: {y.shape}")

# Initialize model
model = SimpleNN()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Define example input for logging the model with signature
example_input = X[0].numpy()  # Convert tensor to numpy.ndarray

# Log model with input example for signature
mlflow.set_experiment("dlops_experiment")
with mlflow.start_run():
    # Train model
    for epoch in range(10):
        # Forward pass
        outputs = model(X)
        loss = criterion(outputs, y)
        
        # Backward pass and optimization
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        
        # Log the loss for each epoch
        mlflow.log_metric("loss", loss.item(), step=epoch)
        
        # Print progress
        print(f"Epoch [{epoch+1}/10], Loss: {loss.item()}")
    
    # Log the model and the final loss after training
    mlflow.pytorch.log_model(model, "model", input_example=example_input)
    mlflow.log_metric("final_loss", loss.item())

    # Check logging confirmation
    mlflow.log_param("epochs", 10)
    mlflow.log_param("optimizer", "Adam")
    mlflow.log_param("loss_function", "MSELoss")
    print("Training complete, model and metrics logged to MLflow.")
