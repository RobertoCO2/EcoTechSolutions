import requests


class ClienteAPI:

    def __init__(self, url_base="https://mindicador.cl/api"):
        self.url_base = url_base

    def obtener_indicador(self, indicador="dolar"):
        """Consulta un indicador económico (ej. 'dolar' o 'uf') y devuelve su valor actual."""
        try:
            url = f"{self.url_base}/{indicador}"
            # Encabezado para identificar la petición como navegador
            headers = {"User-Agent": "Mozilla/5.0"}
            respuesta = requests.get(url, headers=headers, timeout=10)
            respuesta.raise_for_status()

            datos = respuesta.json()
            serie = datos.get("serie", [])

            if not serie:
                return None
            # Obtenemos el valor más reciente de la lista (posición 0)
            return serie[0]["valor"]

        except requests.Timeout:
            print(
                " Error: El servicio de la API demoró demasiado en responder."
            )
            return None
        except requests.ConnectionError:
            print(" Error: Sin conexión a internet para consultar la API.")
            return None
        except requests.RequestException as e:
            print(f" Error al consultar la API: {e}")
            return None


if __name__ == "__main__":
    cliente = ClienteAPI()
    valor = cliente.obtener_indicador("dolar")
    print(f"Valor del dolar hoy: ${valor}")
