class AirConditioner:
    """A room air-conditioner. Reported buggy by the QA team - fix it!"""
    VALID_MODES = ("cool", "fan", "dry", "auto")
    MIN_TEMP = 16
    MAX_TEMP = 30

    def __init__(self, brand, room_name, temperature=25, mode="cool", fan_speed=1):
        self.brand = brand
        self.room_name = room_name
        self.is_on = False
        
        # FIX 1: Assign to `self.temperature` instead of `self._temperature` 
        # so that constructor arguments are validated through the setter.
        self.temperature = temperature
        
        self.mode = mode
        self.fan_speed = fan_speed

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        # FIX 2a: Changed 'and' to 'or'. A number cannot be simultaneously < 16 AND > 30.
        if value < self.MIN_TEMP or value > self.MAX_TEMP:
            raise ValueError(f"Temperature must be {self.MIN_TEMP}-{self.MAX_TEMP} C.")
            
        # FIX 2b: Changed `self.temperature = value` to `self._temperature = value`
        # to assign to the backing attribute and prevent infinite recursion.
        self._temperature = value

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        if value not in self.VALID_MODES:
            raise ValueError(f"Mode must be one of {self.VALID_MODES}.")
        self._mode = value

    @property
    def fan_speed(self):
        return self._fan_speed

    @fan_speed.setter
    def fan_speed(self, value):
        if value not in (1, 2, 3):
            raise ValueError("Fan speed must be 1 (low), 2 (medium) or 3 (high).")
        self._fan_speed = value

    @property
    def is_energy_saving(self):
        # FIX 3: Calculate dynamically based on the current temperature 
        # instead of returning a static attribute set at initialization.
        return self.temperature >= 25

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def cooler(self):
        # FIX 4: Check MIN_TEMP boundary before decrementing temperature.
        if self._temperature > self.MIN_TEMP:
            self._temperature -= 1

    def warmer(self):
        # FIX 5: Check MAX_TEMP boundary before incrementing temperature.
        if self._temperature < self.MAX_TEMP:
            self._temperature += 1

    def __str__(self):
        power = "ON" if self.is_on else "OFF"
        # FIX 6: Renamed `self.fan` to `self.fan_speed` to match the actual property name.
        return (f"{self.brand} AC in {self.room_name}: {power}, "
                f"{self.temperature}C, mode={self.mode}, fan={self.fan_speed}")
