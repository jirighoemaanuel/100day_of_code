import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(
    url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6", headers=headers)
amazon_web_page = response.text
soup = BeautifulSoup(amazon_web_page, 'lxml')

whole_price = soup.find(name="span", class_="a-price-whole")
fraction_price = soup.find(name="span", class_="a-price-fraction")
price = whole_price.text + fraction_price.text
if float(price) < 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Amazon Price Alert!\n\ninstant Pot Duo Plus 9-in-1 Electric Cooker, Sterilizer, SLow Cooker, Rice Cooker, Grain Maker, Steamer, Saute, Yogurt Maker, Sous Vide, Bake, and Warmer, 6 Quartz, 10 Programs if no ${price}\nhttps://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
        print("sent successfully")


# prices = zip(whole_prices, fraction_prices)
# total_price = [whole_price.text +
#                fraction_price.text for whole_price, fraction_price in prices]
