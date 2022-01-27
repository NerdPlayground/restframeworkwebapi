from rest_framework import permissions

# allow code snippets to be visible to anyone
# ensure only the user can update and delete them
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user