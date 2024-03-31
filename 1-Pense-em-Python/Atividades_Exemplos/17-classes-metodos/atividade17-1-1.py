"""
Como exercício, reescreva time_to_int (de “Prototipação versus planejamento”,
na página 234) como um método. Você pode ficar tentado a reescrever int_to_time
como um método também, mas isso não faz muito sentido porque não haveria
nenhum objeto sobre o qual invocá-lo.
"""

import copy


class Time:
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds


time = Time()
time.hour = 11
time.minute = 47
time.second = 30

timet2 = copy.deepcopy(time)
time.hour = 10
time.minute = 27
time.second = 50

print(f"{time.hour}:{time.minute}:{time.second}")
print(time.time_to_int())
print(timet2.time_to_int())
