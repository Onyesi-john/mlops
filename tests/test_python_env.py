import os
import subprocess

def test_python_env():
    """Test if the virtual environment is set up and dependencies installed."""
    subprocess.run(["python3", "-m", "venv", "venv"])
    assert os.path.exists("venv"), "Virtual environment was not created!"

    subprocess.run(["bash", "-c", "source venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt"], shell=True)
    result = subprocess.run(["bash", "-c", "source venv/bin/activate && pip list"], capture_output=True, text=True, shell=True)

    assert "mlflow" in result.stdout, "MLflow not installed!"
    assert "numpy" in result.stdout, "NumPy not installed!"
    print("Python environment setup successful!")

if __name__ == "__main__":
    test_python_env()
