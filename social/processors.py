from .models import Link

def ctx_dict(request):
    links = Link.objects.all()
    ctx = {link.key: link.url for link in links}
    return ctx
