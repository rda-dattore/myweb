import subprocess

from django.http import HttpResponse


def show_version(request):
    with open("/usr/local/myweb/version_number") as f:
        version_number = f.read()

    return HttpResponse(version_number)


def php(request, script):
    o = subprocess.run("/usr/bin/php /usr/local/myweb/" + script, shell=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    err = o.stderr.decode("utf-8")
    if len(err) > 0:
        return HttpResponse("ERROR: " + str(err))

    return HttpResponse(o.stdout.decode("utf-8"))
