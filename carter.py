import requests
from bs4 import BeautifulSoup
import time
# Form Details

website = "https://shop.exclucitylife.com"

email = ''
firstname = ''
lastname = ''
address = ''
city = ''
country = ''
province = ''
postal = ''
phone = ''

cardexpmonth = ''
cardnumber = ''
cardexpyear = ''
cvv = ''


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
    print("Submitted sipping info " + str(time.time()-t0) + 's')

    soup1 = BeautifulSoup(r1.text, 'html.parser')
    form1 = soup1.find('form', {'class': 'edit_checkout'})

    payload1 = {
        '_method': 'patch',
        'authenticity_token': form1.find('input', {'name': 'authenticity_token'})['value'],
        'button': '',
        'checkout[client_details][browser_height]': '728',
        'checkout[client_details][browser_width]': '1280',
        'checkout[client_details][javascript_enabled]': '1',
        'checkout[shipping_rate][id]': 'shopify-Expedited%20Parcels%20W/%20Signature%20&%20Delivery%20confirmation%20(1-2%20business%20days)-0.00',
        'previous_step': 'shipping_method',
        'step': 'payment_method',
        'utf8': ''
    }

    # Submitting Shipping Method
    r2 = session.post(website+form1['action'], data=payload1, headers=headers)
    print(r2.status_code)
    print("Submitted shipping method: " + str(time.time()-t0) + 's')

    soup2 = BeautifulSoup(r2.text, 'html.parser')
    form2 = soup2.find('form', {'class': 'edit_checkout'})

    payload2 = {
        'utf8': '✓',
        'authenticity_token': form2.find('input', {'name': 'authenticity_token'})['value'],
        'previous_step': 'payment_method',
        'step': '',
        's': '',
        #'c': form.find('input', {'name': 'c'})['value'],
        #'d': form.find('input', {'name': 'd'})['value'],
        'checkout[payment_gateway]': form.find('input', {'name': 'checkout[payment_gateway]'})['value'],
        'checkout[credit_card][number]': cardnumber,
        'checkout[credit_card][name]': firstname + ' ' + lastname,
        'checkout[credit_card][month]': cardexpmonth.strip('0'),
        'checkout[credit_card][year]': cardexpyear,
        'expiry': cardexpmonth + ' / ' + cardexpyear[-2:],
        'checkout[credit_card][verification_value]': cvv,
        'checkout[different_billing_address]': 'false',
        'checkout[buyer_accepts_marketing]': '0',
        'complete': '1',
        'checkout[client_details][browser_width]': '1280',
        'checkout[client_details][browser_height]': '728',
        'checkout[client_details][javascript_enabled]': '1'
        }

    # Submitting Payment Method
    #r3 = session.post(website+form2['action'], data=payload2, headers=headers)
    print("Submitted payment method: " + str(time.time() - t0) + 's')





