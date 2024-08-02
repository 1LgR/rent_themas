from .models import *
import datetime
import calendar
from django.shortcuts import get_object_or_404

class  CalcDesconto():
    def calculardesconto(self, date, tema, client):
        desconto_dia = 0
        desconto_cliente = 0
        tema = get_object_or_404(Theme, pk = tema)
        cliente = Rent.objects.filter(client = client).exists()

        date_em_datetime = datetime.datetime.strptime(date, "%Y-%m-%d")
        if not date_em_datetime.isoweekday() > 4:
            desconto_dia = tema.price * 0.40

        for aluguel in Rent.objects.all():
            if aluguel.client == cliente:
                desconto_cliente = tema.price * 0.1

        valor_total = tema.price - (desconto_cliente + desconto_dia)

        return valor_total