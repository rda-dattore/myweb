import os
import subprocess

from django.http import HttpResponse

def df(request):
    o = subprocess.run("/usr/bin/df", shell=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    err = o.stderr.decode("utf-8")
    if len(err) > 0:
        return HttpResponse("ERROR: " + str(err))

    return HttpResponse(o.stdout.decode("utf-8").replace("\n", "<br>"))


def root_ls(request):
    o = subprocess.run("/usr/bin/ls -lt /", shell=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    err = o.stderr.decode("utf-8")
    if len(err) > 0:
        return HttpResponse("ERROR: " + str(err))

    return HttpResponse(o.stdout.decode("utf-8").replace("\n", "<br>"))


def glade_ls(request):
    o = subprocess.run("/usr/bin/ls -lt /glade/campaign/collections/rda/work/dattore/cfsr/cfs_oper/", shell=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    err = o.stderr.decode("utf-8")
    if len(err) > 0:
        return HttpResponse("ERROR: " + str(err))

    return HttpResponse(o.stdout.decode("utf-8").replace("\n", "<br>"))


def write_data(request):
    try:
        with open("/data/test2.txt", "w") as f:
            f.write("data test ABC")
            
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


def data_ls(request, path):
    o = subprocess.run("/usr/bin/ls -lt " + os.path.join("data", path), shell=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    err = o.stderr.decode("utf-8")
    if len(err) > 0:
        return HttpResponse("ERROR: " + str(err))

    return HttpResponse(o.stdout.decode("utf-8"))


def glade_cp(request, path):
    pass
