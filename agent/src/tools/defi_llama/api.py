import requests
import logging
from difflib import SequenceMatcher
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from langchain.pydantic_v1 import BaseModel, Field
from langchain.agents import Tool
from config import Config

class DefiLlamaAPI:
    def __init__(self):
        self.base_url = Config.DEFILLAMA_BASE_URL

    def get_protocols_list(self):
        """Get the list of protocols from DefiLlama API."""
        url = f"{self.base_url}/protocols"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return [item['slug'] for item in data] ,[item['gecko_id'] for item in data]
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to retrieve protocols list: {str(e)}")
            raise

    def get_protocol_tvl(self, protocol_name):
        """Get the TVL (Total Value Locked) of a protocol from DefiLlama API."""
        id,gecko = self.get_protocols_list()
        tag = get_coingecko_id(protocol_name)
        if not tag:
            return None
        protocol_id = next((i for i, j in zip(id, gecko) if j == tag), None)
        if not protocol_id:
            return None
        url = f"{self.base_url}/tvl/{protocol_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to retrieve protocol TVL: {str(e)}")
            raise
