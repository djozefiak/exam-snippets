from csv import DictReader

from renderer import CellRenderer

renderer = CellRenderer(total_cells=100)

for _ in range(100):
	renderer.render_cell()

renderer.output("result.pdf", "F")
