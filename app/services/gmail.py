import smtplib
from email.message import EmailMessage

from fastapi.exceptions import HTTPException

from app.config import settings


async def send_mail(emails: list, content: str):
    try:
        msg = EmailMessage()
        msg["Subject"] = "Advertisement"
        msg["From"] = settings.EMAIL_HOST_USER
        msg["To"] = emails
        msg.add_alternative(content, subtype="html")
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, 465) as smtp:  # type: ignore
            smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)  # type: ignore
            smtp.send_message(msg)
        settings.logger.info(f'Email successfully send: TO: {emails}')
    except Exception:
        # TODO ask and update status code
        raise HTTPException(status_code=409)
