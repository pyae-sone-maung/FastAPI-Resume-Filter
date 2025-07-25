from fastapi import HTTPException, status

class APIError(HTTPException):
    def __init__(self, status_code: int, message: str):
        super().__init__(status_code = status_code, detail=message)
        self.message = message
        self.status_code = status_code