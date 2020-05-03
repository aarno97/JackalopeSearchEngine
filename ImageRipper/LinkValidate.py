"""
Sources:
https://stackoverflow.com/questions/16778435/python-check-if-website-exists

This program aims to validate if a link is valid.
It will return 'true' if the link is valid, it will return false if otherwise
"""
import requests


def validate(url):
    website = requests.get(url)
    if website.status_code == 200:
        return True
    else:
        return False
