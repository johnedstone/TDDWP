from django.conf import settings
from .base import FunctionalTest
from .server_tools import create_session_on_server
from .management.commands.create_session import create_pre_authenticated_session

from django.contrib.auth import (
    BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
)
# User = get_user_model()

from django.contrib.sessions.backends.db import SessionStore


class MyListsTest(FunctionalTest):

    def create_pre_authenticated_session(self, email):
        # user = User.objects.create(email=email)
        if self.against_staging:
            session_key = create_session_on_server(self.server_host, email)
        else:
            session_key = create_pre_authenticated_session(email)

        ## to set a cookie we need to first visit the domain.
        ## 404 pages load the quickest!
        self.browser.get(self.server_url + "/404_no_such_url/")
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session.session_key,
            path='/',
        ))

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        email = 'edith@@example.com'

        self.browser.get(self.server_url)
        self.wait_to_be_logged_out(email)

        # Edith is a lgged-in user
        #self.create_pre_authenticate_session(email)

        #self.browser.get(self.server_url)
        #self.wait_to_be_logged_in(email)