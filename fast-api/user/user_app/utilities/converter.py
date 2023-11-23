from user_app.models.user_local_model import UserLocalOtput
from user_app.models.user_db_model import UserDB

def convert_from_user_db_to_local(user_db: UserDB):
    return UserLocalOtput(
                            id=user_db.id if user_db.id is not None else -1,
                            email=user_db.email if user_db.email is not None else "",
                            full_name=user_db.full_name if user_db.full_name is not None else "",
                            photo=user_db.photo if user_db.photo is not None else "",
                            description= user_db.description if user_db.description is not None else ""
                         )       