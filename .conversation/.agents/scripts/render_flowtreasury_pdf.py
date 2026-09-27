from pathlib import Path
import fitz

pdf_path = Path("attached_assets/FlowTreasury_prompt__1790498259517.pdf")
output_dir = Path(".agents/outputs/flowtreasury_pdf")
output_dir.mkdir(parents=True, exist_ok=True)

doc = fitz.open(pdf_path)
print(f"pages={doc.page_count}")
for index, page in enumerate(doc):
    pixmap = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
    output_path = output_dir / f"page-{index + 1}.png"
    pixmap.save(output_path)
    print(output_path)