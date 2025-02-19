import subprocess

def test_docker_build():
    """Test if Docker image is built successfully."""
    result = subprocess.run(["docker", "build", "-t", "ghcr.io/onyesi-john/mlops:latest", "."], capture_output=True, text=True)

    assert "Successfully built" in result.stdout or "Successfully tagged" in result.stdout, "Docker build failed!"
    print("Docker image built successfully!")

if __name__ == "__main__":
    test_docker_build()
