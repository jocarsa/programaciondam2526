#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from pathlib import Path

TARGET_FOLDER = "101-Ejercicios"
SIBLING_FOLDER = "301-Resumen"
RESUMEN_FILE = "001-Resumen.md"


def process_tree(root: Path):
    for current_root, dirs, files in os.walk(root):
        for d in dirs:
            if d == TARGET_FOLDER:
                ejercicios_path = Path(current_root) / d
                parent = ejercicios_path.parent
                resumen_path = parent / SIBLING_FOLDER

                if not resumen_path.exists():
                    resumen_path.mkdir()
                    print(f"Created folder: {resumen_path}")

                    resumen_file = resumen_path / RESUMEN_FILE
                    resumen_file.touch()
                    print(f"Created file:   {resumen_file}")
                else:
                    print(f"Exists:         {resumen_path}")


def main():
    root = Path.cwd()
    process_tree(root)


if __name__ == "__main__":
    main()

