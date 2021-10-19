import gnupg
import json

gpg = gnupg.GPG()

with open("log.txt") as f:
    data = f.read()

data = [d  + "-----END PGP MESSAGE-----" for d in (d.strip() for d in data.split("-----END PGP MESSAGE-----")) if d]

print("event,report-time,event-time")
for txt in data:
    entry = {"event": "", "report-time": "", "event-time": ""}
    entry.update(json.loads(str(gpg.decrypt(txt))))
    print("%(event)s,%(report-time)s,%(event-time)s" % entry)
