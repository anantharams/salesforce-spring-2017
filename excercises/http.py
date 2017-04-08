import requests
from bs4 import BeautifulSoup


def scrape_channels():
    """
    Scrape the numeric frequencies from the "Midland Extra Channels" table on the 
    URL given. 

    Do not include the header row cell value.

    @return list of floats

    Test with:
        py.test tests/test_http.py
    """
    url = "http://wiki.radioreference.com/index.php/FRS/GMRS_combined_channel_chart"
    return None