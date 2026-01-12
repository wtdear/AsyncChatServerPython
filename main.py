import asyncio


clients = set()


async def handle_client(reader, writer):
    clients.add(writer)
    addr = writer.get_extra_info('peername')
    print(f"Подключён {addr}")


    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break


        message = data.decode()
        print(f"{addr}: {message}")


        for client in clients:
            if client != writer:
                client.write(data)
                await client.drain()


    except Exception as e:
        print("Ошибка:", e)


    finally:
        clients.remove(writer)
        writer.close()
        await writer.wait_closed()
        print(f"Отключён {addr}")


async def main():
    server = await asyncio.start_server(
    handle_client,
    '0.0.0.0',
    8888
    )


    async with server:
        await server.serve_forever()


asyncio.run(main())