import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QLineEdit, QWidget, QHBoxLayout, QLabel, QAction, QFileDialog
from PyQt5.QtGui import QImage, QFont, QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import QRect, Qt, QPoint, QTimer
import math

# f = open("past.txt", 'r')
# past = f.read()
# f.close()

# f = open("present.txt", 'r')
# present = f.read()
# f.close()

# f = open("future.txt", 'r')
# future = f.read()
# f.close()


class Window(QMainWindow):

	def __init__(self):
		super().__init__()
		self.title ="Drawing a Writing System"
		self.left = 500
		self.top = 200
		self.width = 800
		self.height = 800
		self.setGeometry(self.left, self.top, self.width, self.height)	
		self.image = QImage(self.size(), QImage.Format_ARGB32)
		self.image.fill(Qt.black)
		self.top_image = QImage(self.size(), QImage.Format_ARGB32)
		self.top_image.fill(QColor(0,0,0,0))
		# self.merge_image = QImage(self.size(), QImage.Format_ARGB32)

		self.font = QFont("IBM Plex Mono",16) 
		self.font.setStyleHint(QFont.TypeWriter)


		self.font_bold = QFont("IBM Plex Mono",16) 
		self.font_bold.setBold(True)
		self.past_count = 0
		self.future_count = 0
		self.present_count = 0

		self.timer_count=0
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.showTime)
		self.timer.start(1000)

		f = open("past.txt", 'r')
		self.past = f.read()
		f.close()

		f = open("present.txt", 'r')
		self.present = f.read()
		f.close()

		f = open("future.txt", 'r')
		self.future = f.read()
		f.close()


		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu("File")
		oracle_mode = mainMenu.addMenu("Oracle Mode")

		saveAction = QAction("Save",self)
		saveAction.setShortcut("Ctrl+S")
		fileMenu.addAction(saveAction)
		saveAction.triggered.connect(self.save)

		clearAction = QAction("Clear", self)
		clearAction.setShortcut("Ctrl+C")
		fileMenu.addAction(clearAction)
		clearAction.triggered.connect(self.clear)

		pastAction = QAction( "Past", self)
		oracle_mode.addAction(pastAction)
		pastAction.triggered.connect(self.setPast)

		presentAction = QAction( "Present", self)
		oracle_mode.addAction(presentAction)
		presentAction.triggered.connect(self.setPresent)

		futureAction = QAction( "Future", self)
		oracle_mode.addAction(futureAction)
		futureAction.triggered.connect(self.setFuture)

		self.state = self.present

	def showTime(self):
		self.timer_count += 1
		print(self.timer_count)
		# if self.timer_count % 2 == 0:
		

	def paintEvent(self,event):

		# # if self.timer_count == 0:
		# # 	self.grid_init()


		painter = QPainter(self)
		painter.drawImage(self.rect(), self.image)
		painter.drawImage(self.rect(),self.top_image)

	# def grid_init(self):
	# 	canvas = QPainter(self)
	# 	canvas.drawImage(self.rect(), self.image)
	# 	canvas.setFont(self.font)
	# 	canvas.setPen(Qt.white)
	# 	canvas.setBrush(Qt.white)
	# 	for i in range(35):
	# 		for j in range(35):
	# 			canvas.drawText(QPoint(i*20, j*20), str(past[i+j*35]))
	# 		# print(i,j)


	def mousePressEvent(self, event):

		if (event.buttons() == Qt.LeftButton):
			# print(self.char_count)
			self.lastPoint = event.pos()
			x = event.pos().x()
			y = event.pos().y()
			# print(self.lastPoint)
			brush_radius = 180
			canvas = QPainter(self.top_image)
			canvas.drawImage(self.rect(), self.top_image)
			# canvas.drawText(event.pos().x()-event.pos().x()%20,event.pos().y()-event.pos().y()%20,content[1260+self.char_count]) #1260 is taken from after canvas.drawText function
			# print(self.char_count)

			minx = self.toGrid(x - brush_radius)
			maxx = self.toGrid(x + brush_radius)
			miny = self.toGrid(y - brush_radius)
			maxy = self.toGrid(y + brush_radius)

			for circle_y in range(miny, maxy, 20):

				try:
					circle_x = self.toGrid(math.sqrt(brush_radius**2 - (circle_y - y)**2))
					# print(circle_x)
					offsets = range(-int(circle_x), int(circle_x), 20)
					for offset in offsets:
						ax = x + offset
						canvas.setPen(Qt.black)
						canvas.setBrush(QBrush(Qt.black, Qt.SolidPattern))
						canvas.drawRect(self.toGrid(ax) - 4, self.toGrid(circle_y) - 15, 20, 20)
						canvas.setFont(self.font)
						canvas.setPen(Qt.white)
						canvas.setBrush(Qt.white)
						canvas.drawText(self.toGrid(ax), self.toGrid(circle_y), self.content())
						
				except:
					print('oops')

			self.update()

	def toGrid(self, val):
		return val - (val % 20)

	def save(self):
		filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

		if filePath == "":
			return

		# merge_image = QImage(self.size(), QImage.Format_ARGB32)
		# painter = QPainter(self)
		# painter.drawImage(self.rect(), self.image)
		# painter.drawImage(self.rect(),self.top_image)
		merge_image.save(filePath)

	def clear(self):
		self.top_image.fill(QColor(0,0,0,0))
		self.update()

	def content(self):
		if self.state == self.past:
			self.past_count += 1
			# print('counting past')
			return self.state[self.past_count]
		if self.state == self.present:
			self.present_count += 1
			# print('counting present')
			# print(self.present_count)
			return self.state[self.present_count]

		if self.state == self.future:
			self.future_count += 1
			# print('counting future')
			return self.state[self.future_count]


	def setPast(self):
		self.state=self.past


	def setPresent(self):
		self.state=self.present


	def setFuture(self):
		self.state=self.future


def run():
	if __name__ == '__main__':
		app = QApplication(sys.argv)
		window = Window()
		window.show()
		sys.exit(app.exec_())

run()