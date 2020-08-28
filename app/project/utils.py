def Get_Urls(request):
    url = request.build_absolute_uri()
    urls = [url, ""]
    if "?" in url:
        url_head = url[0 : url.find("?")]
        url_tail = url[url.find("?") :]
        urls = [url_head, url_tail]
    return urls
