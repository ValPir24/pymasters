from pathlib import Path

from fastapi_mail import FastMail, MessageSchema, MessageType
from fastapi_mail.errors import ConnectionErrors
from pydantic import EmailStr

from pymasters.repository.users_repo import UserService
from pymasters.services.auth_service import create_email_token
from pymasters.settings import conf

async def send_email(email: EmailStr, host: str):
    
    try:
        token_verification = create_email_token({"sub": email})
        message = MessageSchema(
            subject="Confirm your email ",
            recipients=[email],
            template_body={"host": host, "token": token_verification},
            subtype=MessageType.html
        )

        fm = FastMail(conf)
        await fm.send_message(message, template_name="email_tamplate.html")
    except ConnectionErrors as err:
        print(err)
