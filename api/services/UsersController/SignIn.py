import psycopg2
from rest_framework import status
from rest_framework.response import Response
import re
from django.contrib.auth.hashers import check_password
from api.database.DatabaseController import DatabaseController


class UserSignIn:
    def __init__(self,username,password):

        self.username_or_email = username
        self.password = password

    def exists_user(self):

        email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
        email = email_pattern.fullmatch(self.username_or_email)

        if email:
            sql_password = "SELECT password FROM users.authenticate WHERE email = %s;"
        else:
            sql_password = "SELECT password FROM users.authenticate WHERE username = %s;"
        try:
            controller = DatabaseController()
            controller.connection_database()
            db_password = controller.exec_select_sql_one_register(sql=sql_password,
                                                                  values=(self.username_or_email,)) 
            controller.close_connection()
            if db_password is None:
                return Response({'message': 'User does not exist'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                if check_password(self.password, db_password[0]):
                    return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'User, email or password invalid'}, status=status.HTTP_404_NOT_FOUND)
                    
        except TypeError as error:
            return Response({'message':f'error server: {error}'},status=500)