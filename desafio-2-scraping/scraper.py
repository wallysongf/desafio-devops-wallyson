import requests

def handler(event, context):
    url = event.get("url", "https://poder360.com.br")
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 403:
            return {
                "status": "blocked",
                "reason": "IP bloqueado",
                "retry": True
            }
        elif response.ok:
            return {
                "status": "success",
                "data_length": len(response.text)
            }
        else:
            return {
                "status": "error",
                "code": response.status_code
            }
    except Exception as e:
        return {
            "status": "exception",
            "error": str(e)
        }
