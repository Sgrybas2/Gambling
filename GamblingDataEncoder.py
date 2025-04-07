import json
import base64
from typing import List, Dict

class GamblingDataEncoder:
    def __init__(self):
        pass

    def encode_data(self, data: Dict) -> str:
        """
        Encode the gambling data into a Base64 encoded JSON string.

        :param data: Dictionary containing gambling data
        :return: Base64 encoded JSON string
        """
        # Convert the data dictionary to a JSON string
        json_data = json.dumps(data)
        # Encode the JSON string to Base64
        encoded_data = base64.b64encode(json_data.encode()).decode()
        return encoded_data

    def decode_data(self, encoded_data: str) -> Dict:
        """
        Decode the Base64 encoded JSON string back into a dictionary.

        :param encoded_data: Base64 encoded JSON string
        :return: Dictionary containing gambling data
        """
        # Decode the Base64 string to JSON
        json_data = base64.b64decode(encoded_data.encode()).decode()
        # Convert the JSON string back to a dictionary
        data = json.loads(json_data)
        return data

if __name__ == "__main__":
    encoder = GamblingDataEncoder()
    
    # Sample gambling data
    sample_data = {
        "bets": [
            {"player": "Alice", "amount": 100, "outcome": "win"},
            {"player": "Bob", "amount": 50, "outcome": "lose"}
        ],
        "timestamp": "2025-04-07 21:29:35"
    }
    
    # Encode the sample data
    encoded_data = encoder.encode_data(sample_data)
    print("Encoded Data:", encoded_data)
    
    # Decode the encoded data
    decoded_data = encoder.decode_data(encoded_data)
    print("Decoded Data:", decoded_data)
