from .infrastructure.database import get_engine, get_session
from .domain.models import Base
from .infrastructure.repositories import CategoryRepository, ProductRepository
from .application.services import CatalogService


def init_db(engine):
    Base.metadata.create_all(engine)


def main():
    engine = get_engine()
    Session = get_session(engine)
    init_db(engine)

    with Session() as session:
        cat_repo = CategoryRepository(session)
        prod_repo = ProductRepository(session)
        service = CatalogService(cat_repo, prod_repo)

        guitars = service.create_category("Guitarras")
        electric = service.create_category("Guitarras Electricas", guitars)
        acoustic = service.create_category("Guitarras Acusticas", guitars)

        service.create_product("Estuche Vintage para Stratocaster", electric)
        service.create_product("Estuche de lona para acustica", acoustic)

        for product in service.list_products():
            print(product)


if __name__ == "__main__":
    main()
