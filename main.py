import os
from transformers import pipeline, set_seed
from diffusers import StableDiffusionPipeline

prompt = os.getenv("PROMPT")
if not prompt:
  print("No prompt provided, generating one.")
  generator = pipeline('text-generation', model='gpt2-large')
  promptPrompt = "A 40 character description of a unique cat:"
  res = generator(promptPrompt, max_length=40, num_return_sequences=1)

  prompt = res[0]["generated_text"][len(promptPrompt):]

print(f"Prompt: {prompt}")
# exit(1)

# set up a stable diffusion pipeline
pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1-base")

pipe = pipe.to("mps")
image = pipe(f"cat, {prompt}").images[0]

image.save("cat.jpg")
with open('prompt.txt', 'w') as f:
  f.write(prompt)
