import security
import connexion
from connexion.resolver import RestyResolver


app = connexion.FlaskApp('project')
app.add_api('api.yml', resolver=RestyResolver('api'))
app.run(port=8080)

HTTP_OK = 200
HTTP_FORBIDDEN = 403

'''
    Facilitates login of a user to system
'''
@app.route('/login')
def login():
    username = connexion.request.headers['X-Username']
    password = connexion.request.headers['X-Password']

    authenticated = security.authenticate(username, password)

    if authenticated:
        return 'OK', '200', {'x-message': 'User successfully authenticated'}

    else:
        return 'Forbidden', '403', {'x-message': 'User not authenticated'}