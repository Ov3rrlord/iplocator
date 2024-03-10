class Auth:
    """
    This class is used to store the API keys for the main code
    """    
    def __init__(self, api):
        self.api = api


# You will need to provide your api key by creating an account on https://www.geoapify.com/
auth = Auth(api="YOUR_API_KEY")
