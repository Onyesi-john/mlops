import subprocess

def test_auto_retraining():
    """Test if retraining script runs when loss is high."""
    loss_output = subprocess.run(["python", "check_loss.py"], capture_output=True, text=True)
    loss = float(loss_output.stdout.strip())

    if loss > 0.5:
        retrain_output = subprocess.run(["python", "retrain.py"], capture_output=True, text=True)
        assert "Retraining complete" in retrain_output.stdout, "Retraining failed!"
        print("Auto-retraining triggered successfully!")

if __name__ == "__main__":
    test_auto_retraining()
