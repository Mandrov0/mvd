import requests

url = f'https://kidkodSchool.github.io/welcome.html'

response = requests.get(url)

print(response.content)

with open("python_is_cool.html", 'wb') as f:
    f.write(response.content)