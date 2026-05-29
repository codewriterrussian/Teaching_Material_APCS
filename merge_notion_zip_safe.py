from pathlib import Path
import zipfile
import shutil
import re

ROOT = Path.cwd()
SRC_DIR = ROOT / "student_handouts"
OUT_DOC_DIR = ROOT / "student_handouts"
OUT_IMG_DIR = ROOT / "assets" / "images" / "notion_exports"
TMP_DIR = ROOT / ".tmp_notion_exports"

DOC_EXTS = {".md", ".markdown", ".html"}
IMG_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp"}

OUT_DOC_DIR.mkdir(parents=True, exist_ok=True)
OUT_IMG_DIR.mkdir(parents=True, exist_ok=True)
TMP_DIR.mkdir(parents=True, exist_ok=True)


def safe_name(name: str) -> str:
    name = name.replace("\\", "/").split("/")[-1]
    name = re.sub(r"[^\w.\-() 一-龥ぁ-んァ-ン一-龯：]+", "_", name)
    name = re.sub(r"_+", "_", name).strip("_")
    return name or "unnamed"


def extract_zip_safely(zip_path: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path) as zf:
        for info in zf.infolist():
            if info.is_dir():
                continue

            original_name = info.filename
            filename = safe_name(original_name)
            target = out_dir / filename

            # Avoid overwrite
            if target.exists():
                stem = target.stem
                suffix = target.suffix
                i = 1
                while True:
                    candidate = out_dir / f"{stem}_{i}{suffix}"
                    if not candidate.exists():
                        target = candidate
                        break
                    i += 1

            with zf.open(info) as src, open(target, "wb") as dst:
                shutil.copyfileobj(src, dst)

            print(f"[EXTRACT] {zip_path.name} :: {original_name} -> {target.name}")


def recursively_extract_nested_zips(work_dir: Path):
    while True:
        zip_files = list(work_dir.rglob("*.zip"))
        if not zip_files:
            break

        for z in zip_files:
            nested_dir = z.with_suffix("")
            print(f"[NESTED] {z}")
            extract_zip_safely(z, nested_dir)
            z.rename(z.with_suffix(".zip.extracted"))


for zip_path in sorted(SRC_DIR.glob("*.zip")):
    base = zip_path.stem
    work = TMP_DIR / base

    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)

    print()
    print(f"[INFO] processing: {zip_path.name}")

    extract_zip_safely(zip_path, work)
    recursively_extract_nested_zips(work)

    docs = []
    imgs = []

    for f in work.rglob("*"):
        if not f.is_file():
            continue

        ext = f.suffix.lower()
        if ext in DOC_EXTS:
            docs.append(f)
        elif ext in IMG_EXTS:
            imgs.append(f)

    for doc in docs:
        target_name = f"{base}_{safe_name(doc.name)}"
        target = OUT_DOC_DIR / target_name
        print(f"[DOC] {doc.name} -> student_handouts/{target_name}")
        shutil.copy2(doc, target)

    img_target_dir = OUT_IMG_DIR / base
    img_target_dir.mkdir(parents=True, exist_ok=True)

    for img in imgs:
        target_name = safe_name(img.name)
        target = img_target_dir / target_name

        if target.exists():
            stem = target.stem
            suffix = target.suffix
            i = 1
            while True:
                candidate = img_target_dir / f"{stem}_{i}{suffix}"
                if not candidate.exists():
                    target = candidate
                    break
                i += 1

        print(f"[IMG] {img.name} -> assets/images/notion_exports/{base}/{target.name}")
        shutil.copy2(img, target)

print()
print("[INFO] done.")
print("[INFO] Check with:")
print("tree student_handouts assets/images/notion_exports")
