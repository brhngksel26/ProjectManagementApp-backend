from fastapi import APIRouter, HTTPException, Depends
from project_management.model.card_list import CardList, CardListInput
from project_management.model.project import Project
from project_management.model.cards import CardModel, Card, CommentModel, Comment
from project_management.utility.function import get_username_id
from project_management.utility.auth_handler import AuthHandler

auth_handler = AuthHandler()
router = APIRouter()

@router.get("/get_card_list", response_model=list, tags=["Card"])
def get_card_list():
    card_list = CardList.objects.all()

    output_data = []
    for card in card_list:
        _card = [card_item.to_json() for card_item in card.cards]
        _dict = {
            "project name": card.project.name ,
            "title":card.title,
            "cards" : _card,
            "id" : str(card.id)
            }
        output_data.append(_dict)

    return output_data

@router.post("/create_card_list", tags=["Card"])
def create_card_list(card_list : CardListInput, project_id ):
    project = Project.objects.filter(id=project_id).first()
    
    if not project:
        raise HTTPException(status_code=400, detail="Project Not Found")

    card_list_dict = card_list.dict()
    card_list_dict["project"] = project

    CardList(**card_list_dict).save()
    
    return

@router.post("/create_card", tags=["Card"])
def create_card(new_card_params: CardModel, card_list_id ):
    card_list = CardList.objects.get(id = card_list_id)
    if not card_list:
        raise HTTPException(status_code=400, detail="Card Not Found")

    new_card = Card(**new_card_params.dict()).save()

    if card_list["cards"] is not []:
        card_list.update(push__cards=new_card.to_dbref())
        return

    card_list["cards"] = [new_card.to_dbref()]
    card_list.save()
    return

@router.put("/add_comment", tags=["Card"])
def add_comment(new_comment: CommentModel, card_id ):
    card = Card.objects.get(id = card_id)
    if not card:
        raise HTTPException(status_code=400, detail="Card Not Found")

    new_comment = Comment(**new_comment.dict())
    card.update(push__comment=new_comment)

    return 


@router.put("/add_member", tags = ["Card"])
def add_member_in_card(card_id, username):
    card = Card.objects.get(id = card_id)
    if not card:
        raise HTTPException(status_code=400, detail="Card Not Found")

    card.update(push__members=get_username_id(username))
    return


