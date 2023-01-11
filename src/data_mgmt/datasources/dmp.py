from zeep import Client
from zeep.wsse.username import UsernameToken
from zeep.wsse.signature import Signature


class JupiterXL:

    private_key_filename = ""
    public_key_filename = ""
    optional_password = ""

    def __init__(self, dmp_user, pwd ):
        wsdl_url = "http://data.geus.dk/miljoeportal.pcjupiterxl.1.0/PCJupiterXL?wsdl"
        user_name_token = UsernameToken('dmp_user', 'pwd')
        signature = Signature(self.private_key_filename, self.public_key_filename, self.optional_password)
        self.client = Client(wsdl_url, wsse=[user_name_token, signature])

    def get_borehole(self, dgunr):
        pass

class Bboringer:

    private_key_filename = ""
    public_key_filename = ""
    optional_password = ""

    def __init__(self, dmp_user, pwd ):
        wsdl_url = "http://webs.geus.dk/miljoeportal.groundwater.b-boring.2.0.0/B-Boring?wsdl"
        user_name_token = UsernameToken('dmp_user', 'pwd')
        signature = Signature(self.private_key_filename, self.public_key_filename, self.optional_password)
        self.client = Client(wsdl_url, wsse=[user_name_token, signature])
    
    def get_bboring(dgunr):
        pass

class DKJordWS3:

    private_key_filename = ""
    public_key_filename = ""
    optional_password = ""

    def __init__(self, dmp_user, pwd ):
        wsdl_url = "http://ws.dk-jord.dk/ws/DKJordWS.svc?wsdl"
        user_name_token = UsernameToken('dmp_user', 'pwd')
        signature = Signature(self.private_key_filename, self.public_key_filename, self.optional_password)
        self.client = Client(wsdl_url, wsse=[user_name_token, signature])
