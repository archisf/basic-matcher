from djangorestframework_camel_case.util import camelize
from rest_framework import status
from rest_framework.exceptions import APIException


class BaseBMException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    title = None
    text = 'Not Found'

    def __init__(self, detail=None, title=None, text=None):
        self.title = title or self.title
        self.text = text or self.text
        if detail is None:
            self.detail = self.default_detail

    @property
    def default_detail(self):
        return {
            'title': self.title,
            'text': self.text
        }


class BMNoContent(BaseBMException):
    status_code = status.HTTP_204_NO_CONTENT


class BMBadRequest(BaseBMException):
    status_code = status.HTTP_400_BAD_REQUEST
    title = 'Invalid input parameters'

    def __init__(self, errors=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if errors is not None:
            if isinstance(errors, dict):
                errors = [errors]
            for error in camelize(errors):
                self.detail.update(error)
