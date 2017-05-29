
SIMPLE Rest API for WMS

1. makemigrations
2. migrate
3. runserver

get -> domain/api/
post -> domain/api/
delete, put -> domain/api/(id)

Can be accessed via Tokens also
(eg:
requests.get('',headers={'Authorization':'Token (the token)'})
)

Examples using requests module in python


1. requests.delete('http://127.0.0.1:8000/api/2',headers = {'Authorization': 'Token 93db934493cc48e3a2b6afea07464338c35b9bae'})
2. requests.get('http://127.0.0.1:8000/api/',headers = {'Authorization': 'Token 93db934493cc48e3a2b6afea07464338c35b9bae'}).content
3. requests.put('http://127.0.0.1:8000/2',data = {'temperature': 33}, auth=('ichigo','a9789959296b'))
4. requests.delete('http://127.0.0.1:8000/1', auth = ('ichigo','a9789959296b'))
5. requests.post('http://127.0.0.1:8000/api/',data = {'temperature':40,'pressure':2000, 'humidity':74}, auth=('ichigo','a9789959296b'))

