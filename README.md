# SpamAssassin Client python module
This is a python wrapper for SpamAssissin's SPAMC deamon. It provides these funtions:
* get_score(float) - final score from spamassasin
* get_fulltext(string) - full report as string from SpamAssasin deamon
* get_report_json(json) - full report as JSON from SpamAssasin deamon


# Instalation

Install SpamAssassin

	sudo apt get spamassassin

Pytest needs to be installed to run tests

	sudo apt install python-pytest

Use PIP package manager to install this module

	pip install spamassassin_client



# Example

Module can be used in following way:

	import os

	from spamassassin_client import SpamAssassin

	FILES = [dict(type='spam', name='sample-spam.txt'),
		 dict(type='ham', name='sample-nonspam.txt')]

	def main():

	    path = os.path.dirname(__file__)
	    for test in FILES:
		filename = os.path.join(path, test['name'])
		with open(filename,"rb") as f:            
		    print("\nProcessing file: {}".format(filename))
		    assassin = SpamAssassin(f.read())
		    print(assassin)
		    if assassin.is_spam():
		        print("The received message is considered spam with a score of {0}".format(assassin.get_score()))
		    print('\nreport_fulltext:', assassin.get_fulltext())
		    print('score:', assassin.get_score())
		    print('report_json:', assassin.get_report_json())

	if __name__ == "__main__":
	    main()


# Run tests

	pytest -v

