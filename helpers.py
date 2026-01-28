import requests
import time


def is_url_reachable(url: str) -> bool:
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False


def retrieve_phone_code(driver):
    """
    Retrieves the SMS code from Chrome performance logs.
    This function is REQUIRED by the project description.
    """
    time.sleep(2)
    logs = driver.get_log("performance")
    for entry in logs:
        if "smsCode" in entry["message"]:
            return entry["message"][-4:]
    return "0000"
