from calculator import calc_risk, risk_lev

def test_worst():
    scores = {
        "workload": 10,
        "resilience": 0,
        "sleep_problems": 10,
        "social_cont": 0,
        "mood_pos": 0,
        "mood_neg": 10,
    }
    percent, _ = calc_risk(scores)
    print("Worst:", percent)

def test_best():
    scores = {
        "workload": 0,
        "resilience": 10,
        "sleep_problems": 0,
        "social_cont": 10,
        "mood_pos": 10,
        "mood_neg": 0,
    }
    percent, _ = calc_risk(scores)
    print("Best:", percent)

def test_mid():
    scores = {k: 5 for k in [
        "workload", "resilience", "social_cont", "mood_pos", "mood_neg"
    ]}
    percent, _ = calc_risk(scores)
    print("Middle:", percent)

def test_levels():
    print(risk_lev(20)[0])
    print(risk_lev(45)[0])
    print(risk_lev(80)[0])

if __name__ == "__main__":
    test_worst()
    test_best()
    test_mid()
    test_levels()
