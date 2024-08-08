artists: dict[str, int] = {
    "Radiohead": 156,
    "Kishore Kumar": 141,
    "The Black Eyes": 35,
    "Neutral Milk Hotel": 94,
    "Beck": 88,
    "The Strokes": 61,
    "Wilko": 111,
}

order_list_artists: list = [*artists.items()]

print(order_list_artists)

order_list_artists.sort(key=lambda x: x[1]) # X[0]: Name; X[1]: Total Played

print(order_list_artists)
