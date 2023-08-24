from typing import Callable, List

ConditionalFunction = Callable[[int], bool]

def filter_list(l: List[int], condition: ConditionalFunction) -> List[int]:
	return [i for i in l if condition(i)] 

def is_even(i: int) -> bool:
	return i % 2 == 0

print(filter_list([1,2,3,4,5,6,7], is_even))
