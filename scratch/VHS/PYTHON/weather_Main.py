# import ALL
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess
import time
import adafruit_dht
from Adafruit_IO import Client, Feed

# Delay in-between sensor readings, in seconds.
DHT_READ_TIMEOUT = 10

# Pin connected to DHT22 data pin
DHT_DATA_PIN = 4

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = '0d4ec3bc5ebd45f286f70be93e7301c8'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username).
ADAFRUIT_IO_USERNAME = 'rao003'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Set up Adafruit IO Feeds.
temperature_feed = aio.feeds('temperature')
humidity_feed = aio.feeds('humidity')

# Set up DHT22 Sensor.
dht22_sensor = Adafruit_DHT.DHT22

while True:
    humidity, temperature = Adafruit_DHT.read_retry(dht22_sensor, DHT_DATA_PIN)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
        # Send humidity and temperature feeds to Adafruit IO
        temperature = '%.2f'%(temperature)
        humidity = '%.2f'%(humidity)
        aio.send(temperature_feed.key, str(temperature))
        aio.send(humidity_feed.key, str(humidity))
    else:
        print('Failed to get DHT22 Reading, trying again in ', DHT_READ_TIMEOUT, 'seconds')
    # Timeout to avoid flooding Adafruit IO
    time.sleep(DHT_READ_TIMEOUT)

#display code
RST = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image1 = Image.new('1', (width, height))
draw = ImageDraw.Draw(image1)
draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding
x = 0
font = ImageFont.load_default()

# PRINT TEMPERATURE and HUMIDITY

while True:
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Write two lines of text.
    disp.clear()
    disp.display()
    draw.text((x, top),     disp.temperature,  font=font, fill=255)
    draw.text((x, top+8),    disp.humidity,   font=font, fill=255)
    draw.text((x, top+16),    "For more Videos",  font=font, fill=255)
    draw.text((x, top+25),    "Visit at",  font=font, fill=255)
    draw.text((x, top+34),    "www.circuitdigest.com",  font=font, fill=255)
