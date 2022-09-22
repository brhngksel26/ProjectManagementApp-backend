from project_management.model.auth import Auth


def get_username_id(username):
    return Auth.objects.filter(username=username).first().id