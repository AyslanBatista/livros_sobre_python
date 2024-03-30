"""
Como exercício, escreva uma versão correta de increment que não contenha loops.
"""


def increment(time, seconds):
    time.second += seconds
    if time.second >= 60:
        minutes, seconds = divmod(time.second, 60)
        time.second -= 60 * minutes
        time.second += seconds
        time.minute += minutes
    if time.minute >= 60:
        hour,  minutes = divmod(time.minute, 60)
        time.minute -= 60 * hour
        time.minute += minutes
        time.hour += hour
