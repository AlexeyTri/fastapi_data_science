def greeting(name: str | None = None) -> str:
	return f"Hello {name if name else 'Anonimus'}"

import printg as pr 

pr.printh()
