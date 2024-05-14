from datetime import datetime, timedelta

hora_atual = datetime.now()

duracao = timedelta(hours=2)

nova_hora = hora_atual - duracao

print("Hora atual:", hora_atual)
print("Nova hora após subtrair 2 horas:", nova_hora)
