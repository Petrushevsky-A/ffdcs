from asgiref.sync import iscoroutinefunction, markcoroutinefunction

class CheckPermission:
    async_capable = True
    sync_capable = False

    def __init__(self, get_response):
        self.get_response = get_response
        if iscoroutinefunction(self.get_response):
            markcoroutinefunction(self)

    async def __call__(self, request):
        # is_superuser

        # services

        # sevices_group

        # user

        # role

        # organization structure

        if is_not_valid:
            return 
        response = await self.get_response(request)
        return response
