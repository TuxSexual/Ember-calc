FACTORS = {
    "workload": (0.678, -1), 
    "resilience": (0.595, +1),
    "sleep_problems": (0.39, -1),
    "social_contact": (0.30, +1),
    "mood_pos": (0.30, +1),
    "mood_neg": (0.30, -1)
}

maxrisk = sum(w for w, d in FACTORS.values())
