from bs4 import BeautifulSoup
html_snippet = '<td class="price"><a href="/tablets/shops-39407-apple-ipad-10.2-2021.aspx">17,190,000 </a></td>'

soup = BeautifulSoup(html_snippet, 'html.parser')
price_td = soup.find('td', class_='price')
a_element = price_td.find('a')
price_text = a_element.text.strip()
price = int(price_text.replace(',', ''))
print(f"The product price is: {price}")