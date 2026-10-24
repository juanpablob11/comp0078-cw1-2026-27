"""Export source files for Moodle; refuse empty notebook templates."""
import ast
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
INCLUDE_DIRS = ("notebooks", "src", "scripts", "docs")
INCLUDE_ROOT = ("README.md", "requirements.txt", "data/README.md")


def has_implementation(path):
    notebook = json.loads(path.read_text(encoding="utf-8"))
    for cell in notebook["cells"]:
        if cell["cell_type"] != "code":
            continue
        source = cell["source"]
        source = source if isinstance(source, str) else "".join(source)
        try:
            # Imports, comments and pass alone do not implement an experiment.
            nodes = ast.parse(source).body
            if any(not isinstance(node, (ast.Import, ast.ImportFrom, ast.Pass)) for node in nodes):
                return True
        except SyntaxError:
            # Notebook magics require manual review; another Python cell must
            # still provide an implementation for this packaging guard.
            continue
    return False


def build():
    notebooks = sorted((ROOT / "notebooks").glob("*.ipynb"))
    unfinished = [path.name for path in notebooks if not has_implementation(path)]
    if len(notebooks) != 3 or unfinished:
        raise SystemExit("No archive created. Implement and review all notebooks first: " + ", ".join(unfinished))
    selected = {ROOT / name for name in INCLUDE_ROOT}
    for folder in INCLUDE_DIRS:
        for path in (ROOT / folder).rglob("*"):
            if path.is_file() and not path.is_symlink() and path.suffix in {".py", ".ipynb", ".md", ".txt"}:
                if not {"__pycache__", ".ipynb_checkpoints"}.intersection(path.parts):
                    selected.add(path)
    destination = ROOT / "dist" / "comp0078-cw1-code.zip"
    destination.parent.mkdir(exist_ok=True)
    if destination.exists():
        raise SystemExit(f"Archive already exists; move it aside before rebuilding: {destination}")
    with ZipFile(destination, "w", compression=ZIP_DEFLATED) as archive:
        for path in sorted(selected):
            archive.write(path, path.relative_to(ROOT).as_posix())
    print(f"Created {destination}")
    print("Review identification, dataset instructions and completeness before submission.")


if __name__ == "__main__":
    build()
