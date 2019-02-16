import socketio
from aiohttp import web
from aiohttp_index import IndexMiddleware

#Setting Up Server
sio = socketio.AsyncServer()
app = web.Application(middlewares=[IndexMiddleware()])
sio.attach(app)


#Serves all static files in Public folders
app.router.add_static('/', 'Public')


@sio.on('connect')
def connect(sid, environ):
    print("Client: " + sid + " has connected!")

@sio.on('message')
async def message(sid, message):
    print(sid + " " + message)
    await sio.emit('message',message)



if __name__ == '__main__':
    web.run_app(app)
