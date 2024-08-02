from .models import *
import datetime
import calendar

class SaveRentSE():
    def SaveRentS(self, request):
            a = Address(street = request.POST['street'],
                    number = request.POST['number'],
                    complement = request.POST['complement'], 
                    district = request.POST['district'],
                    city = request.POST['city'],
                    state = request.POST['state'] )
            a.save()
            
            r = Rent(date=request.POST['date'], 
                    start_hours=request.POST['start_hours'],
                    end_hours=request.POST['end_hours'],
                    client_id= request.POST['select_client'],
                    theme_id = request.POST['select_theme'],
                    address = a )
            return r.save()
        