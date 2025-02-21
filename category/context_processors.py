from .models import Category


def menu_links(request):
    # context proceesor configure it in setting.py(templates)
    # fectching the categories form the database
    
    links = Category.objects.all()
    return dict(links=links)