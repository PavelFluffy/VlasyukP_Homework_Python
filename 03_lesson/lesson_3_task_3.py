from address import Address
from mailing import Mailing

to_address = Address(140048, "Москва", "Лермонтова", 10, 204)
from_address = Address(100001, "Коломна", "Краскова", 14, 32)

ExMailing = Mailing(
    to_address,
    from_address,
    250,
    "AA123456789BB")

print(f"Отправление {ExMailing.track} из {ExMailing.from_address.index}, "
      f" {ExMailing.from_address.city}, {ExMailing.from_address.street}, "
      f"{ExMailing.from_address.house} - {ExMailing.from_address.apartment} "
      f"в {ExMailing.to_address.index}, {ExMailing.to_address.city}, "
      f"{ExMailing.to_address.street}, {ExMailing.to_address.house} - "
      f"{ExMailing.to_address.apartment}. Стоимость {ExMailing.cost} рублей.")
