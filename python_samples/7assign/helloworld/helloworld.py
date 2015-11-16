import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Ni Hao Shi Jie - Hello World in Mandarin!')

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

