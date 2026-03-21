user_champion = input("What champion are you playing against? ")
best_score = 0
best_champion = None
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
    }, "Lulu": {
        "counters":{
            "Nautilus":{
                "Reasons": "Hard Engage, Gap Closes on Lulu, Strong CC",
                "Tips": "Look to engage on Lulu, Play with Bushes and secure scuttle priority early.",
                "Score" : 9
            },
            "Leona":{
                "Reasons": "Strong Engage, Strong CC, Teamfight Presence",
                "Tips": "Engage on Lulu, Force her to use Utility on you. All-in Post 6.",
                "Score": 10
            }
        }
    }, "Janna": {
        "counters":{
            "Senna":{
                "Reasons": "Win All Trades, Good Sustain, Outscales",
                "Tips" : "Fully-charged Tornadoes are the only way you lose trades. Pressure accordingly",
                "Score": 8
            },
            "Xerath":{
                "Reasons": "Longer Range, High Kill Potential, Priority",
                "Tips": "Your Q always outranges Janna, W and Q if she walks up",
                "Score": 9
            }
        }
    }
} 

print("Let me think for a moment...")

if user_champion in champions:
    counter_data = champions[user_champion]["counters"]

    for counter_name, info in counter_data.items():
        score = info['Score']
        if score > best_score:
            best_score = score
            best_champion = counter_name
        print(f"\nCounter pick: {counter_name}")
        print(f"Reasons: {info['Reasons']}")
        print(f"Tips: {info['Tips']}")
        print(f"Score:{info['Score']}")
        
    print(f"\nThe Best Champion to Pick is:" + best_champion)
else:
    print("Champion not found.")