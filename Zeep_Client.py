from zeep import Client
# import my

soap_client = Client(wsdl='http://127.0.0.1:8000/soap_service/?WSDL')

print ('Function hello: ', soap_client.service.hello('SoapAPI'))
print ('Function sum: ', soap_client.service.sum(30, 20))
