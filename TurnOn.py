import asyncio
from bleak import BleakScanner
from bleak import BleakClient

UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        if "Pwn To Survive" in str(d): 
            mac = str(d).split(" ")[0][:-1]
            async with BleakClient(mac) as client:
                state = await client.read_gatt_char(UUID)
                print("Module state: {0}".format("".join(map(chr, state))))
                w = await client.write_gatt_char(UUID, b"AL1V3")
                state = await client.read_gatt_char(UUID)
                print("Module state: {0}".format("".join(map(chr, state))))
                await client.disconnect()
asyncio.run(main())
