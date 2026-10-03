import json
import math
import random
from pathlib import Path

def generate(count=500, arms=4):
    stars = []
    for _ in range(count):
        arm = random.randrange(arms)
        radius = random.random() ** 0.55 * 100
        angle = radius * 0.08 + arm * (2 * math.pi / arms) + random.gauss(0, .15)
        stars.append({
            "x": radius * math.cos(angle),
            "y": random.gauss(0, 3),
            "z": radius * math.sin(angle)
        })
    return stars

Path("galaxy.json").write_text(json.dumps(generate(), indent=2), encoding="utf-8")
print("galaxy.json erzeugt")
