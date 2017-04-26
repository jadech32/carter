import requests
from bs4 import BeautifulSoup
import time
# Form Details

website = "https://shop.exclucitylife.com"

email = 'jade.jch@gmail.com'
firstname = 'Jakrarat'
lastname = 'Chunnananda'
address = '2406-788 Richards Street'
city = 'Vancouver'
country = 'Canada'
province = 'British Columbia'
postal = 'V6B3A4'
phone = '7789854625'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}


def checkout(atc_url, captchatoken):
    t0 = time.time()
    session = requests.Session()
    r0 = session.get(atc_url)
    soup = BeautifulSoup(r0.text, 'html.parser')

    form = soup.find('form', {'class': 'edit_checkout'})

    payload = {
        '_method': 'patch',
        'authenticity_token': form.find('input', {'name': 'authenticity_token'})['value'],
        'button': '',
        'checkout[client_details][browser_height]': '728',
        'checkout[client_details][browser_width]': '1280',
        'checkout[client_details][javascript_enabled]': '1',
        'checkout[email]': email,
        'checkout[shipping_address][address1]': address,
        'checkout[shipping_address][address2]': '',
        'checkout[shipping_address][city]': city,
        'checkout[shipping_address][country]': country,
        'checkout[shipping_address][first_name]': firstname,
        'checkout[shipping_address][last_name]': lastname,
        'checkout[shipping_address][phone]': phone,
        'checkout[shipping_address][province]': province,
        'checkout[shipping_address][zip]': postal,
        'previous_step': 'contact_information',
        'remember_me': 'false',
        'step': 'shipping_method',
        'utf8': '✓'
    }

    # Submitting Shipping
    r1 = session.post(website+form['action'], data=payload, headers=headers)
    print("Submitted Shipping - took " + str(time.time()-t0) + 's')


