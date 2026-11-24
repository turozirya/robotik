import random


class Sensor:
    def __init__(self, name, unit, min_value, max_value, noise=0.0, history_size=20, source=None):
        if min_value >= max_value:
            raise ValueError("min_value, max_value değerinden küçük olmalidir.")

        if history_size < 1:
            raise ValueError("history_size 0'dan buyuk bir deger olmalidir.")

        if noise < 0:
            raise ValueError("noise negatif bir deger olamaz.")

        self.name = name
        self.unit = unit
        self.min_value = min_value
        self.max_value = max_value
        self.noise = noise
        self.history_size = history_size
        self._source = source

        self._history = []
        self._error_count = 0

    def read(self):
        if self._source is None:
            raw_value = random.uniform(self.min_value, self.max_value)
        else:
            raw_value = self._source()

        if self.noise > 0:
            value = raw_value + random.uniform(-self.noise, self.noise)
        else:
            value = raw_value

        if not self.is_valid(value):
            self._error_count += 1
            return None

        self._history.append(value)

        if len(self._history) > self.history_size:
            self._history.pop(0)

        return value

    def is_valid(self, value):
        if not isinstance(value, (int, float)):
            return False

        if value < self.min_value or value > self.max_value:
            return False

        return True

    def average(self):
        if not self._history:
            return None

        return sum(self._history) / len(self._history)

    def history(self):
        return self._history[:]

    def error_count(self):
        return self._error_count

    def __repr__(self):
        if self.average() is None:
            avg = None
        else:
            avg = round(self.average(), 2)

        return (
            f"Sensor(name='{self.name}', "
            f"unit='{self.unit}', "
            f"n={len(self._history)}, "
            f"average={avg}, "
            f"errors={self._error_count})"
        )


# Dosya doğrudan çalıştırıldığında burası devreye girer
if __name__ == "__main__":
    print("UYARI: Bu dosya bir modüldür ve tek basina calistirilamaz!")