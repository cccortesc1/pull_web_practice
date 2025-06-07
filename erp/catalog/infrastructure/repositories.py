from typing import List, Optional
from sqlalchemy.orm import Session
from ..domain import models


class CategoryRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, category: models.Category) -> models.Category:
        self.session.add(category)
        self.session.commit()
        return category

    def get_by_id(self, category_id: int) -> Optional[models.Category]:
        return self.session.query(models.Category).filter_by(id=category_id).first()

    def list(self) -> List[models.Category]:
        return self.session.query(models.Category).all()


class ProductRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, product: models.Product) -> models.Product:
        self.session.add(product)
        self.session.commit()
        return product

    def get_by_id(self, product_id: int) -> Optional[models.Product]:
        return self.session.query(models.Product).filter_by(id=product_id).first()

    def list(self) -> List[models.Product]:
        return self.session.query(models.Product).all()
