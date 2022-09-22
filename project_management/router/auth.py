
from project_management.model.auth import Auth, AuthModel
from project_management.model.account import Account, AccountModel
from fastapi import APIRouter, HTTPException, Depends
from project_management.utility.auth_handler import AuthHandler
from project_management.utility.function import get_username_id
auth_handler = AuthHandler()
router = APIRouter()

@router.post("/register", status_code=200, tags=["Auth"])
async def register(authInfo: AuthModel):
    if Auth.objects.filter(username=authInfo.username).first():
        raise HTTPException(status_code=400, detail="Username is taken")

    hashed_password = auth_handler.get_password_hash(authInfo.password)

    new_account = Auth()
    new_account.username = authInfo.username
    new_account.password = hashed_password
    new_account.save()

    return

@router.post("/login", tags=["Auth"])
async def login(auth: AuthModel):
    auth_data = Auth.objects.filter(username=auth.username).first()
    auth_input = auth.dict()

    if (auth_data is None):
        raise HTTPException(status_code=401, detail="Invalid username and/or password")
    
    if not auth_handler.verify_password(auth_input["password"], auth_data["password"]):
        raise HTTPException(status_code=401, detail="Invalid username and/or password")

    token = auth_handler.encode_token(auth_data["username"])
    return {"token": token}


@router.post("/add_account_info", tags=["Auth"])
async def add_account_info(account: AccountModel, username=Depends(auth_handler.auth_wrapper)):
    account = Account(**account.dict())
    account["auth_id"] = get_username_id(username)
    account.save()
    return 
