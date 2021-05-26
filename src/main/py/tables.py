import mysql.connector

TABLES = {}

TABLES['users'] = (
    "CREATE TABLE `users` ("
    " `username` varchar(16) NOT NULL,"
    " `password` varchar(32) NOT NULL,"
    " `email` varchar(16) NOT NULL,"
    " PRIMARY KEY (`username`))"
)

'''
    Tables static class to construct fresh database if one does not exist
'''
class Tables:

    constructed = False

    @staticmethod
    def construct():

        success = True

        # Build database Schema
        try:
            cursor.execute('CREATE DATABASE {} DEFAULT CHARACTER SET {}'.
                format('project', 'utf-8'))
                
        except mysql.connector.Error as err:
            print("Database Schema count not be created")

        # Build table schema
        for table_name in TABLES:
            try:
                print("Creating table {}".format(table_name))
                cursor.execute(TABLES[table_name])

            except mysql.connector.Error as err:
                success = False
                print("Error creating table {}: {}", table_name, err.message)

        if success:
            constructed = True
            print("Database successfully created")
        else:
            print("Database Creation Failed")

        return

    @staticmethod
    def create_user(username, password, email):

        if constructed:
            cursor.execute('INSERT INTO project (username, password, email) VALUES ({}, {}, {})'.format(
                username,
                password,
                email))
        else:
            construct()
            create_user(username, password, email)