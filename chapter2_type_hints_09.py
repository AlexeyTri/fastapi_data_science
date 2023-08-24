from typing import Any, cast
def f(i: Any) -> Any:
	return i

a = f(10)
print(type(a))

a = cast(str, f("b"))
print(type(a))
