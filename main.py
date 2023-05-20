import os
from diffusers import StableDiffusionPipeline

# set up a stable diffusion pipeline
pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1-base")

pipe = pipe.to("mps")
prompt = os.getenv("PROMPT")
image = pipe(prompt).images[0]

image.save("cat.jpg")
