from calculator import calc_risk, risk_lev

def ask(question):
    while True:
        try:
            val = float(input(question + " (0-10): "))
            if 0 <= val <= 10:
                return val
            print("Число от 0 до 10")
        except ValueError:
            print("Нужно число")
def main():
    print("Ember calc")
    print("Отвечай по шкале")
    print()

    scores = {}
    scores["workload"] = ask("Рабочая нагрузка")
    scores["resilience"] = ask("Устойчивость")
    scores["sleep_problems"] = ask("Проблемы со сном")
    scores["social_contact"] = ask("Соц влияние")
    scores["mood_pos"] = ask("Позитивные эмоции")
    scores["mood_neg"] = ask("Негативные эмоции")

    percent, details = calc_risk(scores)
    level, advice = risk_lev(percent)

    print()
    print("Риск выгорания:", str(percent) + "%")
    print("Уровень:", level)
    print("Совет:", advice)
    print()

    print("Вклад факторов:")
    for name, val in sorted(details.items(), key = lambda x: -x[1]):
        print(" " + name + ": " + str(round(val, 3)))

    print()
    print("Это не диагноз!")

if __name__ == "__main__":
    while True:
        main()
        again = input("Еще разок?) (y/n): ")
        if again.lower() != "y":
            break
        print()
