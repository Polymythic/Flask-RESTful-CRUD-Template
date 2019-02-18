# Allows for safer string comparison
from werkzeug.security import safe_str_cmp

# Include necessary model (in this case, the user)
from models.user import UserModel

# Authenticate if username and password match
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

# Find the identity of the user based 'identity' field in the payload
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
