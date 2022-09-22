from project_management.applications.slack import Slack
from project_management.model.cards import Card
from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/card_trigger", tags = ["Trigger"])
async def trigger_card():
    data_list = (Card.objects.filter(created_time__lte = datetime.now))

    for data in data_list:
        message = f"{data.description} finished time has passed but still not finished"

        slack = Slack()
        await slack.send_message(message)

    return