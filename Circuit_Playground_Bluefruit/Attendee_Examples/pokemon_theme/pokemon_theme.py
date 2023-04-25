from adafruit_circuitplayground import cp
import time

a = 440
g = 392
e = 329
c = 261
f = 349
b = 473

quarter = .5
half = 1
triple = .167 

cp.play_tone(a, triple)
cp.play_tone(a, triple)
cp.play_tone(a, triple)
cp.play_tone(a, quarter)
cp.play_tone(a, quarter)
cp.play_tone(g, quarter)
cp.play_tone(e, quarter)
cp.play_tone(c, quarter)
cp.play_tone(c, quarter)
cp.play_tone(a, quarter)
cp.play_tone(a, quarter)
cp.play_tone(g, quarter)
cp.play_tone(f, quarter)
cp.play_tone(g, half)
time.sleep(half)
cp.play_tone(f, quarter)
cp.play_tone(b, quarter)
cp.play_tone(b, quarter)
cp.play_tone(b, quarter)
cp.play_tone(a, quarter)
cp.play_tone(g, quarter)
cp.play_tone(f, quarter)
cp.play_tone(f, quarter)
cp.play_tone(a, quarter)
cp.play_tone(a, quarter)
cp.play_tone(g, quarter)
cp.play_tone(f, quarter)
cp.play_tone(a, half)
