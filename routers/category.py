from fastapi import APIRouter
from models.post import Category


router = APIRouter()


@router.get("/")
def all_posts():
   categories = Category.all()
   return {"categories": categories}


@router.post("/")
def create_post(title: str):
   category = Category.create(title=title)
   return {'Catgegory': category}


@router.get('/{id}/')
def get_category(id: int):
   category = Category.get(id=id)
   if not category:
      return {"error": "Category not found"}
   
   return {"category": category}
   

@router.delete('/{id}/')
def delete_category(id: int):
   category = Category.get(id=id)
   if not category:
      return {"error": "Category not found"}
   
   Category.delete(id=id)
   return {'category': "Deleted"}

@router.put('/{id}/')
def update_category(id: int, title: str):
   category = Category.get(id=id)
   if not category:
      return {"error": "Category not found"}
   
   category.title = title
   category.save()
   return {'category': "Updated"}