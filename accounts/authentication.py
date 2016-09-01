import requests
import sys
from accounts.models import ListUser

class PersonaAuthenticationBackend(object):

    def authenticate(self.assertion):
        # Send the assertion to Mozilla 's verifier service
        data = {'assertion': assertion, 'audience': 'localhost'}
        print('sending to mozilla', data,file=sys.stderr)
        resp = requests.post('https://verifier.login.persona.org', data=data)
        print('got', resp.content, file=sys.stderr)

        # Did the verifier resond?
        if resp.ok:
            # Parse the response
            verification_data = resp.json()

            # check if the assertion was valid
            if verification_data['status']  == 'okay':
                email = verification_data['email']
                try:
                    return self.get_user(email)
                except ListUser.DoesNotExit
                    return Listuser.objects.create(email=email)

        def get_user(self, email):
           return ListUser.objects.get(email=email)
