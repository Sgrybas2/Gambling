import json
import base64
import requests
from bs4 import BeautifulSoup
from typing import Dict

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

    def fetch_nba_team_stats(self, url: str) -> Dict:
        """
        Fetch NBA team stats from an ESPN NBA team stats page.

        :param url: URL of the ESPN NBA team stats page
        :return: Dictionary containing team stats data
        """
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from {url}, status code: {response.status_code}")

        soup = BeautifulSoup(response.content, 'html.parser')
        stats_table = soup.find('table')  # Assuming the stats are in the first table on the page

        if not stats_table:
            raise Exception("No stats table found on the page")

        headers = [th.text.strip() for th in stats_table.find_all('th')]
        rows = stats_table.find_all('tr')[1:]  # Skip the header row

        team_stats = []
        for row in rows:
            cols = [td.text.strip() for td in row.find_all('td')]
            if len(cols) == len(headers):
                team_stats.append(dict(zip(headers, cols)))

        return {"team_stats": team_stats}

if __name__ == "__main__":
    encoder = GamblingDataEncoder()

    # ESPN NBA team stats URL
    nba_stats_url = "https://www.espn.com/nba/team/stats/_/name/gs"  # Replace with the desired team's stats URL

    # Fetch NBA team stats
    try:
        stats_data = encoder.fetch_nba_team_stats(nba_stats_url)
        print("Fetched Stats Data:", stats_data)

        # Encode the stats data
        encoded_data = encoder.encode_data(stats_data)
        print("Encoded Data:", encoded_data)

        # Decode the encoded data
        decoded_data = encoder.decode_data(encoded_data)
        print("Decoded Data:", decoded_data)
    except Exception as e:
        print("Error:", e)
