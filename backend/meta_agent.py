#!/usr/bin/env python3
import sys
from pathlib import Path
from app.modules.meta_ai import improve_python_code

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Verwendung: python scripts/meta_agent.py datei.py")
        raise SystemExit(2)
    path = Path(sys.argv[1])
    result = improve_python_code(path.read_text(encoding="utf-8"))
    print(result["message"])
