# Stable-Diffusion-Formal-Verifier
This tool consists of two python files executed sequentially. The executed files are:
1. imageanalyzer.py : analyzes all images in a given directory and provides detailed descriptions for each image. 
2. determineviolations.py : reads the list of LTLs and determines which images, if any, violate the LTLs. Also determines which LTL is violated for each image.

Running sdfv_run.py will automatically run both scripts sequentially without pausing. If you do not wish to execute both scripts at once (but rather execute the scripts one at a time), run imageanalyzer.py first, followed by determineviolations.py if satisfied with the results of imageanalyzer.py. 

## Installations
Ensure that the following are installed using the "pip install" command in your python environment.
1. openai
2. requests

## Preparing the LTLs
Following the format of the example ltl_formulas.txt, enter the following information into ltl_formulas.txt: 
1. All propositions and their definitions.
2. All operators used and their definitions. 
3. The list of LTLs

## Other 
You will need to replace the directory path to your API key for imageanalyzer.py and determineviolations.py. 