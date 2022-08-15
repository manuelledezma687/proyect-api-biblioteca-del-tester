from pydantic import BaseModel, Field, date
from typing import Optional


class Article(BaseModel):
    title: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example="5 maneras de hacer buen testing"
        ) 
    article: str = Field(
        ..., 
        min_length=1,
        max_length=1000,
        example="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ligula tellus, dictum vel ante vitae, finibus sodales ipsum. Sed id lorem fringilla, placerat sapien a, suscipit velit. Pellentesque ac mattis dolor, id luctus arcu. Nullam malesuada, purus ut auctor imperdiet, massa felis accumsan turpis, a faucibus ante risus ac tellus. Nunc auctor vitae mi id lacinia. In metus magna, lacinia ac imperdiet sed, consectetur pretium purus. Mauris quis accumsan metus, quis maximus dolor. Proin convallis tincidunt semper. Mauris tincidunt sed nulla ut fringilla. Etiam rutrum ipsum sit amet felis venenatis, vitae gravida velit aliquet."
        ) 
    user_id: int = Field(
        ...,
        gt=0
        example=12
        ) 
    date: date = Field(None)