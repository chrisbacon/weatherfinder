import web
import metoffer
import json

api_key = 'fdeee994-304e-4ce9-86d4-de83f8fba702'
M = metoffer.MetOffer(api_key)

urls = (
    '/weather', 'weather'
)

render = web.template.render('templates/')

class weather:
    def GET(self):
        return render.weather()
    def POST(self):
        data = web.input()
        x = M.nearest_loc_forecast(float(data['lat']), float(data['lng']), metoffer.THREE_HOURLY)

        for i in range(1):
            y = metoffer.parse_val(x)
            json_dict = {'location': str(y.name + ', ' + y.country),
                         'weather': metoffer.WEATHER_CODES[y.data[0]["Weather Type"][0]],
                         'temp': y.data[0]["Temperature"][0]}
            web.header('Content-Type', 'application/json')
            return json.dumps(json_dict)
        #except KeyError,e:
         #   print
          #  return web.internalerror(self)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()