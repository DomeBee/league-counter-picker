user_champion = input("What champion are you playing against? ")

champions = {
    "Jhin": {
        "counters": {
            "Ashe": {
                "Reasons": "Longer range, stronger all-in, high kill pressure post-6.",
                "Tips": "Take extended trades with your longer range. All-in whenever you have R.",
                "Score": 9
            },
            "Caitlyn": {
                "Reasons": "Longer range, lane dominance, stronger late game.",
                "Tips": "Poke him out with your longer range. Outscale Jhin later.",
                "Score": 8
            }
        }
    },
    "Lulu": {
        "counters": {
            "Nautilus": {
                "Reasons": "Hard Engage, Gap Closes on Lulu, Strong CC",
                "Tips": "Look to engage on Lulu, Play with Bushes and secure scuttle priority early.",
                "Score": 9
            },
            "Leona": {
                "Reasons": "Strong Engage, Strong CC, Teamfight Presence",
                "Tips": "Engage on Lulu, Force her to use Utility on you. All-in Post 6.",
                "Score": 10
            }
        }
    },
    "Janna": {
        "counters": {
            "Senna": {
                "Reasons": "Win All Trades, Good Sustain, Outscales",
                "Tips": "Fully-charged Tornadoes are the only way you lose trades. Pressure accordingly",
                "Score": 8
            },
            "Xerath": {
                "Reasons": "Longer Range, High Kill Potential, Priority",
                "Tips": "Your Q always outranges Janna, W and Q if she walks up",
                "Score": 9
            }
        }
    }
}

print("Let me think for a moment...")


def best_champion(user_champion):
    best_score = 0
    good_champion = None

    if user_champion in champions:
        counter_data = champions[user_champion]["counters"]

        for counter_name, info in counter_data.items():
            score = info["Score"]
            if score > best_score:
                best_score = score
                good_champion = counter_name

        return good_champion
    else:
        return "Champion not found."


print("The best champion to pick is:", best_champion(user_champion))

extra_top3 = input("Would you like to get the Top 3 Champions for this matchup? ")


def top_3_champion(user_champion):
    top_3 = []

    if user_champion in champions:
        counter_data = champions[user_champion]["counters"]
    else:
        return "Champion not found."

    for counter_name, info in counter_data.items():
        counter_entry = (counter_name, info["Score"], info["Tips"], info["Reasons"])
        top_3.append(counter_entry)

    top_3_sorted = sorted(top_3, key=lambda x: x[1], reverse=True)
    first_3 = top_3_sorted[:3]
    return first_3


if extra_top3 == "Yes":
    print(top_3_champion(user_champion))