import os
import time
import logging
from eodhd import APIClient

# Configure Logging for Railway
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load API Key from Railway Variables
API_KEY = os.getenv("EODHD_API_KEY")
SYMBOL = "NVDA.US"  # Ensure you add the exchange suffix

client = APIClient(API_KEY)

def run_strategy():
    try:
        logger.info(f"Fetching data for {SYMBOL}...")
        # Fetching real-time data
        data = client.get_live_stock_prices(SYMBOL)
        
        # Example logic: Accessing price
        # Note: EODHD live API returns JSON; convert to dict/frame as needed
        current_price = data[0].get('close')
        logger.info(f"Current Price of {SYMBOL}: {current_price}")
        
        # ADD YOUR STRATEGY LOGIC HERE
        # e.g., if price < some_threshold: trigger_trade()
        
    except Exception as e:
        logger.error(f"Strategy Error: {e}")

if __name__ == "__main__":
    logger.info("Bot service initialized.")
    while True:
        run_strategy()
        time.sleep(60)  # Check every 60 seconds
