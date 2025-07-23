from pydantic import BaseModel, Field
from typing import Optional, Any
from fastapi.responses import JSONResponse
from fastapi import HTTPException, status as http_status 

class BaseResponse(BaseModel):
    status: str = Field(..., example="success", description="Response status (e.g., 'success', 'fail').")
    message: Optional[str] = Field(..., example="Data retrieved successfully.", description="Response message.")
    data: Optional[Any] = Field(None, description="Response data.")
    error: Optional[str] = Field(None, description="Error message.")
    
    @classmethod
    def success_response(cls, message: str, data: Optional[Any] = None)-> 'BaseResponse':
        return cls(status="success", message=message, data=data, error="")
    
    @classmethod
    def fail_response(cls, message: str, error: Optional[str] = None)-> 'BaseResponse':
        return cls(status="fail", message=message, data={}, error=error)
    
    def to_json_response(self, status_code:int = http_status.HTTP_200_OK )-> JSONResponse:
        return JSONResponse(
            status_code = status_code,
            content = self.model_dump()
        )
        
    @classmethod
    def raise_exception(cls, status_code:int, message: str, error: str = None):
        error_response = cls.fail_response(message = message, error = error).model_dump()
        raise HTTPException(
            status_code = status_code,
            detail = error_response
        )