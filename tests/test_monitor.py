import requests

def test_monitor_model():
    """Test if the monitoring API is running and responding correctly."""
    response = requests.get("http://localhost:9090/api/v1/query?query=loss")

    assert response.status_code == 200, "Monitoring API not responding!"
    print("Monitoring API is working correctly!")

if __name__ == "__main__":
    test_monitor_model()
