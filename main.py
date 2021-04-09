from func.save_get_file import *
import requests

urls = get_array_from_file_lines("data/link")
data = ""
error = ""
for url in urls:
    print(url)
    try:
        status = requests.get(url).status_code
        data += str(status) + " " + url + "\n"
    except:
        error += url + "\n"

save_string_to_file("data/result", data.strip())
save_string_to_file("data/error", error.strip())