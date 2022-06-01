from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)

        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

    def init_capacity_volume(self, capacity_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError

        if not capacity_volume > 0:
            raise ValueError

        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, occupied_volume: Union[int, float]):
        if not isinstance(occupied_volume, (int, float), ):
            raise TypeError

        if not 0 <= occupied_volume <= self.capacity_volume:
            raise ValueError

        self.occupied_volume = occupied_volume

    def add_water(self, water):
        if not isinstance(water, int):
            raise TypeError

        if water < 0:
            raise ValueError

        space = self.capacity_volume - self.occupied_volume
        if water > space:
            raise ValueError("")

        self.occupied_volume += water

    def remove_water(self, water):
        if not isinstance(water, int):
            raise TypeError

        if water < 0:
            raise ValueError

        space = self.occupied_volume - water
        if space < 0:
            raise ValueError("Вода закончилась")

        self.occupied_volume -= water


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    glass.remove_water(120)
    print(glass.capacity_volume, glass.occupied_volume)
