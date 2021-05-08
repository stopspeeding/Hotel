# Packages used
from bs4 import BeautifulSoup
import requests

# Requests browser
headers = {'User-Agent': 'Booking'}

# URL = Booking.com Hotels
url = 'https://www.booking.com/searchresults.html?label=gen173nr-1DCAEoggI46AdIM1gEaKQCiAEBmAExuAEXyAEM2AED6AEB-AECiAIBqAIDuALZ2deEBsACAdICJDhhZTEwZmFjLTY2MzUtNGFiMS1iY2ZjLTg5NjMzZWM1YTk4ZtgCBOACAQ&sid=1daf8c85454412c422ccf303f593763e&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.html%3Flabel%3Dgen173nr-1DCAEoggI46AdIM1gEaKQCiAEBmAExuAEXyAEM2AED6AEB-AECiAIBqAIDuALZ2deEBsACAdICJDhhZTEwZmFjLTY2MzUtNGFiMS1iY2ZjLTg5NjMzZWM1YTk4ZtgCBOACAQ%3Bsid%3D1daf8c85454412c422ccf303f593763e%3Btmpl%3Dsearchresults%3Bac_click_type%3Db%3Bac_position%3D0%3Bcheckin_month%3D6%3Bcheckin_monthday%3D1%3Bcheckin_year%3D2021%3Bcheckout_month%3D6%3Bcheckout_monthday%3D2%3Bcheckout_year%3D2021%3Bclass_interval%3D1%3Bdest_id%3D20082895%3Bdest_type%3Dcity%3Bdtdisc%3D0%3Bfrom_sf%3D1%3Bgroup_adults%3D2%3Bgroup_children%3D0%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D0%3Bpostcard%3D0%3Braw_dest_type%3Dcity%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bsearch_selected%3D1%3Bshw_aparth%3D1%3Bslp_r_match%3D0%3Bsrc%3Dindex%3Bsrc_elem%3Dsb%3Bsrpvid%3D005c0c38400d0043%3Bss%3DWildwood%252C%2520New%2520Jersey%252C%2520United%2520States%3Bss_all%3D0%3Bss_raw%3DWild%3Bssb%3Dempty%3Bsshis%3D0%3Btop_ufis%3D1%26%3B&ss=Wildwood&is_ski_area=0&ssne=Wildwood&ssne_untouched=Wildwood&city=20082895&checkin_year=2021&checkin_month=6&checkin_monthday=1&checkout_year=2021&checkout_month=6&checkout_monthday=2&group_adults=3&group_children=0&no_rooms=1&sb_changed_group=1&from_sf=1'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')



# Prints hotel details
for parameter in soup.select('.sr_property_block'):
	try:
		print('+--------------------------------------------------+')
		print("Hotel name: " + parameter.select('.sr-hotel__name')[0].get_text().strip())
		print("Price: " + parameter.select('.bui-price-display__value')[0].get_text().strip())
		print("Rating: " + parameter.select('.bui-review-score__badge')[0].get_text().strip())
		print(parameter.select('.bui-review-score__text')[0].get_text().strip())

		print("URL: booking.com" + parameter.select('.hotel_name_link')[0]['href'])
		print('+--------------------------------------------------+')
	except Exception as x:
		print('')
