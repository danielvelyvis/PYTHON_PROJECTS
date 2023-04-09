import requests
from bs4 import BeautifulSoup
import csv

def find_data(soup):
    # Find the element containing the value
    market_cap_elem = soup.find('td', string ='Market Cap')
    revenue_elem = soup.find('td', string ='Revenue (ttm)')
    net_income_elem = soup.find('td', string ='Net Income (ttm)')
    volume_elem = soup.find('td', string ='Volume')
    beta_elem = soup.find('td', string ='Beta')
    #shares_out_elem = soup.find('td', string ='Shares Out')
    eps_elem = soup.find('td', string ='EPS (ttm)')
    pe_elem = soup.find('td', string ='PE Ratio')
    pe_forward_elem = soup.find('td', string ='Forward PE')

    # Extract the value
    market_cap = market_cap_elem.find_next_sibling('td').get_text(strip=True)
    revenue = revenue_elem.find_next_sibling('td').get_text(strip=True)
    net_income = net_income_elem.find_next_sibling('td').get_text(strip=True)
    volume = volume_elem.find_next_sibling('td').get_text(strip=True)
    beta = beta_elem.find_next_sibling('td').get_text(strip=True)
    #shares_out = shares_out_elem.find_next_sibling('td').get_text(strip=True)
    eps = eps_elem.find_next_sibling('td').get_text(strip=True)
    pe = pe_elem.find_next_sibling('td').get_text(strip=True)
    pe_forward = pe_forward_elem.find_next_sibling('td').get_text(strip=True)

    stocks_dict = {
        'Market Cap': market_cap,
        'Revenue': revenue,
        'Net Income': net_income,
        'Volume': volume,
        'Beta': beta,
        #'Shares Out': shares_out,
        'EPS (ttm)': eps,
        'Price to Earnings': pe,
        'Forward Price to Earnings': pe_forward
                   }

    return stocks_dict

def parse_url(url):
    # Send a request to the website and get the HTML response
    response = requests.get(url)
    html = response.content

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    return soup

def read_csv():
    with open('nasdaq_data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        rows = [row for row in reader] # Read all rows in the CSV file
        return rows

def dload_tkrs():
    url = "https://pkgstore.datahub.io/core/nasdaq-listings/nasdaq-listed-symbols_csv/data/595a1f263719c09a8a0b4a64f17112c6/nasdaq-listed-symbols_csv.csv"
    response = requests.get(url)

    with open("nasdaq_data.csv", "wb") as f:
        f.write(response.content)

    f.close()

def main():

    dload_tkrs()
    rows = read_csv()
    for row in rows:
        # Specify the URL of the website to scrape
        url = 'https://stockanalysis.com/stocks/'+row[0]+'/'

        try:
            soup = parse_url(url)
            stocks_dict = find_data(soup)

            print(row[0])
            print(row[1])
            print(url)

            for key, value in stocks_dict.items():
                print(f'{key}: {value}')

            print('\n')

        except:
            pass

if __name__ == '__main__':
    main()






'''
print(soup.prettify())

# Print the title of the website
print(soup.title.text)

# Print all the links in the website
for link in soup.find_all('a'):
    print(link.get('href'))
print (response.status_code)
'''

#print('Market Cap:', market_cap_value)

