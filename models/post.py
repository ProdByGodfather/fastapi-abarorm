from abarorm import SQLiteModel
from abarorm import fields
from config.db import db_config

class Category(SQLiteModel):
   title = fields.CharField(max_length=200)
   class Meta:
      db_config = db_config


class Post(SQLiteModel):
   title = fields.CharField(max_length=200)
   content = fields.TextField()
   create_date = fields.DateTimeField(auto_now_add=True)
   category = fields.ForeignKey(Category, on_delete='CASCADE')
   best = fields.BooleanField()
   class Meta:
      db_config = db_config
      table_name = 'posts'