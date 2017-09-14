from rest_framework import permissions


class UpdateOwnAnimal(permissions.BasePermission):
    '''Allow user to update their own statue'''

    def has_object_permission(self, request, view, obj):
        '''Checks the user is trying to update their own pet'''
        if request.method == 'POST':
            return True
        return obj.owner == request.user
