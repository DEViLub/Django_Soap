from suds.client import Client
from suds.cache import NoCache

my_client = Client('http://127.0.0.1:8000/soap_service/?WSDL', cache=NoCache())
print (my_client)
print ('Function hello: ', my_client.service.hello('Vinay'))
print ('Function sum: ', my_client.service.sum(30, 20))