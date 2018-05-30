import qi
import sys

#create an application
app = qi.Application(sys.argv)
app.start()

#create an instance of MyService
myfoo = MyService()

s = app.session
#let's register our service with the name "foo"
id = s.registerService("foo", myfoo)

#let the application run
app.run()