# Updated get_input function to offer enumerated choices

def get_input(prompt, options, fixed_choice=''):
    option_map = {chr(97 + i): (key, value) for i, (key, value) in enumerate(options.items())}  # 'a', 'b', 'c', etc.
    if (fixed_choice == ''):
        print(prompt)
        for option, (key, value) in option_map.items():
            print(f"{option}) {key}: {value}")
        choice = input("Enter your choice (a, b, c, etc.): ")
    else:
        choice = fixed_choice
    return option_map.get(choice, (None, None))[1]

# Dictionary options for user inputs (provided example options)
joy_levels = {
    "Very Positive": 0.6,
    "Positive": 0.8,
    "Neutral": 1,
    "Negative": 1.2,
    "Very Negative": 1.4
}

fatigue_levels = {
    "Not tired": 1,
    "A little tired": 1.2,
    "Somewhat tired": 1.4,
    "Very tired": 1.8,
    "Super exhausted": 2
}

experience_levels = {
    "Expert": 1,
    "Lots": 1.5,
    "Some": 2,
    "Low": 2.5,
    "None": 3
}

stress_levels = {
    "Very low": 1.4,
    "Low": 1.2,
    "Medium": 1,
    "High": 0.8,
    "Very High": 0.6
}

e_base_options = {
    "Guaranteed": 1,
    "Likely": 0.75,
    "Could go either way (50/50)": 0.5,
    "Unlikely": 0.25,
    "Impossible": 0.01
}

v_base_options = {
    "Very very much": 2,
    "A lot": 1.5,
    "Somewhat": 1,
    "A little": 0.5,
    "Not at all": 0.25
}

i_base_options = {
    "Super focused": 0.25,
    "Focused": 0.5,
    "Somewhere in the middle": 1,
    "Distracted": 2,
    "Super/easily distracted": 4
}

d_base_options = {
    "Seconds (less than 2-3 minutes)": 0.25,
    "Minutes (less than 2 hours)": 0.5,
    "Hours (less than a day up to 1 full day)": 1,
    "Days (more than 1 day, up to 1 full week)": 2,
    "Weeks or More": 4
}

# Placeholder example usage of the new get_input function for demonstration purposes
# Uncomment the following lines if running in an interactive Python environment

def calc_raw_m(default_choice=''):
    joy_mod = get_input("Joy Levels: How enjoyable do you find this activity/effort?", joy_levels, default_choice)
    fatigue_mod = get_input("How tired are you?", fatigue_levels, default_choice)
    experience_mod = get_input("How much experience do you have with this task or similar?", experience_levels, default_choice)
    stress_mod = get_input("How stressed are you?", stress_levels, default_choice)
    e_base = get_input("How likely do you think you will get the final outcome/reward from this activity/effort?", e_base_options, default_choice)
    v_base = get_input("How much do you value the final outcome/goal achievement?", v_base_options, default_choice)
    i_base = get_input("How impulsive are you typically?", i_base_options, default_choice)
    d_base = get_input("How long do you anticipate this task/activity will take to completion?", d_base_options, default_choice)

    # Calculate E, V, I, and D
    E = (e_base / experience_mod) * stress_mod
    V = (v_base / experience_mod) * stress_mod
    I = (i_base / experience_mod) * (joy_mod / stress_mod)
    D = (d_base / experience_mod) + fatigue_mod

    # Calculate Motivation (M)
    M = (E * V) / (I * D)
    return M

# Define the normalization function
def normalize_m(m, m_worst, m_best):
    return ((m - m_worst) / (m_best - m_worst)) * 100

# Given worst and best values for M
m_worst = calc_raw_m('d')
m_best = calc_raw_m('a')
m = calc_raw_m()

# Test the function with worst and best values
normalized_worst = normalize_m(m_worst, m_worst, m_best)
normalized_best = normalize_m(m_best, m_worst, m_best)
normalized_m = normalize_m(m)

# Display results
# print(f"Calculated values:\nE: {E}\nV: {V}\nI: {I}\nD: {D}\nRaw Motivation Score (M): {M}")
print(f"Raw computed M score: {m}, normalized M score: {normalized_m}")
print(f"Raw computed worst M score: {m_worst}, normalized worst M score: {normalized_worst}")
print(f"Raw computed best M score: {m_best}, normalized best M score: {normalized_best}")
# print(f"Adjusted motivation score (0-100): ...")
