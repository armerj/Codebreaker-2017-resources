import base64, hmac, pickle

def tob(s, enc='utf8'):
    if isinstance(s, unicode):
        return s.encode(enc)
    return bytes(s)

def cookie_encode(data, key):
    """ Encode and sign a pickle-able object. Return a (byte) string """
    msg = base64.b64encode(pickle.dumps(data, -1))
    sig = base64.b64encode(hmac.new(tob(key), msg).digest())
    return tob('!') + sig + tob('?') + msg

cookie_secret='0D484BE84C22C94E72A7DE327FA0B2FB' # from servercfg.py
cookie_name_value='True'

print cookie_encode(cookie_name_value, cookie_secret)