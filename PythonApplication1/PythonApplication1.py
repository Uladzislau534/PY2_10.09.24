import math
from typing import List


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

floats_cubed = [round(x**3, 3) for x in floats]


long_names = [name for name in names if len(name) >= 5]

product_of_numbers = math.prod(numbers)
