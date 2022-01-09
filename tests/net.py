import hek

# connect to wifi
result = hek.wifi.connect(ssid="Wifi ssid/Name", # wifi ssid/name
                          password="wifi-password" # wifi password
                          )
# connection result
print(result)