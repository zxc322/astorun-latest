def local_url_generator(url):
    if '/ru/' in url:
        return '/ru/'
    elif '/uk/' in url:
        return '/uk/'
    else:
        return '/'
