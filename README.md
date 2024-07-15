# Stable-Diffusion-Formal-Verifier
This tool consists of two python files executed sequentially. The executed files are:
1. imageanalyzer.py : analyzes all images in a given directory and provides detailed descriptions for each image. 
2. determineviolations.py : reads the list of LTLs and determines which images, if any, violate the LTLs. Also determines which LTL is violates for each image.

Running sdfv_run.py will automatically run both scripts sequentially without stopping. If you do not want to execute both scripts at once (and instead wish to execute the scripts one at a time), run imageanalyzer.py first, followed by determineviolations.py if satisfied with the results of imageanalyzer.py. 

## Installations
Ensure that the following are installed using the "pip install" command in your python environment.
1. openai
2. requests

## Other 
You will need to replace the dirctory path to your API key for imageanalyzer.py and determineviolations.py. 