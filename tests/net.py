import hek

# stop monitor mode
result = hek.net.monitor_stop(name="wlan0mon")

# Output
print(result)