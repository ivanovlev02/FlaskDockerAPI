from flask import jsonify
from typing import Union


class HttpError(Exception):
# позволяет передавать полезную информацию об ошибке
    def __init__(self, status_code: int, message: Union[str, list, dict]):
        self.status_code = status_code
        self.message = message


# генерирует ответ для пользователя на основании ошибки
def error_handler(error: HttpError):
    response = jsonify({'status': 'error', 'message': error.message})
    response.status_code = error.status_code
    return response



