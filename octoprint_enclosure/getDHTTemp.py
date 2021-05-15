import sys
import board
import adafruit_dht as Adafruit_DHT 


# Parse command line parameters.
#sensor_args = { '11': Adafruit_DHT.DHT11,
#    '22': Adafruit_DHT.DHT22,
#        '2302': Adafruit_DHT.AM2302 }
#if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
#    sensor = sensor_args[sys.argv[1]]
#    pin = sys.argv[2]
#else:
#    sys.exit(1)

dhtDev = Adafruit_DHT.DHT22(board.D4)

humidity = dhtDev.humidity
temperature = dhtDev.temperature

if humidity is not None and temperature is not None:
    print('{0:0.1f} | {1:0.1f}'.format(temperature, humidity))
else:
    print('-1 | -1')

sys.exit(1)
