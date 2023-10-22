from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup
import urllib.parse


class GetTopicId(APIView):
    def get(self, request, format=None):
        productName = request.GET.get("productName")

        if not productName:
            return Response({"error": "Please provide a search query."})
        encoded_string = urllib.parse.quote(productName)
        google_url = f"https://www.google.com/search?q={encoded_string}&tbm=shop"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.87 Safari/537.36"
        }

        response = requests.get(google_url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            price = soup.find("span", {"class": "a8Pemb OFFNJ"})
            name = soup.find("h3", {"class": "tAxDx"})
            image = soup.find("div", {"class": "ArOc1c"}).find_all("img")[0]
            imageSoup = BeautifulSoup(f"{image}", "html.parser")
            img_tag = imageSoup.find("img")
            src = img_tag["src"]
            return Response({"name": name.get_text(), "price": price.get_text()})
        return Response({"error": "error coming"})
