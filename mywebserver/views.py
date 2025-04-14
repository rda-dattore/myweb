from django.http import HttpResponse


def show_version(request):
    with open("/usr/local/myweb/version_number") as f:
        version_number = f.read()

    return HttpResponse(version_number)
