import subprocess

from django.http import HttpResponse

def df(request):
    pass


def root_ls(request):
    pass


def write_data(request):
    try:
        with open("/data/test.txt", "w") as f:
            f.write("data test 18801938234")
            
    except Exception as err:
        return HttpResponse("There was an error: " + str(err))

    return HttpResponse("good job!")

def show_version(request):
    with open("/usr/local/gdexweb/version_number") as f:
        version_number = f.read()

    return HttpResponse(version_number)


def php(request, script):
    o = subprocess.run("/usr/bin/php /usr/local/gdexweb/" + script, shell=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    err = o.stderr.decode("utf-8")
    if len(err) > 0:
        return HttpResponse("ERROR: " + str(err))

    return HttpResponse(o.stdout.decode("utf-8"))
