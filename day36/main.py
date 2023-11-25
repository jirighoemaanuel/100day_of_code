import requests
from dotenv import load_dotenv
import os
load_dotenv()


NEWS_KEY = os.getenv("NEWS_KEY")
STOCK_KEY = os.getenv("STOCK_KEY")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = F"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={
    STOCK_NAME}&apikey={STOCK_KEY}"
NEWS_ENDPOINT = F"https://newsapi.org/v2/everything?q={
    COMPANY_NAME}&sortBy=popularity&apiKey={NEWS_KEY}"


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
percent_difference = round((price_difference/yesterday_closing_price) * 100, 2)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percent_difference > 5:
    print('Get News')
# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
news_response = requests.get(url=NEWS_ENDPOINT)
news_response.raise_for_status()
news_data = news_response.json()

first_3_articles = news_data["articles"][:3]

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.


articles_headlines_and_description = [
    [article['title'], article['description']] for article in first_3_articles]
print(articles_headlines_and_description)

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
