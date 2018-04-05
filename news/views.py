from django.shortcuts import render, redirect
import math
import requests
requests.packages.urllib3.disable_warnings()

from bs4 import BeautifulSoup
from datetime import timedelta, timezone, datetime
import os
import shutil

from .models import Headline, UserProfile


def scrape(request):
	user_p = UserProfile.objects.filter(user=request.user).first()
	user_p.last_scrape = datetime.now(timezone.utc)
	user_p.save()

	session = requests.Session()
	session.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"}
	url = 'https://www.theonion.com/'

	content = session.get(url, verify=False).content

	soup = BeautifulSoup(content, "html.parser")

	posts = soup.find_all('div',{'class':'curation-module__item'}) # returns a list

	for i in posts:
		link = i.find_all('a',{'class':'js_curation-click'})[1]['href']
		title = i.find_all('a',{'class':'js_curation-click'})[1].text
		image_source = i.find('img',{'class':'featured-image'})['data-src']

		# stackoverflow solution

		media_root = '/Users/matthew/Downloads/dashboard/media_root'
		if not image_source.startswith(("data:image", "javascript")):
			local_filename = image_source.split('/')[-1].split("?")[0]
			r = session.get(image_source, stream=True, verify=False)
			with open(local_filename, 'wb') as f:
				for chunk in r.iter_content(chunk_size=1024):
					f.write(chunk)

			current_image_absolute_path = os.path.abspath(local_filename)
			shutil.move(current_image_absolute_path, media_root)


		# end of stackoverflow

		new_headline = Headline()
		new_headline.title = title
		new_headline.url = link
		new_headline.image = local_filename
		new_headline.save()

	return redirect('/home/')

