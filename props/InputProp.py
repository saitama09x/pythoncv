class InputProp:

	def __init__(self, kilo, height, width, length, qty, pixels, status, life):
		self.kilo = float(kilo)
		self.height = float(height)
		self.width = float(width)
		self.qty = int(qty)
		self.pixels = int(pixels)
		self.status = status
		self.life = int(life)
		self.length = float(length)

	@property
	def kilo(self):
		return self.__kilo

	@kilo.setter
	def kilo(self, kilo):
		self.__kilo = kilo

	@property
	def height(self):
		return self.__height

	@height.setter
	def size(self, height):
		self.__height = height

	@property
	def width(self):
		return self.__width

	@height.setter
	def width(self, width):
		self.__width = width

	@property
	def qty(self):
		return self.__qty

	@qty.setter
	def qty(self, qty):
		self.__qty = qty

	@property
	def image(self):
		return self.__image

	@image.setter
	def image(self, image):
		self.__image = image

	@property
	def pixels(self):
		return self.__pixels

	@pixels.setter
	def pixels(self, pixels):
		self.__pixels = pixels

	@property
	def status(self):
		return self.__status

	@status.setter
	def status(self, status):
		self.__status = status

	@property
	def length(self):
		return self.__length

	@length.setter
	def length(self, length):
		self.__length = length

	@property
	def status(self):
		return self.__life

	@status.setter
	def status(self, life):
		self.__life = life
