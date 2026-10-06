from factors import FACTORS, maxrisk

def calc_risk(scores):
    total = 0.0
    details = {}

    for name, (weight, direction) in FACTORS.items():
        val = scores.get(name, 5) / 10.0

        if direction > 0:
          part = (1 - val) * weight
        else:
            part = val * weight
        
        total += part
        details[name] = part

    percent = round((total / maxrisk) * 100)
    return percent, details

def risk_lev(percent):
    if percent < 35:
        return "Низкий", "Состояние стабильно"
    if percent < 60:
        return "Умеренный", "Обрати внимание на сон и нагрузку"
    return "Высокий", "Стоит отдохнуть"
