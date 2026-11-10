"""Print the SMS received in the last 24 hours, newest first.

export TELELEO_API_KEY=...
python examples/incoming_sms.py
"""

from datetime import datetime, timedelta, timezone

from teleleo import Teleleo
from teleleo.types import SmsType

client = Teleleo()
since = datetime.now(timezone.utc) - timedelta(hours=24)

for sms in client.sms.list(sms_type_ids=[SmsType.INCOMING], from_=since, limit=100):
    print(f"{sms.created_at:%Y-%m-%d %H:%M}  {sms.number_caller:<16} {sms.message_decoded}")
