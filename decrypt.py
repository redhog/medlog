import gnupg

gpg = gnupg.GPG()

with open("log.txt") as f:
    data = f.read()

data = [d  + "-----END PGP MESSAGE-----" for d in (d.strip() for d in data.split("-----END PGP MESSAGE-----")) if d]

data = [str(gpg.decrypt(d)) for d in data]

for entry in data:
    print(entry)
