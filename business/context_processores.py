
from .models import Business 
def extras(request):
    business = Business.objects.first()
    return {'business': business}