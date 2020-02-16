class PublicTransportInterface:
    def transport_people(self):
        raise NotImplementedError('This method must be implemented in subclass')

    def display_info(self):
        raise NotImplementedError('This method must be implemented in subclass')


class Tram(PublicTransportInterface):
    def __init__(self, tram_type, capacity, max_speed):
        self.tram_type = tram_type
        self.capacity = capacity
        self. max_speed = max_speed

    def transport_people(self):
        print(f'{self.__class__.__name__} transported {self.capacity} people')

    def display_info(self):
        print(f'Tram type: {self.tram_type}\nCapacity: {self.capacity}\nMax speed: {self.max_speed}')


class Bus(PublicTransportInterface):
    def __init__(self, brand, capacity, color):
        self.brand = brand
        self.capacity = capacity
        self.color = color

    def transport_people(self):
        print(f'{self.__class__.__name__} transported {self.capacity} people')

    def display_info(self):
        print(f'Bus brand: {self.brand}\nCapacity: {self.capacity}\nColor: {self.color}')


class MercedesBenzBus(Bus):
    def __init__(self, air_conditioning, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.air_conditioning = air_conditioning

    def display_info(self):
        super().display_info()
        print(f'Air conditioning: {self.air_conditioning}')


avenio_tram = Tram('Avenio', 240, 80)
volvo_bus = Bus('Volvo', 30, 'white')
mercedes_benz_bus = MercedesBenzBus(True, 'Mercedes-Benz', 40, 'black')

for public_transport in [avenio_tram, volvo_bus, mercedes_benz_bus]:
    public_transport.transport_people()
    public_transport.display_info()
    print('-------------------')