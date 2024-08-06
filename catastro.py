import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Suprimir sólo las advertencias de solicitud insegura
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def obtener_datos_finca_por_ref_catastral(ref_catastral):

    url = f"https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPRC?RefCat={ref_catastral}"

    try:
        response = requests.get(url, verify=False)  # Desactivar verificación SSL

        response.raise_for_status()  # Esto lanzará una excepción para códigos de estado HTTP no exitosos

        # Verificar si la respuesta es JSON válida
        try:
            datos = response.json()
            return datos
        except requests.exceptions.JSONDecodeError:
            print("Error: la respuesta no es un JSON válido.")
            print("Contenido de la respuesta:", response.text)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return None

# Ejemplo de uso
ref_catastral = "6903204TP7360S0002ZT"  # Reemplaza con la referencia catastral real

datos_finca = obtener_datos_finca_por_ref_catastral(ref_catastral)

if datos_finca:
    print(datos_finca)
else:
    print("No se pudieron obtener los datos de la finca.")