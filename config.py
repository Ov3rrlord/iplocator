class Auth:
    
    """
    This class is used to store the API keys for the main code
    """    
    def __init__(self, api:None, ipinfoapi:None):
        self.api = api
        self.ipinfoapi = ipinfoapi


# You will need to provide your api key by creating an account on https://www.geoapify.com/
auth = Auth(api="YOUR API KEY HERE", ipinfoapi=None)

# You will need to provide your api key by creating an account on https://ipinfo.io/
auth2 = Auth(api=None, ipinfoapi="YOUR API KEY HERE")
