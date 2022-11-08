# Copyright 2022 Rom Adams (https://github.com/romdalf) at Red Hat Inc. 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
import websockets
import logging 

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

async def deviceService(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with websockets.serve(deviceService, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
