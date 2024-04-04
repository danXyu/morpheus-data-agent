from dotenv import load_dotenv
import os
import logging

load_dotenv()

# Logging configuration
logging.basicConfig(level=logging.INFO)

# Configuration object
class Config:
    SANTIMENT_API_KEY = os.getenv("SANTIMENT_API_KEY")
    SANTIMENT_BASE_URL = "https://api.santiment.net/v1"

    # User-facing strings for SantimentAPI functions
    TOKEN_CIRCULATION_SUCCESS_MESSAGE = "The token circulation of {slug} is {value}."
    TOKEN_CIRCULATION_FAILURE_MESSAGE = "Failed to retrieve token circulation for {slug}. Please try again."
    HIGHEST_TRANSACTION_VOLUME_SUCCESS_MESSAGE = "The highest transaction volume for {slug} in the last {days} days is {value}."
    HIGHEST_TRANSACTION_VOLUME_FAILURE_MESSAGE = "Failed to retrieve highest transaction volume for {slug}. Please ensure the slug is correct and try again."
    COINS_WITH_HIGHEST_PRICE_INCREASE_SUCCESS_MESSAGE = "Coins with the highest price increase are: {coins}."
    COINS_WITH_HIGHEST_PRICE_INCREASE_FAILURE_MESSAGE = "Failed to retrieve coins with the highest price increase. Please try again."
    TRENDING_COINS_SUCCESS_MESSAGE = "Trending coins are: {coins}."
    TRENDING_COINS_FAILURE_MESSAGE = "Failed to retrieve trending coins. Please try again."
    HIGHEST_DEV_ACTIVITY_SUCCESS_MESSAGE = "Coins with the highest developer activity are: {coins}."
    HIGHEST_DEV_ACTIVITY_FAILURE_MESSAGE = "Failed to retrieve coins with the highest developer activity. Please try again."
    API_ERROR_MESSAGE = "We're experiencing difficulties accessing the Santiment API at the moment. Please try again later."