import web

urls = (
  
  '/', 'Index',
  '/foo', 'Foo',
  '/static', 'Static',
  '/bootstrap', 'Bootstrap'
  
)

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        name = "Trey"
        return render.index(name)
        #i = web.input(name=None)
        #return render.index(i.name)        
        
class Foo():
    def GET(self):
    	owner = "Scott"
    	return render.foo(owner)
    
class Static(object):
    def GET(self):
    	return render.static()
    	
class Bootstrap(object):
    def GET(self):
    	return render.bootstrap()
 
if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
