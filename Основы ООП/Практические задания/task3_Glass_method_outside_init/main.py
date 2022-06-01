from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)
        self.occupied_volume = None  # объем жидкости в стакане
        self.init_occupied_volume(occupied_volume)

    def init_capacity_volume(self, capacity_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, occupied_volume: Union[int, float]):
        if not isinstance(occupied_volume, (int, float),):
            raise TypeError
        if not 0 <= occupied_volume <= self.capacity_volume:
            raise ValueError
        self.occupied_volume = occupied_volume

if __name__ == "__main__":
    glass_1 = Glass(200, 100)  # TODO инициализировать экземпляр класса Glass
    print(glass_1.capacity_volume)  # TODO распечатать атрибут capacity_volume
    print(glass_1.occupied_volume)  # TODO распечатать атрибут occupied_volume
