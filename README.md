# 📦 API de Facturas – Sistema Corporativo

¡Bienvenido/a a la API de Facturación! Esta API permite consultar facturas emitidas desde el sistema empresarial, ideal para integraciones móviles, web o de escritorio.

---

## 📍 Endpoint Base

```
https://tuservidor.com/api/v1
```

---

## 🔐 Autenticación

Esta API utiliza **Bearer Token** para autenticación. Debes enviar tu token de acceso en el encabezado `Authorization`.

### 🔑 Ejemplo:

```
Authorization: Bearer TU_TOKEN_AQUI
```

---

## 📄 Obtener Facturas

### ➤ Endpoint

```
GET /motos/facturas
```

### 🧪 Ejemplo en `curl`

```bash
curl -X GET "https://tuservidor.com/api/v1/motos/facturas" \
  -H "Authorization: Bearer TU_TOKEN_AQUI" \
  -H "Content-Type: application/json"
```

### 📬 Respuesta esperada

```json
{
  "facturas": [
    {
      "numero": "FA-000001",
      "fecha": "2025-04-21",
      "cliente": "JUAN PÉREZ",
      "items": [
        {
          "producto": "PRODUCTO XYZ",
          "cantidad": 1.0,
          "precio": 100.0,
          "total": 116.0
        }
      ]
    }
  ]
}
```

---

## 🧰 Cómo probarlo en Postman

1. Abre [Postman](https://www.postman.com/)
2. Crea una nueva colección llamada `API Facturación`
3. Agrega una nueva petición:
   - **Método:** `GET`
   - **URL:** `https://tuservidor.com/api/v1/motos/facturas`
4. En la pestaña **Headers**, añade:
   - `Authorization: Bearer TU_TOKEN_AQUI`
   - `Content-Type: application/json`
5. Haz clic en **Send** y revisa la respuesta 🎉

---

## ⚠️ Notas importantes

- El token debe ser generado desde el sistema backend.
- Actualmente solo se permiten consultas (método GET).
- Esta API puede ser usada en apps móviles, sistemas web, CRMs, etc.
- El entorno puede ser `test` o `producción` según tu configuración.