import subprocess

def test_model_training():
    """Test if the model trains successfully."""
    result = subprocess.run(["bash", "-c", "source venv/bin/activate && python train.py"], capture_output=True, text=True, shell=True)
    
    assert "Training complete" in result.stdout, "Training failed!"
    print("Model training successful!")

if __name__ == "__main__":
    test_model_training()
