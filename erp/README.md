# ERP Skeleton for Musical Instrument Cases

Este proyecto contiene un ejemplo muy básico inspirado en la filosofía DDD. El módulo `catalog` representa un servicio autónomo encargado de manejar categorías y productos.

## Estructura
- `domain` contiene los modelos de negocio usando SQLAlchemy.
- `application` define servicios que coordinan la lógica de negocio.
- `infrastructure` implementa la conexión a la base de datos y los repositorios.

Cada módulo debería contar con su propia base de datos; en este caso el `catalog` utiliza un archivo SQLite `catalog.db`.

## Ejemplo rápido

```bash
python -m erp.catalog.main
```

El script inicializa la base de datos y crea algunas categorías y productos de ejemplo.

A futuro, cada módulo puede exponerse como microservicio y comunicarse mediante sistemas de mensajería como Kafka, RabbitMQ o Pulsar.
