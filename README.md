Prueba eDarkStore

Este proyecto implementa dos funciones Lambda utilizando el framework Serverless:

1. **Función Lambda para obtener la UF**: Una función POST que obtiene el valor de la UF y lo guarda en un archivo PDF dentro de un bucket en S3.
2. **Función Lambda para obtener el valor del dólar (No implementada)**: Una función que debería ejecutarse con un schedule o cron para obtener el valor del dólar y guardarlo en DynamoDB. No se pudo implementar debido a problemas con el plugin de DynamoDB local.

## Requisitos

- **Python**: Utilizado para ejecutar el proyecto.
- **Serverless Framework v3**: Para la gestión de funciones Lambda.
- **Plugins Serverless**:
  - `serverless-offline`: Para ejecutar las funciones de forma local.
  - `serverless-s3-local`: Para emular el servicio de S3 localmente.
  - `serverless-dynamodb-local`: Para emular el servicio de DynamoDB localmente (hubo problemas con este plugin).

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/keloco23/eds-test.git
cd eds-test
```

### Instalar dependencias

No se encuentra la carpeta node_modules, por tanto es necesario instalar npm junto a sus dependencias

```bash
npm install
```

### Instalar plugins de Serverless

Instalar los siguientes plugins para la ejecución local:

- **serverless-offline**: Para ejecutar el proyecto localmente.
- **serverless-s3-local**: Para emular S3 localmente.
- **serverless-dynamodb-local** (No implementado por problemas en DynamoDB).

```bash
npm install serverless-offline --save-dev
npm install serverless-s3-local --save-dev
npm install serverless-dynamodb-local --save-dev
```

### Configuración de `serverless.yml`

El archivo `serverless.yml` ya está configurado con las funciones Lambda y los recursos necesarios para ejecutar el proyecto localmente.

### Iniciar proyecto localmente

Para ejecutar las funciones Lambda localmente, utiliza el siguiente comando:

```bash
npx sls offline start
```

### Función lambda UF

Una vez que el proyecto esté corriendo localmente, puedes probar la función Lambda de la UF utilizando Postman. La función acepta una petición POST y guarda un archivo PDF con el valor de la UF en un bucket S3 local.

### Función del Dólar (No implementada)

La funcionalidad para obtener el valor del dólar y guardarlo en DynamoDB no fue implementada debido a problemas con el plugin de DynamoDB local. Sin embargo, hay codigo presente mostrando su estructura y lógica detras.
