from csv import DictReader
from random import randrange
from renderer import CellRenderer

with open("list.csv", newline="", encoding="utf8") as csv_file:
	reader = DictReader(csv_file, delimiter=";")
	rows = list(reader)
	rows.sort(key=lambda row: row["Nachname"])
	renderer = CellRenderer(total_cells=len(rows))
	for row in rows:
		pin = randrange(1, 10**4)
		pin_str = str(pin).zfill(4)
		renderer.render_cell(first_name=row["Vorname"], last_name=row["Nachname"], pin=pin_str, comment="Viel Erfolg bei der Klausur!")

renderer.output("result.pdf", "F")
