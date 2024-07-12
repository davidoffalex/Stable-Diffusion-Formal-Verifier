import os
import json
import openai
import base64
from openai import OpenAI
from PIL import Image

#Set OpenAI API key
def read_api_key(api_path):
    with open(api_path, 'r') as file:
        api_key = file.read().strip()
    return api_key

file_path_api = '/home/alexda/projects/openai_api_key.txt' # Path to api key
my_api_key = read_api_key(file_path_api)

client = OpenAI(api_key = my_api_key)

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def generate_image_descriptions(image_directory, output_file):
    descriptions = {}

    for filename in os.listdir(image_directory):
        base64_image = encode_image(filename)
        # headers = {
        #     "Content-Type": "application/json",
        #     "Authorization": f"Bearer {api_key}"
        # }
        # Generate a description using the GPT API Prompt: "Please provide a detailed description of this image"
        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "text": "Please provide a detailed description of this image"
                },
                {
                    "type": "image-url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64_image}"
                    }
                }
            ],
            "max_tokens": 300
        }
        # Extract the description from the response
        description = response['data'][0]['text']
        descriptions[filename] = description

    # Save the descriptions to a JSON file
    with open(output_file, 'w') as json_file:
        json.dump(descriptions, json_file, indent=4)
    
# Example usage
image_directory = 'home/alexda/projects/Stable-Diffusion-Formal-Verifier/images' # Path to the image directory
output_file = 'home/alexda/projects/Stable-Diffusion-Formal-Verifier/outputs/descriptions.json' # Path to output file
generate_image_descriptions(image_directory, output_file)
