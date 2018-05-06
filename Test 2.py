import sys
import time
# Keeps the initial message in buffer.
sys.stdout.write("\rfoobar bar black sheep")
sys.stdout.flush()
# Wait 2 seconds
time.sleep(2)
# Replace the message with a new one.
sys.stdout.write("\r"+'hahahahaaa             ')
sys.stdout.flush()
# Finalize the new message by printing a return carriage.
sys.stdout.write('\n')
