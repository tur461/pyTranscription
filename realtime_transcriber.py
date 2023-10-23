import websockets as ws
import asyncio
import base64 as bs64
import json
#from configure import auth_key as akey
import pyaudio as pyaud

FRAMES_PER_BUF = 3200
FORMAT = pyaud.paInt16
CHANS = 1
RATE = 16000

# the AssemblyAI endpoint we're going to hit
URL = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"

AssemblyAI_API_KEY = '1ded8191dab84e6ba4151d0401f223d0'

paud = pyaud.PyAudio()

stream = paud.open(
        format = FORMAT,
        channels = CHANS,
        rate = RATE,
        input = True,
        frames_per_buffer = FRAMES_PER_BUF
)


async def send_receive():
    print(f'connecting ws to ${URL}')
    async with ws.connect(
        URL,
        extra_headers = (('Authorization', AssemblyAI_API_KEY),),
        ping_interval = 5,
        ping_timeout = 20
    ) as _ws:
        await asyncio.sleep(0.1)
        print('receiving sessiion begins..')
        sess_begins = await _ws.recv()
        print(sess_begins)
        print('sending messages..')
        async def send():
            while True:
                try:
                    data = stream.read(FRAMES_PER_BUF)
                    encData = b64.b64encode(data).decode('utf-8')
                    json_data = json.dumps({'audio_data': str(encData)})
                    await _ws.send(json_data)
                except ws.exceptions.ConnectionClosedError as e:
                    print(e)
                    assert e.code == 4008
                    break
                except Exception as e:
                    assert False, 'Unknown Error occured!'
                    break
                await asyncio.sleep(0.01)
            return True

        async def recv():
            while True:
                try:
                    res_str = await _ws.recv()
                    print(josn.loads(res_str)['text'])
                except ws.exceptions.ConnectionClosedError as e:
                    print(e)
                    assert e.code == 4008
                    break
                except Exception as e:
                    assert False, 'Unknown Error occured!'
                    break
        send_res, recv_result = await asyncio.gather(send(), recv())

asyncio.run(send_receive())
