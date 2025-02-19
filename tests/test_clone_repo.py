import os
import subprocess

def test_clone_repo():
    """Test if the repository is cloned successfully."""
    repo_url = "https://github.com/Onyesi-john/mlops.git"
    clone_dir = "mlops_test_clone"
    
    # Remove existing test directory
    if os.path.exists(clone_dir):
        subprocess.run(["rm", "-rf", clone_dir])

    # Clone repo
    result = subprocess.run(["git", "clone", repo_url, clone_dir], capture_output=True, text=True)
    
    assert os.path.exists(clone_dir), "Repository cloning failed!"
    print("Repository cloned successfully!")

if __name__ == "__main__":
    test_clone_repo()
