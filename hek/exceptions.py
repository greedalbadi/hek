class SiteHostNameRequestError(LookupError):
    """Request host name error"""

class LengthError(ValueError):
    """ length error exception """
class ProxyFailed(ConnectionRefusedError):
    """ Proxy failed to connect """