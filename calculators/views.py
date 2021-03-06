import base64
import numexpr
from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Equation

class EquationCreate(APIView):

    @staticmethod
    def decode_message(encoding):
        encoding_bytes = encoding.encode('utf8')
        decode_bytes = base64.b64decode(encoding_bytes)
        decode_msg = decode_bytes.decode('utf8')

        return decode_msg

    @staticmethod
    def calculate(equation):
        solution = numexpr.evaluate(equation).item()
        solution = round(solution, 3)
        return str(solution)
    
    @staticmethod
    def create(encoding, equation, solution):
        Equation.objects.create(
            encoding = encoding,
            equation = equation,
            result = solution
        )
        return

    def get(self, request):
        try:
            # get encoding from query parameter
            encoding = request.query_params["uery"]
            # decode the encoding message
            equation = self.decode_message(encoding)
            # calculate the decoded equation
            solution = self.calculate(equation)
            # add equation and solution to db
            self.create(encoding, equation, solution)
            # return response with result
        except:
            error = True
            message = "Invalid request"
        else:
            error = False
            result = solution
        
        if error == True:
            response_message = {'error': error, 'message': message}
            status_code = status.HTTP_400_BAD_REQUEST
        else:
            response_message = {'error': error, 'result': result}
            status_code = status.HTTP_200_OK

        return Response(data=response_message, status=status_code)