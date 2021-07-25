# medlog

MedLOG is a medical logging tool. It provides a web based UI with a set of buttons. Pressing one of them,
logs the button name and the time to a file encrypted using GPG.

## Running

    export MEDLOG_KEY=user@example.com
    python app.py

You should run this software behind an nginx / apache that terminates SSL / HTTPS. Do not run over plain HTTP or a man-in-the-middle attack
could make all the encryption pointless.
