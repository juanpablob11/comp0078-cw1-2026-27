"""Check notebook structure without running experiments (standard library only)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check(path):
    notebook = json.loads(path.read_text(encoding="utf-8"))
    if notebook.get("nbformat") != 4 or not isinstance(notebook.get("cells"), list):
        raise ValueError(f"{path.name}: expected a version-4 notebook")
    ids = set()
    implemented = 0
    for cell in notebook["cells"]:
        if cell.get("cell_type") not in {"code", "markdown", "raw"}:
            raise ValueError(f"{path.name}: unknown cell type")
        cell_id = cell.get("id")
        if not cell_id or cell_id in ids:
            raise ValueError(f"{path.name}: missing or duplicate cell id")
        ids.add(cell_id)
        if not isinstance(cell.get("metadata"), dict):
            raise ValueError(f"{path.name}: invalid cell metadata")
        source = cell.get("source")
        if not isinstance(source, (str, list)):
            raise ValueError(f"{path.name}: invalid cell source")
        text = source if isinstance(source, str) else "".join(source)
        if cell["cell_type"] == "code":
            if not isinstance(cell.get("outputs"), list) or "execution_count" not in cell:
                raise ValueError(f"{path.name}: invalid code-cell fields")
            implemented += bool(text.strip())
    return implemented


if __name__ == "__main__":
    paths = sorted((ROOT / "notebooks").glob("*.ipynb"))
    if len(paths) != 3:
        raise SystemExit(f"Expected three notebooks; found {len(paths)}")
    for path in paths:
        count = check(path)
        status = "EMPTY TEMPLATE" if count == 0 else f"{count} nonempty code cells"
        print(f"OK {path.name}: {status}")
    print("Structural check only; experiments were not executed.")
