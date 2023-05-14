import re
import urllib.parse
import argparse

def replace_url_in_query_params(url, replace_url, replace_all):
    # decode the input URL if it is url encoded
    decoded_url = urllib.parse.unquote(url)

    # replace the URL in query parameters
    if replace_all:
        # Replace all parameter values with the replace URL
        query_params = urllib.parse.parse_qs(urllib.parse.urlparse(decoded_url).query)
        for key in query_params:
            query_params[key] = [replace_url]
        modified_query = urllib.parse.urlencode(query_params, doseq=True)
        modified_url = re.sub(r'\?.*', '?' + modified_query, decoded_url)
    else:
        # Replace only the URL in query parameters
        modified_url = re.sub(r'((?:^|&)[^&=]*?=)https?://[^&]*', r'\1' + replace_url, decoded_url)
    
    return modified_url

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Replace URL in query parameters')
    parser.add_argument('-f', '--file', type=str, required=True, help='Input file containing URLs')
    parser.add_argument('-u', '--url', type=str, required=True, help='Server URL, like burp collaborator url')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output file to save modified URLs')
    parser.add_argument('-A', '--replace-all', action='store_true', help='Replace all parameter values with the replace URL')
    args = parser.parse_args()

    with open(args.file, 'r') as f:
        urls = f.readlines()

    with open(args.output, 'w') as f:
        for url in urls:
            updated_url = replace_url_in_query_params(url.strip(), args.url, args.replace_all)
            f.write(updated_url + '\n')
            print(updated_url)


            # Check list completed