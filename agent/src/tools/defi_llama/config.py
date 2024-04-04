import logging

# Logging configuration
logging.basicConfig(level=logging.INFO)

# Configuration object
class Config:

    # User-facing strings
    TVL_SUCCESS_MESSAGE = "The TVL of {protocol_name} is ${tvl:,}"
    TVL_FAILURE_MESSAGE = "Failed to retrieve TVL. Please enter a valid protocol name."
    API_ERROR_MESSAGE = "I can't seem to access the API at the moment."
    
