"""
api_client.py
Python client for interacting with the NxtAbroad AI Visa Readiness API.
Author: Ibrahim Akintunde Akinyera
"""

import json
import requests


class NxtAbroadAIClient:
    """
    Lightweight Python SDK for calling the NxtAbroad AI FastAPI scoring service.
    """

    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url.rstrip("/")

    def predict(self, profiles):
        """
        Sends one or more profiles for scoring.
        
        Parameters:
            profiles (list[dict]): List of applicant dictionaries.

        Returns:
            dict: API scoring output.
        """
        url = f"{self.base_url}/predict"

        payload = {"profiles": profiles}

        response = requests.post(url, json=payload)

        if response.status_code != 200:
            raise Exception(
                f"API Error {response.status_code}: {response.text}"
            )

        return response.json()

    @staticmethod
    def load_json(path):
        """
        Loads a JSON request file (e.g., data/sample_request.json).
        """
        with open(path, "r") as f:
            return json.load(f)


# --------------------------------------------------------
# Example Usage (only runs when executed as a script)
# --------------------------------------------------------

if __name__ == "__main__":
    client = NxtAbroadAIClient("http://127.0.0.1:8000")

    print("Loading sample request from data/sample_request.json...")
    data = client.load_json("data/sample_request.json")

    print("Sending request to API...")
    result = client.predict(data["profiles"])

    print("\n--- API RESPONSE ---")
    print(json.dumps(result, indent=4))