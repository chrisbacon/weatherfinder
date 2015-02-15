import web
import metoffer
import json

api_key = 'fdeee994-304e-4ce9-86d4-de83f8fba702'
M = metoffer.MetOffer(api_key)

urls = (
    '/', 'index',
    '/data', 'data'
)

render = web.template.render('templates/')

class index:
    def GET(self):
        return render.index()
class data:
    def POST(self):
        data = web.input()
        x = M.nearest_loc_forecast(float(data['lat']), float(data['lng']), metoffer.THREE_HOURLY)
        y = metoffer.parse_val(x)
        data_dict = {'location': str(y.name + ', ' + y.country),
                     'weather': metoffer.WEATHER_CODES[y.data[0]["Weather Type"][0]],
                     'temp': y.data[0]["Temperature"][0]}
        return render.data(data_dict)
        #except KeyError,e:
         #   print
          #  return web.internalerror(self)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()