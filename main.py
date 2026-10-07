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
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    print("EMBER CALC | Твое выгорание")
    print("Отвечай 0-10")
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    print()

    scores = {}
    scores["workload"] = ask("Рабочая нагрузка \n 0 = свободен, 10 = завал")
    scores["resilience"] = ask("Устойчивость \n 0 = совсем не справляюсь, 10 = легко")
    scores["sleep_problems"] = ask("Проблемы со сном \n 0 = сплю отлично, 10 = почти не сплю")
    scores["social_contact"] = ask("Поддержка близких \n 0 = совсем один, 10 = полная поддержка")
    scores["mood_pos"] = ask("Позитивные эмоции \n 0 = почти не было, 10 = часто")
    scores["mood_neg"] = ask("Негативные эмоции \n 0 = нет негатива, 10 = часто")

    percent, details = calc_risk(scores)
    level, advice = risk_lev(percent)

    print()
    print("~~~~~~~~~~~~~~~~~~~~")
    print("Риск выгорания:", str(percent) + "%")
    print("Уровень:", level)
    print("Совет:", advice)
    print("~~~~~~~~~~~~~~~~~~~~")
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
