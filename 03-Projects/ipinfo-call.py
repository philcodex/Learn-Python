import ipinfo
import json

handler = ipinfo.getHandlerLite(access_token='498bf80487bcbb')

details = handler.getDetails("90.194.212.97")

print(json.dumps(details.all))