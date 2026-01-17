from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional as optional

class postbasse(BaseModel):
    title: str
    content: str
    publisher : bool = True

class createpost(postbasse):
    pass

class userout(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True



class post(BaseModel):
    id: int
    title: str
    content: str
    publisher : bool = True
    created_at: datetime
    owner_id: int
    owner: userout

    class Config:
       from_attributes = True

class postvote(BaseModel):
    Post: post
    votes: int

    class Config:
       from_attributes = True

class userbase(BaseModel):
    email: EmailStr
    password: str 

    class Config:
        from_attributes = True

class userlogin(BaseModel):
    email: EmailStr
    password: str 
    
class token(BaseModel):
    access_token: str
    token_type: str

class tokenData(BaseModel):
    id: optional[int] = None

class vote(BaseModel):
    post_id: int
    dir: int  