import requests


url = "https://sportscore1.p.rapidapi.com/sports"

headers = {
	"X-RapidAPI-Key": "69e94493bbmsh944c5e7d88d9849p11dcb1jsn131894a051c4",
	"X-RapidAPI-Host": "sportscore1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)