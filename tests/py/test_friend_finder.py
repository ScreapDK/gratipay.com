from __future__ import print_function, unicode_literals

from aspen import json
from gratipay.testing import Harness

class TestFriendFinder(Harness):
	def test_twitter_get_friends_for(self):
		elsewhere = self.make_elsewhere('twitter', 23608307, 'Changaco')
		friends, nfriends, pages_urls = self.platforms['twitter'].get_friends_for(elsewhere)
		assert nfriends > 0

	def test_github_get_friends_for(self):
		elsewhere = self.make_elsewhere('github', 134455, 'whit537')
		friends, nfriends, pages_urls = self.platforms['github'].get_friends_for(elsewhere)
		assert nfriends > 0
