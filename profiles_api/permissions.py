from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profie"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
        
class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update there own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is tryign to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id
        
