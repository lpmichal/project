import mysql.connector
import tables

'''
    Module responsible for handling security operations
'''
class Security(object):


    '''
        Ensures the database exists with the proper tables
    '''
    @staticmethod
    def _ensure_database():
        ready = False
        if len(cursor.execute('SHOW DATABASES LIKE {}'.format('project'))) > 0:
            ready = True

        if not ready:
            tables.construct(cursor)
        return ready

    '''
        Determines if a user is authenticated or not
    '''
    @staticmethod
    def authenticate(username, password):

        authenticated = False
        _ensure_database()

        query = ("SELECT username, password FROM project "
         "WHERE username={} and password={}").format(username, password)

        result = cursor.execute(query)
        if (len(result) != 0):
            authenticated = True
        
        return authenticated
