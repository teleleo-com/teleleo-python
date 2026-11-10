"""Send an SMS from a modem and handle the errors the API can answer with.

export TELELEO_API_KEY=...
python examples/send_sms.py 1234 +447700900123 "Hello from Teleleo"
"""

import sys

import teleleo
from teleleo import Teleleo

dongle_id, number, message = int(sys.argv[1]), sys.argv[2], sys.argv[3]
client = Teleleo()

try:
    sms = client.sms.send(dongle_id, number=number, message=message)
except teleleo.NotFoundError:
    sys.exit(f"Modem {dongle_id} is not in this account")
except teleleo.BadRequestError as e:
    sys.exit(f"Not sent: {e.error_message} {e.error_details}")

# sms_status_id SENT means the mobile network accepted the SMS, not that the handset received it.
print(f"SMS {sms.sms_id} created, status {sms.sms_status_id!r}")
