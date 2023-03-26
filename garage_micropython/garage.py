import machine
import esp32
import ntptime
import dht
import time


machine.freq()
machine.freq(240_000_000)

esp32.hall_sensor()
esp32.raw_temperature()
esp32.ULP()

SSID = ''
KEY = ''

TIMEZONE = 3
NTP_SERVER_ADDRESS = '0.ru.pool.ntp.org'

DHT_SENSOR_1_PIN = 34
DHT_SENSOR_2_PIN = 35
DHT_SENSOR_3_PIN = 32

dht_sensor_1 = dht.DHT22(machine.Pin(DHT_SENSOR_1_PIN))
dht_sensor_2 = dht.DHT22(machine.Pin(DHT_SENSOR_2_PIN))
dht_sensor_3 = dht.DHT22(machine.Pin(DHT_SENSOR_3_PIN))


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
    return (True, f'network config: {wlan.ifconfig()}')


def get_dht_measure(sensor: dht) -> tuple[float, float]:
    try:
        sensor.measure()
        return (sensor.temperature(), sensor.humidity())
    except Exception:
        pass


if do_connect(SSID, KEY)[0]:
    print("Local time before synchronization：%s" % str(time.localtime()))
    # ntptime.settime(timezone=TIMEZONE, server=NTP_SERVER_ADDRESS)
    ntptime.settime()
    print("Local time after synchronization：%s" % str(time.localtime()))


# while True:
try:
    print(f'Temperture: {get_dht_measure(dht_sensor_1)[0]}')
    print(f'Humidity: {get_dht_measure(dht_sensor_1)[1]}')
    print('\n')
except Exception:
    pass
