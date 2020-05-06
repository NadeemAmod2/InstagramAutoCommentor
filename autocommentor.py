# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

session = InstaPy(username='xxxxxxx', password='xxxxxxx', headless_browser=True)

with smart_run(session):
	session.set_dont_include(["quarantinecurls"])	# ignore himself
	session.set_ignore_users(["quarantinecurls"])	# ignore himself
	session.like_by_tags(["quarantinecurls"], amount=30)
