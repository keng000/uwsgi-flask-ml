from pathlib import Path


class PathManager:
    ROOT = Path(__file__).absolute().parent
    MODELS = ROOT / "models"
