import asyncio
import websockets
import i_am_common

connected_clients = set()

async def handle_client(websocket):
    print("New connection!")


    connected_clients.add(websocket)

    try:
     
        await websocket.send("Hello from server!")

   
        while True:
            message = await websocket.recv()
            print(f"Message from client: {message}")

           
            for client in connected_clients:
                await client.send(f"{message}")

    except websockets.ConnectionClosed:
        print("Connection closed")

    finally:
        connected_clients.remove(websocket)

async def main():
    server = await websockets.serve(handle_client, i_am_common.SERVER_HOST, i_am_common.SERVER_PORT)
    print("Server started on ws://localhost:8080")
    await server.wait_closed()

asyncio.run(main())
