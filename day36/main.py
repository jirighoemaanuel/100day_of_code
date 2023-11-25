import requests
from dotenv import load_dotenv
from twilio.rest import Client
import os

load_dotenv()

NEWS_KEY = os.getenv("NEWS_KEY")
STOCK_KEY = os.getenv("STOCK_KEY")
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]


client = Client(account_sid, auth_token)


STOCK_ENDPOINT = F"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={
    STOCK_NAME}&apikey={STOCK_KEY}"
NEWS_ENDPOINT = F"https://newsapi.org/v2/everything?q={
    COMPANY_NAME}&sortBy=popularity&apiKey={NEWS_KEY}"

news_response = requests.get(url=NEWS_ENDPOINT)
news_response.raise_for_status()
news_data = news_response.json()

first_3_articles = news_data["articles"][:3]

# Get the stock prices for tesla
stock_response = requests.get(url=STOCK_ENDPOINT)
stock_response.raise_for_status()
stock_data = stock_response.json()
prices = [prices for (
    prices) in stock_data["Time Series (Daily)"].values()]

# yesterday stock closing for tesla
yesterday_closing_price = float(prices[0]['4. close'])

# day before yesterday stock closing for tesla
day_bfr_yesterday_closing_price = float(prices[1]['4. close'])
# print(yesterday_closing_price, day_bfr_yesterday_closing_price)


# Check the price difference
price_difference = abs(yesterday_closing_price -
                       day_bfr_yesterday_closing_price)
price_difference = round(price_difference, 2)
# print(price_difference)

# Check the percentage difference
percent_difference = round(
    (price_difference / yesterday_closing_price) * 100, 2)


if percent_difference > 5:

    articles_headlines_and_description = [
        [article['title'], article['description']] for article in first_3_articles]

    for title, description in articles_headlines_and_description:
        message = client.messages \
            .create(
                body=f"TSLA: 🔺{percent_difference}%"
                f"Headlines: {title}"
                f"Brief: {description}",
                from_='+16194521087',
                to='+2347037642158'
            )
