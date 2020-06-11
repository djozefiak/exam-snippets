from fpdf import FPDF
from math import ceil

from definitions import *

class CellRenderer(FPDF):
	def __init__(self, total_cells):
		super().__init__(orientation="P", unit="mm", format="A4")
		self.set_margins(left=10, top=10, right=10)
		self.set_auto_page_break(auto=True, margin=MARGIN)
		self.add_page()
		self.set_font(family="Arial", size=10)
		self.total_cells = total_cells
		self.total_pages = ceil(total_cells / CELLS_PER_PAGE)
		self.cell_counter = 0
		self.total_cell_counter = 0

	def set_style(self, style, size=10):
		self.set_font(family="Arial", style=style, size=size)

	def render_cell(self, first_name, last_name, pin, comment):
		if self.total_cell_counter >= self.total_cells:
			raise RuntimeError(f"renderer exhausted, maximum cell count of {self.total_cells} reached")

		# store current x and y coordinates
		x, y = self.x, self.y
		
		# draw outer border for current cell
		self.rect(x=x, y=y, w=CELL_WIDTH, h=CELL_HEIGHT, style="")

		self.set_style("B")
		self.cell(w=SUB_CELL_WIDTH_A, h=SUB_CELL_HEIGHT, txt="Nachname:", align="L", ln=0) # move next position to the right of the cell
		self.set_style("")
		if len(last_name) >= 22:
			self.set_style("", 8)
		self.cell(w=SUB_CELL_WIDTH_B, h=SUB_CELL_HEIGHT, txt=last_name, align="L", ln=2) # move next position below
		self.x = x # restore x coordinate to draw next cell on same width as the first cell
		
		self.set_style("B")
		self.cell(w=SUB_CELL_WIDTH_A, h=SUB_CELL_HEIGHT, txt="Vorname:", align="L", ln=0)
		self.set_style("")
		if len(first_name) >= 22:
			self.set_style("", 8)
		self.cell(w=SUB_CELL_WIDTH_B, h=SUB_CELL_HEIGHT, txt=first_name, align="L", ln=2)
		self.x = x
		
		self.set_style("B")
		self.cell(w=SUB_CELL_WIDTH_A, h=SUB_CELL_HEIGHT, txt="PIN:", align="L", ln=0)
		self.set_style("")
		self.cell(w=SUB_CELL_WIDTH_B, h=SUB_CELL_HEIGHT, txt=pin, align="L", ln=2)
		self.x = x

		self.cell(w=CELL_WIDTH, h=SUB_CELL_HEIGHT, txt=comment, align="C", ln=0)
		
		if self.cell_counter == 0:
			# draw current page when drawing the first cell of the page
			self.text(x=2, y=5, txt=f"Seite {self.page_no()} / {self.total_pages}")

		if self.cell_counter % CELLS_PER_ROW == CELLS_PER_ROW - 1:
			# reached end of the current line / row
			self.ln()
		else:
			self.y = y # restore y coordinate to draw next cell on the same height
		
		if self.cell_counter == CELLS_PER_PAGE - 1:
			# reached end of the current page
			self.add_page()
			self.cell_counter = 0
		else:
			self.cell_counter += 1
		self.total_cell_counter += 1
