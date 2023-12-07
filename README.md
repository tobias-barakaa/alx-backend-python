# Variable Annotations in Python

Variable annotations in Python are a way to provide hints about the expected types of variables. While Python is dynamically typed, meaning that you don't have to explicitly declare the type of a variable, variable annotations can provide hints to tools and other developers about the intended types.

## Basic Variable Annotations

You can use variable annotations to specify the type of a variable. For example:

```python
# Variable annotations
name: str = "John"
age: int = 25
is_student: bool = False.

# In the above example, name: str, age: int, and is_student: bool indicate the expected types for each variable.

## Annotations in Function Body

# Annotations in function body
def calculate_area(radius: float) -> float:
    pi: float = 3.14159
    area: float = pi * radius ** 2
    return area

## List and Dict Annotations

from typing import List, Dict

# List annotation
numbers: List[int] = [1, 2, 3, 4]

# Dict annotation
person: Dict[str, Union[str, int]] = {"name": "Alice", "age": 30}


## Optional Types

from typing import Optional

# Optional type annotation
email: Optional[str] = get_user_email(user_id)

 
