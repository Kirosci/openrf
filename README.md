# OpenRf
A Python tool for replacing URLs in query parameters.

# Description
OpenRf is a Python tool for replacing URLs in query parameters in a batch of URLs. This tool can be useful for security researchers or penetration testers who need to modify a large number of URLs for testing purposes.
The tool takes an input file containing a list of URLs, replaces the specified URL in the query parameters with a new URL, and outputs the modified URLs to an output file. The user can choose to replace all instances of the URL in the query parameters or only the URL itself.
Additionally, the tool can make a request to each modified URL and print the response code, with the option to colorize the output based on the HTTP status code.

# Installation
To use URL Parameter Replacer, you must have Python 3.x and the requests module installed. You can install the requests module using pip:

pip install -r requirements.txt

## Flag (-A)
# If used (-A),
It will replace each and every parameter's value to your url.
# If not used,
It will only replace the values of the parameters that contain url as values.
## Flag -R:
# If used (-R),
It will also send request to the modified urls and respectively show the response. 
# If not used,
It will just give you the modifed requests.


##Ex:
python3 -f urls.txt -u burpcollaborator.link -A -R
