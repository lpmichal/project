import security
import tables
import connexion
from connexion.resolver import RestyResolver

# Create the flask app
app = connexion.FlaskApp('project')
app.add_api('api.yml', resolver=RestyResolver('api'))
app.run(port=8080)

# HTTP Codes
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


'''
    Creates a user from the given user spec
'''
@app.route('/create')
def create(username, password, email):

    try:
        tables.create_user(username, password, email)
        return 'OK', '200', {'x-message': 'New user successfully created'}
    except Exception as e:
        print(str(e))
        return 'Internal Server Error', '500', {'x-message': str(e)}