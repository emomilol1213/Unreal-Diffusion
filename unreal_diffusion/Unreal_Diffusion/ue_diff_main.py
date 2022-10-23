import requests
import json
import base64
import argparse
import asyncio

#only load unreal module when inside the editor
try:
    import unreal
    in_unreal = True
except ImportError:
    in_unreal = False

parser = argparse.ArgumentParser(description="Unreal Diffusion Plugin")
parser.add_argument("prompt", type=str, help="Prompt of the txt2img")
parser.add_argument("--x", type=int, metavar="", default=512, help="X size in pixels")
parser.add_argument("--y", type=int, metavar="", default=512, help="Y size in pixels")
parser.add_argument("--cfg", type=float, metavar="", default=12, help="CFG Scale")
parser.add_argument("--i","--iterations", type=int, metavar="", default=1, help="number of images to generate")
parser.add_argument("--steps", type=int, metavar="", default=32, help="number of steps")
parser.add_argument("--img2img", "--initimg", "--i2i", metavar="", type=str, help="Img2Img switch if set to 1")
parser.add_argument("--strength",metavar="", type=float, default=0.5, help="Img2Img Strength")
parser.add_argument('--seamless',action='store_true',help='Change the model to seamless tiling (circular) mode')
parser.add_argument('--realtime',action='store_true',help='realtime mode, doesn´t freeze the editor')
parser.add_argument("--seed","--s", type=int, metavar="", help="Seed")
parser.add_argument('-v', '--variation_amount', default=0.0, type=float, help='If > 0, generates variations on the initial seed instead of random seeds per iteration. Must be between 0 and 1. Higher values will be more different.')

args = parser.parse_args()


null = None
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

prompt = args.prompt

width = args.x
height = args.y
seamless = args.seamless if args.seamless else False
iterations = args.i if args.i != 1 else 1
seed = args.seed if args.seed else 1

mime = "images/png,"

if (args.img2img):
    initimg = args.img2img
    encoded = base64.b64encode(open(initimg, "rb").read())
    encodedmime = mime + encoded.decode("ascii")
    initimg = encodedmime
else:
    initimg = null

data = {       
        "index":0,
        "prompt":prompt,
        "width":width,
        "height":height,
        "variation_amount":args.variation_amount,
        "with_variations":"",
        "steps":args.steps,
        "seed":seed,
        "strength":args.strength,
        "initimg":initimg,
        "cfg_scale":args.cfg,
        "iterations":iterations,
        "upscale_level":0,
        "upscale_strength":0,
        "sampler_name":"k_euler"
}

if(seamless):
    data["seamless"] = seamless
    
data_json = json.dumps(data)


realtime = True
if not (args.realtime):
    response = requests.post('http://localhost:3333', headers=headers, data=data_json)
else:
    def background(f):
        from functools import wraps
        @wraps(f)
        def wrapped(*args, **kwargs):
            loop = asyncio.get_event_loop()
            if callable(f):
                return loop.run_in_executor(None, f, *args, **kwargs)
            else:
                raise TypeError('Task must be a callable')    
        return wrapped


    @background
    def foo():
        response = requests.post('http://localhost:3333', headers=headers, data=data_json)
        print("Image generation completed")


    print("Starting runtime diffusion")
    foo()
    print("Waiting for results")