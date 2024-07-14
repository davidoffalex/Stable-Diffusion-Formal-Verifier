# Stable-Diffusion-Formal-Verifier
This tool consists of three files executed through a bash script. The executed files are:
1. imageanalyzer.py : analyzes all images in a given directory and provides detailed descriptions for each image. 
2. determineviolations.py : reads the list of LTLs and determines which images, if any, violate the LTLs. Also determines which LTL is violates for each image.
3. removeviolations.py : Optional. Removes the violating images. 

## Installations
Ensure that the following are installed using the "pip install" command in your python environment.
1. openai
2. requests

## Other 
You will need to replace the dirctory path to your API key for imageanalyzer.py and determineviolations.py. 