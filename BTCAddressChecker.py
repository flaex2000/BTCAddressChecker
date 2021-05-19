import mailbox
import re
from cryptoaddress import BitcoinAddress

def btc_test(email_body):
    btc_addresses = re.findall(r"(?:[13]{1}[a-km-zA-HJ-NP-Z1-9]{26,33}|bc1[a-z0-9]{39,59})", email_body)
    for btc_address in btc_addresses:
        try:
            test_btc_address = BitcoinAddress(btc_address, network_type='mainnet')
            print (message['Date'] + "#" + message['From']+ "#" + message['To'] + "#" + str(test_btc_address))
        except ValueError:
            next

for message in mailbox.mbox('mailbox'):
    if message.is_multipart():
        for part in message.get_payload():
            body = str(part.get_payload(decode=True))
            btc_test(body)
    else:
        body = str(message.get_payload(decode=True))
        btc_test(body)