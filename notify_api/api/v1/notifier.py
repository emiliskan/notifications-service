import logging

from fastapi import APIRouter, Depends

from models import Message
from services.message import get_message_service, MessageService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/send/",
             summary="Отправить сообщение.")
async def send(
        message: Message,
        service: MessageService = Depends(get_message_service),
) -> None:
    await service.send(message)
