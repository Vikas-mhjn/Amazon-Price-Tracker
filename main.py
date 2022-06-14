import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

BUY_PRICE = 100
URL = "https://www.amazon.com/dp/B091C4RFWT/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B091C4RFWT&pd" \
      "_rd_w=3FPdB&pf_rd_p=085568d9-3b13-4ac1-8ae4-24a26c00cb0c&pd_rd_wg=Z81"

header = {
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8,es;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/90.0.4430.93 Safari/537.36"
}
response = requests.get(URL, headers=header)
website_html = response.content


soup = BeautifulSoup(website_html, "lxml")
print(soup.prettify())
title = soup.find(id="productTitle").get_text().strip()
price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(your_smtp_address, port= 587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )
