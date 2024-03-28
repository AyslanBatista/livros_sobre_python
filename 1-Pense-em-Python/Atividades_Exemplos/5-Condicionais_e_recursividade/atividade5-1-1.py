"""
Escreva um script que leia a hora atual e a converta em um tempo
em horas, minutos e segundos, mais o número de dias desde a época.
"""

import time

tempo_atual = time.time()


dias = int(tempo_atual // (24 * 3600))
horas = int((tempo_atual % (24 * 3600)) // 3600)
minutos = int((tempo_atual % (3600)) // 60)
segundos = int(tempo_atual % 60)

print(dias, horas, minutos, segundos)
