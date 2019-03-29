import os
import time
import jwt
from authorization_django.config import settings as middleware_settings


def make_token():
    jwks = middleware_settings()['JWKS'].signers
    assert len(jwks) > 0
    (kid, key), = jwks.items()

    now = int(time.time())

    token_default = jwt.encode({
        'scopes': ['SIG/ALL'],
        'iat': now, 'exp': now + 31536000, # One year
        'sub':'acceptatie@sigmax.nl'
    }, key.key, algorithm=key.alg, headers={'kid': kid})

    return str(token_default, 'utf-8')


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    t = make_token()
    print(t)
    print(jwt.decode(t, verify=False))
