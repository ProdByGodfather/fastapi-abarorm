from fastapi import APIRouter
from models.post import Post


router = APIRouter()


@router.get("/")
def all_posts():
   posts = Post.all()
   return {"posts": posts}


@router.post("/")
def create_post(title: str, content:str, category_id: int, best: bool):
   Post.create(title=title, content=content, category=category_id, best=best)
   return {'post': "OK"}


@router.get('/{id}/')
def get_post(id: int):
   post = Post.get(id=id)
   if not post:
      return {"error": "Post not found"}
   
   return {"post": post}


@router.delete("/{id}/")
def delete_post(id: int):
   post = Post.get(id=id)
   print(post)
   if not post:
      return {"error": "Post not found"}
   
   Post.delete(id=id)
   return {'post': "Deleted"}

@router.put('/{id}/')
def update_post(id: int, title: str = None, content: str = None, category_id: int = None, best: bool = None):
   post = Post.get(id=id)
   if not post:
      return {"error": "Post not found"}
   
   if title:
      post.title = title
   if content:
      post.content = content
   if category_id:
      post.category = category_id
   if best is not None:
      post.best = best
   
   post.save()
   return {'post': "Updated"}