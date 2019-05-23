
def generete_full_url(request):

    absolute_uri = request.build_absolute_uri()
    full_path = request.get_full_path()

    host_protocol = str(absolute_uri).replace(str(full_path),"")

    return str(host_protocol)


