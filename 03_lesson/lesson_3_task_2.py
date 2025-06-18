from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "10 Pro", "+79001001010"),
    Smartphone("Apple", "11 Pro", "+79002002020"),
    Smartphone("Apple", "12 Pro", "+79003003030"),
    Smartphone("Apple", "13 Pro", "+79004004040"),
    Smartphone("Apple", "14 Pro", "+79005005050")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
