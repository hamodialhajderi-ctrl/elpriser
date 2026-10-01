import requests

def hämta_priser(datum, elområde):
    url = f"https://www.elprisetjustnu.se/api/v1/prices/{datum}_{elområde}.json"
    try:
        svar = requests.get(url)
        print("Statuskod:", svar.status_code)
        print("Svar:", svar.text)
        data = svar.json()
        return data
    except Exception as e:
        print("Något gick fel vid hämtning av priser.")
        print("Riktiga felet:", e)
        return []

resultat = hämta_priser("2026/09-24", "SE3")
print(resultat)  