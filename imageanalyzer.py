import os
import json
import openai
import base64
import requests
from openai import OpenAI
from PIL import Image

#Set OpenAI API key
def read_api_key(api_path):
    with open(api_path, 'r') as file:
        api_key = file.read().strip()
    return api_key

file_path_api = '/home/alexda/projects/openai_api_key.txt' # Path to API key [USER ENTERED]
my_api_key = read_api_key(file_path_api)

client = OpenAI(api_key = my_api_key)

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def generate_image_descriptions(image_directory, output_file):
    descriptions = {}

    counter = 0
    for filename in os.listdir(image_directory):
        counter += 1
        print (f"Analzying image:  {counter}")
        
        base64_image = encode_image(os.path.join(image_directory,filename))
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {my_api_key}"
        }
        
        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Please provide a detailed description of this image."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                               "url": f"data:image/png;base64,{base64_image}" 
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 600
        }
        # Extract the description from the response
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        description = response.json()['choices'][0]['message']['content']
        descriptions[filename] = description

    # Save the descriptions to a JSON file
    with open(output_file_path, 'w') as json_file:
        json.dump(descriptions, json_file, indent=4)
    
# Execute the functions
project_directory = os.path.dirname(os.path.abspath(__file__))
image_directory_path = os.path.join(project_directory, 'images') # Path to the image directory
output_file_path = os.path.join(project_directory, 'outputs', 'descriptions.json')
generate_image_descriptions(image_directory_path, output_file_path)
