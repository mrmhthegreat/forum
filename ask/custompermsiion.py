from rest_framework import permissions
from rest_framework.authentication  import TokenAuthentication
class TOk(TokenAuthentication):
    keyword='',
class owner(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.add_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        return super().has_permission(request, view)
    # def has_object_permission(self, request, view, obj):
    #     request.method ==permissions.SAFE_METHODS
    #     if usr.has('appname.type_model.')
    #     return super().has_object_permission(request, view, obj)