import sys
sys.path.append("lib")
from sensor import Sensor
error_count = 0

class SequenceSource:

    def __init__(self, values=None):
        self._values = values
        self._index = 0

    def __call__(self):
        if self._values is None:
            value = self._index + 1
        else:
            value = self._values[self._index]
        self._index += 1
        return value


def assert_raises_value_error(func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except ValueError as e:
        return str(e)    
    raise AssertionError("ValueError bekleniyordu ama hata firlatilmadi")


def test_init_valid_values():
    s = Sensor("sicaklik", "C", 0, 100, noise=1.5, history_size=5)
    
    assert s.name == "sicaklik", "name yanlis atandi"
    assert s.unit == "C", "unit yanlis atandi"
    assert s.min_value == 0, "min_value yanlis atandi"
    assert s.max_value == 100, "max_value yanlis atandi"
    assert s.noise == 1.5, "noise yanlis atandi"
    assert s.history_size == 5, "history_size yanlis atandi"
    assert s.history() == [], "yeni sensorun gecmisi bos olmali"
    assert s.error_count() == 0, "yeni sensorun hata sayisi 0 olmali"


def test_init_min_equal_max_raises():
    assert_raises_value_error(Sensor, "x", "u", 10, 10)


def test_init_min_greater_than_max_raises():
    msg = assert_raises_value_error(Sensor, "x", "u", 50, 10)
    assert "min_value" in msg, "hata mesaji min_value'yu belirtmeli"


def test_init_history_size_zero_raises():
    assert_raises_value_error(Sensor, "x", "u", 0, 10, history_size=0)


def test_init_history_size_negative_raises():
    assert_raises_value_error(Sensor, "x", "u", 0, 10, history_size=-3)


def test_init_history_size_one_is_allowed():
    s = Sensor("x", "u", 0, 10, history_size=1)
    assert s.history_size == 1, "history_size=1 kabul edilmeliydi"


def test_init_negative_noise_raises():
    assert_raises_value_error(Sensor, "x", "u", 0, 10, noise=-0.1)


def test_read_without_source_stays_in_range():
    s = Sensor("x", "u", 10, 20)
    for _ in range(200):
        value = s.read()
        assert value is not None, "gurultusuz okumada None donmemeli"
        assert 10 <= value <= 20, f"deger aralik disi: {value}"


def test_read_uses_source_values_in_order():
    s = Sensor("x", "u", 0, 100, source=SequenceSource())
    assert s.read() == 1, "ilk okuma 1 olmali"
    assert s.read() == 2, "ikinci okuma 2 olmali"
    assert s.read() == 3, "ucuncu okuma 3 olmali"


def test_read_with_noise_stays_within_tolerance():
    s = Sensor("x", "u", 0, 10, noise=0.5, source=lambda: 5)
    for _ in range(200):
        value = s.read()
        assert value is not None, "genis aralikta deger gecersiz sayilmamali"
        assert 4.5 <= value <= 5.5, f"gurultu toleransi asildi: {value}"


def test_read_out_of_range_returns_none_and_counts_error():
    s = Sensor("x", "u", 0, 10, source=SequenceSource([5, 100, 5]))

    assert s.read() == 5, "gecerli deger aynen donmeli"
    assert s.read() is None, "aralik disi degerde None donmeli"
    assert s.error_count() == 1, "hata sayaci 1 olmali"
    assert s.read() == 5, "hatadan sonra normal okumaya devam etmeli"
    assert s.error_count() == 1, "gecerli okuma hata sayacini artirmamali"


def test_read_invalid_value_not_added_to_history():
    s = Sensor("x", "u", 0, 10, source=SequenceSource([5, -1, 7]))
    s.read()
    s.read()
    s.read()     
       
    assert s.history() == [5, 7], f"gecmis yanlis: {s.history()}"


def test_read_non_numeric_source_value_is_error():
    s = Sensor("x", "u", 0, 10, source=SequenceSource(["abc", None, 5]))
    assert s.read() is None, "yazi degeri gecersiz sayilmali"
    assert s.read() is None, "None degeri gecersiz sayilmali"
    assert s.read() == 5, "ardindan gelen gecerli deger okunmali"
    assert s.error_count() == 2, "iki gecersiz okuma sayilmali"


def test_read_boundary_values_are_valid():
    s = Sensor("x", "u", 0, 10, source=SequenceSource([0, 10]))
    assert s.read() == 0, "min_value gecerli olmali"
    assert s.read() == 10, "max_value gecerli olmali"
    assert s.error_count() == 0, "sinir degerler hata sayilmamali"


def test_read_noise_at_edge_every_read_accounted_for():
    total = 300
    count = 0
    s = Sensor("x", "u", 0, 10, noise=2, history_size=total, source=lambda: 10)
    for _ in range(total):
        result = s.read()
        if result == 10:
            count += 1  
    assert count == 0, "gurultu eklenmiyor"  
    assert len(s.history()) + s.error_count() == total, (
        f"okumalar tutmuyor: gecmis={len(s.history())}, hata={s.error_count()}"
    )


def test_history_respects_size_limit():
    s = Sensor("x", "u", 0, 100, history_size=3, source=SequenceSource())
    for _ in range(5):
        s.read()
    assert s.history() == [3, 4, 5], f"gecmis yanlis: {s.history()}"


def test_average_empty_history_returns_none():
    s = Sensor("x", "u", 0, 10)
    assert s.average() is None, "bos gecmiste ortalama None olmali"


def test_average_is_correct():
    s = Sensor("x", "u", 0, 100, source=SequenceSource())
    s.read()
    s.read()
    s.read()
    assert s.average() == 2.0, f"ortalama yanlis: {s.average()}"


def test_average_ignores_invalid_values():
    s = Sensor("x", "u", 0, 10, source=SequenceSource([2, 999, 4]))
    for _ in range(3):
        s.read()
    assert s.average() == 3.0, f"ortalama yanlis: {s.average()}"


def test_history_returns_copy():
    s = Sensor("x", "u", 0, 100, source=SequenceSource())
    s.read()
    s.read()

    dis_liste = s.history()
    dis_liste.append(999)
    dis_liste.clear()

    assert s.history() == [1, 2], "disaridan degisiklik ic gecmisi etkiledi"


def test_is_valid():
    s = Sensor("x", "u", 0, 10)

    assert s.is_valid(5) is True, "orta deger gecerli olmali"
    assert s.is_valid(5.5) is True, "ondalikli deger gecerli olmali"
    assert s.is_valid(0) is True, "alt sinir dahil olmali"
    assert s.is_valid(10) is True, "ust sinir dahil olmali"

    assert s.is_valid(-0.001) is False, "alt sinirin hemen alti gecersiz"
    assert s.is_valid(10.001) is False, "ust sinirin hemen ustu gecersiz"
    assert s.is_valid("5") is False, "yazi gecersiz olmali"
    assert s.is_valid(None) is False, "None gecersiz olmali"


def test_error_count_accumulates():
    s = Sensor("x", "u", 0, 10, source=SequenceSource([-1, -2, 5, 50]))
    for _ in range(4):
        s.read()
    assert s.error_count() == 3, f"hata sayisi yanlis: {s.error_count()}"


def test_repr_empty_sensor():
    s = Sensor("T1", "C", 0, 100)
    beklenen = "Sensor(name='T1', unit='C', n=0, average=None, errors=0)"
    assert repr(s) == beklenen, f"repr yanlis: {repr(s)}"


def test_repr_with_data():
    s = Sensor("T1", "C", 0, 100, source=SequenceSource([1, 2, 4, 999]))
    for _ in range(4):
        s.read()
    beklenen = "Sensor(name='T1', unit='C', n=3, average=2.33, errors=1)"
    assert repr(s) == beklenen, f"repr yanlis: {repr(s)}"


TESTS = [
    test_init_valid_values,
    test_init_min_equal_max_raises,
    test_init_min_greater_than_max_raises,
    test_init_history_size_zero_raises,
    test_init_history_size_negative_raises,
    test_init_history_size_one_is_allowed,
    test_init_negative_noise_raises,
    test_read_without_source_stays_in_range,
    test_read_uses_source_values_in_order,
    test_read_with_noise_stays_within_tolerance,
    test_read_out_of_range_returns_none_and_counts_error,
    test_read_invalid_value_not_added_to_history,
    test_read_non_numeric_source_value_is_error,
    test_read_boundary_values_are_valid,
    test_read_noise_at_edge_every_read_accounted_for,
    test_history_respects_size_limit,
    test_average_empty_history_returns_none,
    test_average_is_correct,
    test_average_ignores_invalid_values,
    test_history_returns_copy,
    test_is_valid,
    test_error_count_accumulates,
    test_repr_empty_sensor,
    test_repr_with_data,
]


def run_tests(tests):
    global error_count
    passed = 0
    failed = []

    for test in tests:
        try:
            test()
        except AssertionError as e:
            failed.append((test.__name__, str(e)))
            print(f"[KALDI] {test.__name__}")
        except IndexError as e:
                print(f"{e}(\"kaynak tükendi\")")
                error_count += 1  
        except Exception:
                error_count += 1                     
        else:
            passed += 1
            print(f"[GECTI] {test.__name__}")

    print()
    print("=" * 50)
    print("TEST RAPORU")
    print("=" * 50)
    print(f"Toplam : {len(tests)}")
    print(f"Gecen  : {passed}")
    print(f"Kalan  : {len(failed)}")
    print(f"Hata   : {error_count}")

    if failed:
        print()
        print("Kalan testler:")
        for name, message in failed:
            print(f"  - {name}: {message or '(mesaj yok)'}")


if __name__ == "__main__":
    run_tests(TESTS)
