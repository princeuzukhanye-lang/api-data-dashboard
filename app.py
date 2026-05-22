from api import get_bitcoin_price
from display import show_price
import time

print("🚀 Starting API Dashboard...\n")

while True:
    price = get_bitcoin_price()
    show_price(price)
    time.sleep(15)
