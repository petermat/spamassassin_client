import os, json
import socket

from spamassassin_client import SpamAssassin


FILES = [dict(type='spam', name='sample-spam.txt'),
         dict(type='ham', name='sample-nonspam.txt')]

class TestClass:
    def _init_(self):
        # SPAMC localserver - Connecting
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(timeout)
        client.connect(('127.0.0.1', 783))

        # SPAMC localserver - Sending
        client.sendall(self._build_message(message))
        client.shutdown(socket.SHUT_WR)

        # SPAMC localserver - Closing
        client.close()
        client = None

    def test_SpamA(self):
       # spamassasin funtions
       path = os.path.dirname(__file__)
       for test in FILES:
           filename = os.path.join(path, test['name'])
           with open(filename,"rb") as f:            
               assassin = SpamAssassin(f.read())
               if test['name'] == 'sample-spam.txt':
                   assert assassin.is_spam()
            
               assert len(assassin.get_fulltext()) > 50
               assert isinstance(float(assassin.get_score()), float)
               assert isinstance(dict(assassin.get_report_json()), dict)

