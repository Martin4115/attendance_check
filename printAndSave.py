import labels
from reportlab.graphics import shapes

def draw_label(label, width, height, obj):

	label.add(shapes.String(6, 6, str(obj), fontName="Helvetica", fontSize=25))


def codes2pdf(codes, batch_id):
	specs = labels.Specification(210, 297, 3, 10, 65, 25, corner_radius=2, bottom_padding=5)
	sheet = labels.Sheet(specs, draw_label, border=True)
	for code in codes:
		sheet.add_label(code)
	filename = str(batch_id) + '.pdf'
	sheet.save(filename)
	print("{0:d} label(s) output on {1:d} page(s).".format(sheet.label_count, sheet.page_count))


def codes2txt(codes, batch_id):
	data_to_write = ''
	for code in codes:
		data_to_write += code
		data_to_write += ' '
	f1 = open(str(batch_id) + ".txt",'w')
	f1.write(data_to_write)
	f1.close()