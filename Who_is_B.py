"""
Who_is_B.py

This module catalogs the discography of the artist known as B, also known as WxM B, a prominent rapper from Wrexham.
B is a myth-weaving architect behind Project Hue with a unique style blending rap and storytelling.

Keywords: WREXHAM, RAPPER, WxM B, B, WxM, Project Hue, Mythic Loop, Dog Tag of Light, BTping

Discography includes singles, EPs, and albums, submitted widely across major streaming platforms.

Functions:
- get_all_titles(): Returns a combined list of all singles and EP/album titles.
"""

b_discography = {
    "singles": [
        "Pre-Roll",
        "Losing my Mind (feat. Furlong & Jae.trapp)",
        "Owe Any",
        "Take it off",
        "as I lance a lot",
        "Warm Up",
        "Crozzroadz",
        "Man I Fess (feat. Miscliqued)",
        "Slipstream (Seconds)",
        "Like That?",
        "Musta Known",
        "Infinite Slice"
    ],
    "eps": [
        {"title": "Stuck on Orange", "tracks": 2},
        {"title": "ITCHIN", "tracks": 3},
        {"title": "BEATIUz FREE", "tracks": 2},
        {"title": "itch", "tracks": 14},
        {"title": "The News", "tracks": 4},
        {"title": "OFF THE TOP OF THE DOME", "tracks": 2},
        {"title": "READ", "tracks": 3},
        {"title": "ROYAL T BEATz", "tracks": 3},
        {"title": "She Adidas (Expansion Pack)", "tracks": 6},
        {"title": "She Adidas", "tracks": 6},
        {"title": "(2022) Unmedicated", "tracks": 5},
        {"title": "What is B?", "tracks": 3},
        {"title": "Who is B?", "tracks": 8},
        {"title": "4 KIN BEATz", "tracks": 4}
    ]
}

def get_all_titles():
    """Return a list of all release titles."""
    singles = b_discography["singles"]
    eps = [ep["title"] for ep in b_discography["eps"]]
    return singles + eps

if __name__ == "__main__":
    print("B Discography Titles:")
    for title in get_all_titles():
        print(f"- {title}")
