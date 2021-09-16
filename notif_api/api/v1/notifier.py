import logging


from fastapi import APIRouter, Depends

from models.email import Email
from services.email import get_email_service, EmailService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/email/send/",
            summary="Отправить письмо.",
            )
async def send_email(
        email_data: Email,
        service: EmailService = Depends(get_email_service),
) -> None:
    await service.send(email_data)


