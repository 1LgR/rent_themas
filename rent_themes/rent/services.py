from .models import Theme, Rent
import datetime
from django.shortcuts import get_object_or_404

class CalcDesconto():
    def calculardesconto(self, date, tema_id, client_id):
        tema = get_object_or_404(Theme, pk=tema_id)
        cliente_ja_alugou = Rent.objects.filter(client_id=client_id).exists()

        date_em_datetime = datetime.datetime.strptime(date, "%Y-%m-%d")

        if 2 <= date_em_datetime.isoweekday() <= 4:
            desconto_dia = tema.price * 0.40
        else:
            desconto_dia = 0

        if cliente_ja_alugou:
            desconto_cliente = tema.price * 0.10
        else:
            desconto_cliente = 0

        valor_total = tema.price - (desconto_cliente + desconto_dia)

        return valor_total
