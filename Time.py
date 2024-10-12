class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add_minutes(self, minutes):
        self.hours += minutes // 60
        self.minutes += minutes % 60
        self.hours += self.minutes // 60

        self.minutes = self.minutes % 60
        self.hours = self.hours % 24

    def set_time(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f"{self.hours}:{self.minutes}"
    

if __name__ == "__main__":
    time = Time(12,32)
    time.add_minutes(100)
    print(time)
