from apis.translation.models import Project


class ProjectMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        project_code = request.GET.get('project', None)
        project = Project.objects.filter(code=project_code).first()
        setattr(request, 'project', project)
        response = self.get_response(request)
        return response
