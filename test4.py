import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bs

page = rq.get(
            'https://www.motordepot.co.uk/used/cars?make=&range=&coin=&min_year=&max_year=&odometer_value=&body_type=&fuel_type=&transmission=&doors=&colour=&min_price=&max_price=&page=&no_options=false&body_types=&seats=&search=&sort=price%7Casc&finance_term=60&finance_deposit=250&finance_mileage=8000&monthly_from=&monthly_to=&resultsPerPage=10&vrm_partial=&location_name=&department_id=&added_since=&status=&tags=&layout=list')

soup = bs(page.content, 'lxml')
name = soup.select('div.vehicle-card > div.vehicle-card-title > h2 > a')
print(name)