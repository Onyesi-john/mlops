python
from src.train import train_model  # Assuming you refactor your script into reusable functions

def test_training_process():
    result = train_model(data_path='path/to/a/smaller/test_dataset.csv', epochs=1)
    assert result is not None, "Training process failed"
    assert 'final_loss' in result, "Training did not log final loss"