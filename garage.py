import ntptime
import machine
import esp32
import dht
import time
from singletons import get_logger


machine.freq()
machine.freq(240_000_000)

esp32.hall_sensor()
esp32.raw_temperature()
esp32.ULP()

SSID = 'subnet'
KEY = 'xam_8B0*'

DHT_SENSOR_1_PIN = 13


def fahrenheit_to_celsius(temperature: float) -> float:
    return round((temperature - 32) * 5/9, 2)


def do_connect(ssid: str, key: str) -> tuple[bool, str]:
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(SSID, KEY)
        while not wlan.isconnected():
            pass
    return True, f'network config: {wlan.ifconfig()}'


def get_dht_measure(sensor: dht) -> tuple[float, float]:
    try:
        sensor.measure()
        return (sensor.temperature(), sensor.humidity())
    except Exception:
        pass

do_connect(SSID, KEY)

dht_sensor_1 = dht.DHT22(machine.Pin(DHT_SENSOR_1_PIN))

# while True:
try:
    print(f'Temperture: {get_dht_measure(dht_sensor_1)[0]}')
    print(f'Humidity: {get_dht_measure(dht_sensor_1)[1]}')
    print('\n')
except Exception:
    pass


print("Local time before synchronization：%s" % str(time.localtime()))
ntptime.settime()
print("Local time after synchronization：%s" % str(time.localtime()))
