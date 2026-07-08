from pathlib import Path
import shutil


def publish(project_root: Path) -> None:
    """
    outputs/html klasöründe üretilen site dosyalarını
    GitHub Pages'in yayınladığı docs klasörüne kopyalar.
    """

    source_dir = project_root / "outputs" / "html"
    target_dir = project_root / "docs"

    if not source_dir.exists():
        raise FileNotFoundError(f"Kaynak klasör bulunamadı: {source_dir}")

    target_dir.mkdir(parents=True, exist_ok=True)

    for item in source_dir.iterdir():
        target_path = target_dir / item.name

        if item.is_dir():
            if target_path.exists():
                shutil.rmtree(target_path)
            shutil.copytree(item, target_path)
        else:
            shutil.copy2(item, target_path)