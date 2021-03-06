import tornado.ioloop
import tornado.web
import json
import os

g_port=9998

g_router=""
def createHtmlPage(firstPart, getUrl, secondPart, body, thirdPart):
	f = open(os.path.join(os.path.dirname(__file__),"template/tmp.html"), "w")

	with open(os.path.join(os.path.dirname(__file__),firstPart),"r") as infile: #copy infile into f
		f.write(infile.read())
	f.write(getUrl)
	with  open(os.path.join(os.path.dirname(__file__),secondPart),"r") as infile:
		f.write(infile.read())
	with  open(os.path.join(os.path.dirname(__file__),body),"r") as infile:
		f.write(infile.read())
	with  open(os.path.join(os.path.dirname(__file__),thirdPart),"r") as infile:
		f.write(infile.read())

	f.close()

def createHtmlPageParams(firstPart, getUrl, secondPart, params, thirdPart, body, fourthPart):
	f = open(os.path.join(os.path.dirname(__file__),"template/tmp.html"), "w")

	with open(os.path.join(os.path.dirname(__file__),firstPart),"r") as infile: #copy infile into f
		f.write(infile.read())
	f.write(getUrl)
	with open(os.path.join(os.path.dirname(__file__),secondPart),"r") as infile:
		f.write(infile.read())
	f.write(str(params))
	with open(os.path.join(os.path.dirname(__file__),thirdPart),"r") as infile:
		f.write(infile.read())
	with open(os.path.join(os.path.dirname(__file__),body),"r") as infile:
		f.write(infile.read())
	with open(os.path.join(os.path.dirname(__file__),fourthPart),"r") as infile:
		f.write(infile.read())

	f.close()

class mainPage(tornado.web.RequestHandler):
	def get(self, uri):
		'''Render page with javascript get requests to api (through router)'''
		if self.cookies:
			print("I received some cookies from the scout girls.")
			print(self.get_secure_cookie("UserType"), self.get_secure_cookie("UserID"))

		parsed = uri.split("/")
		url = str(g_router + "/api/" + uri)
		if parsed[0] == "rozvrh":
			data = (json.dumps({
				'datum':"1.1.2022",
				'type':"prednasky"
			}))

			createHtmlPageParams("template/page1.html", url, "template/page2params.html", data, "template/page3params.html", "template/body.html","template/page3and4params.html")
			f =  open(os.path.join(os.path.dirname(__file__),"template/tmp.html")) # Opened to get the current (latest) version, with simple render he used the file created after first run on every attempt
			self.write(f.read())
		else:
			createHtmlPage("template/page1.html", url, "template/page2.html", "template/body.html", "template/page3and4params.html")
			f =  open(os.path.join(os.path.dirname(__file__),"template/tmp.html")) # Opened to get the current (latest) version, with simple render he used the file created after first run on every attempt
			self.write(f.read())

		f.close()

application = tornado.web.Application([
    (r"/(.*)", mainPage),
], 
	cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__")

if __name__ == "__main__":
	application.listen(g_port)
	print("UI_tornado running on port: " + str(g_port) + "...")
	tornado.ioloop.IOLoop.instance().start()
