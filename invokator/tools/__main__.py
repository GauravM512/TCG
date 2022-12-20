"""Fetch raw card data."""
import json
import os

from .raw import fetch_cards
from .converter import convert_to_carddata

if __name__ == "__main__":
    print("Fetching cards...")  # noqa: T201
    cards = fetch_cards()

    os.makedirs("carddata/raw", exist_ok=True)

    with open("carddata/raw/cards.json", "w", encoding="utf-8") as f:
        json.dump(cards, f, indent=4, ensure_ascii=False)

    print("Converting to carddata...") # noqa: T201
    carddata = convert_to_carddata(cards)

    with open("characters.json", "w", encoding="utf-8") as f:
        json.dump(carddata, f, indent=4, ensure_ascii=False, sort_keys=True)

    print("Done.")  # noqa: T201
