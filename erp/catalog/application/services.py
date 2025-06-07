from ..infrastructure.repositories import CategoryRepository, ProductRepository
from ..domain.models import Category, Product


class CatalogService:
    def __init__(self, category_repo: CategoryRepository, product_repo: ProductRepository):
        self.category_repo = category_repo
        self.product_repo = product_repo

    def create_category(self, name: str, parent: Category = None) -> Category:
        category = Category(name=name, parent=parent)
        return self.category_repo.add(category)

    def create_product(self, name: str, category: Category) -> Product:
        product = Product(name=name, category=category)
        return self.product_repo.add(product)

    def list_categories(self):
        return self.category_repo.list()

    def list_products(self):
        return self.product_repo.list()
