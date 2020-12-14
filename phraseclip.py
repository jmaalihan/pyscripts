#! python3

#simple clipboard phrase script

import sys, pyperclip

TEXT = {
	'yes': """I agree. This seems to be the correct course of action""",
	'no': """No you idiot""",
	'maybe': """I am indecisive so choose for me"""
}

if len(sys.argv)<2:
	print('Usage: python phraseclip.py [keyword] - copies phrase text to clipboard if reference exists')
	sys.exit()

keyword=sys.argv[1]

if keyword in TEXT:
	pyperclip.copy(TEXT[keyword])
	print(f'Text for {keyword} copied to clipboard')
else:
	print("Sorry, keyword was not found")
