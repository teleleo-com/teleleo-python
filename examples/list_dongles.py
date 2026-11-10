"""Print the modems of the account.

export TELELEO_API_KEY=...
python examples/list_dongles.py
"""

from teleleo import Teleleo

client = Teleleo()

for dongle in client.dongles.list():
    status = "active" if dongle.is_active else "inactive"
    print(f"{dongle.dongle_id:>6}  {dongle.name:<30} {dongle.number or '-':<16} {status}")
