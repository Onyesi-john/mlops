import subprocess

def test_docker_push():
    """Test if Docker push authentication works."""
    result = subprocess.run(["docker", "login", "ghcr.io", "-u", "$DOCKER_USER", "--password", "$DOCKER_PASS"], capture_output=True, text=True)

    assert "Login Succeeded" in result.stdout, "Docker authentication failed!"
    print("Docker login successful!")

if __name__ == "__main__":
    test_docker_push()
