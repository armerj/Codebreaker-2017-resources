import base64, pickle, hmac

def cookie_decode(data, key):
    if cookie_is_encoded(data):
        sig, msg = data.split(tob('?'), 1)
        if _lscmp(sig[1:], base64.b64encode(hmac.new(tob(key), msg).digest())):
            return pickle.loads(base64.b64decode(msg))

def tob(s, enc='utf8'):
    if isinstance(s, unicode):
        return s.encode(enc)
    return bytes(s)

def cookie_is_encoded(data):
    """ Return True if the argument looks like a encoded cookie."""
    return bool(data.startswith(tob('!')) and tob('?') in data)

def _lscmp(a, b):
    """ Compares two strings in a cryptographically safe way:
    Runtime is not affected by length of common prefix. """
    return not sum(((0 if x == y else 1) for x, y in zip(a, b))) and len(a) == len(b)

def get_cookie(key, default=None, secret=None):
    """ Return the content of a cookie. To read a `Signed Cookie`, the
        `secret` must match the one used to create the cookie (see
        :meth:`BaseResponse.set_cookie`). If anything goes wrong (missing
        cookie or wrong signature), return a default value. """
    value = cookies.get(key)
    if secret and value:
        dec = cookie_decode(value, secret)
        if dec and dec[0] == key:
            return dec[1]
        return default
    return value or default

def set_cookie(name, value, secret=None, **options):
    if not _cookies:
        _cookies = SimpleCookie()
    if secret:
        value = touni(cookie_encode((name, value), secret))
    else:
        if not isinstance(value, basestring):
            raise TypeError('Secret key missing for non-string Cookie.')
    if len(value) > 4096:
        raise ValueError('Cookie value to long.')
    _cookies[name] = value
    for key, value in options.items():
        if key == 'max_age' and isinstance(value, timedelta):
            value = value.seconds + value.days * 24 * 3600
        if key == 'expires':
            if isinstance(value, (datedate, datetime)):
                value = value.timetuple()
            else:
                if isinstance(value, (int, float)):
                    value = time.gmtime(value)
            value = time.strftime('%a, %d %b %Y %H:%M:%S GMT', value)
        _cookies[name][key.replace('_', '-')] = value

secret='0D484BE84C22C94E72A7DE327FA0B2FB'
file_cookie = open('file_cookie', 'rb')
data = file_cookie.read()

print cookie_decode(data, secret)