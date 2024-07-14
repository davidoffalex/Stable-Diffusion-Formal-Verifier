import openai
import json
import requests
import os
from openai import OpenAI

#Set OpenAI API key
def read_api_key(api_path):
    with open(api_path, 'r') as file:
        api_key = file.read().strip()
    return api_key

file_path_api = '/home/alexda/projects/openai_api_key.txt' # Path to api key [USER ENTERED]
my_api_key = read_api_key(file_path_api)

client = OpenAI(api_key = my_api_key)

# Read the LTL formulas from a text file
def read_ltl_formulas(ltl_file_path): 
    with open(ltl_file_path, 'r') as file:
        ltl_formulas = file.readlines()
    return [formula.strip() for formula in ltl_formulas]

# Read image descriptions from a JSON file
def read_image_descriptions(json_file_path): 
    with open(json_file_path, 'r') as file: 
        image_descriptions = json.load(file)
    return image_descriptions

def check_violations(ltl_formulas, image_descriptions):
    violations = {}
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
                    "text": ("Read the list of Linear Temporal Logic (LTL) formulas used to describe the specifications of an entire image dataset."
                                "Additionally, read all image descriptions from the image dataset."
                                "Determine which LTLs were broken, and by which images (if applicable)"
                                "For violating images, print the LTL(s) that were not adhered to"
                                "If an image does not violate any LTLs, do not print anything")
                    },
                    {
                    "type": "text",
                    "text" : f"LTL formulas: {ltl_formulas}, image descriptions: {image_descriptions}"
                    }
                ]
            }
        ],
        "max_tokens": 3500
    }
    # Extract the description from the response
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    violations_description = response.json()['choices'][0]['message']['content']

    # Save the descriptions to a text file
    with open(output_file_path, 'w') as text_file:
        text_file.write(violations_description)

# Execute the functions
project_directory = os.path.dirname(os.path.abspath(__file__))
descriptions_file_path = os.path.join(project_directory, 'outputs', 'descriptions.json')
ltl_formula_path = os.path.join(project_directory, "ltl_formulas.txt")
output_file_path = os.path.join(project_directory,'outputs', 'violations.txt')
check_violations(read_ltl_formulas(ltl_formula_path), read_image_descriptions(descriptions_file_path))
