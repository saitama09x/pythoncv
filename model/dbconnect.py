import pymysql
import datetime

class DB():
	def __init__(self): 		
		self.hostname = 'localhost'
		self.username = 'root'
		self.password = ''
		self.database = 'opencv'
	 	try:
	 		self.conn = pymysql.connect( host=self.hostname, user=self.username, passwd=self.password, db=self.database )
		except pymysql.MySQLError as e:
			print e.args[0]

	def get_login(self, username, password):
		try:
			with self.conn.cursor() as cursor:
				sql = "select * from desktop_user where username = '%s' and password = '%s'" % \
					(username, password)
					
				cursor.execute(sql)
				results = cursor.fetchone()
				return results
		except pymysql.MySQLError as e:
			print e.args[0]

	def insertImage(self, front_image, back_image, side_image):
		try:
			now = datetime.datetime.now()
			format_time = now.strftime("%Y-%m-%d")
			with self.conn.cursor() as cursor:
				sql = "insert into items(front_img, back_img, side_img, datecreated) values('%s', '%s', '%s', '%s')" % \
					(front_image, back_image, side_image, format_time)
				cursor.execute(sql)
				self.conn.commit()

				sql = "select MAX(id) as last_id from items"
				cursor.execute(sql)
  				results = cursor.fetchone()
  				return results
		finally:
  			self.conn.close()

	def insertData(self, prop):
		try:
			with self.conn.cursor() as cursor:
				sql = "insert into items(weight, height, width, length, qty, pixel_counts, status, life) values(%2f, %2f, %2f, %2f, %d, %d, '%s', %d)" % \
					(prop.kilo, prop.height, prop.width, prop.length, prop.qty, prop.pixels, prop.status, prop.life)

				cursor.execute(sql)

				self.conn.commit()
		finally:
  			self.conn.close()

  	def updateData(self, prop, item_id):
  		try:
  			with self.conn.cursor() as cursor:
  				sql = "update items set weight = %2f, height = %2f, width = %2f, qty = %d, pixel_counts = %d, status = '%s', life = %d where id = %d" % \
  					(prop.kilo, prop.height, prop.width, prop.qty, prop.pixels, prop.status, prop.life, item_id)

  				cursor.execute(sql)
  				self.conn.commit()
		finally:
  			self.conn.close()		

  	def get_row(self):
  		try:
  			with self.conn.cursor() as cursor:
  				sql = "select count(*) as max_row from items"
  				cursor.execute(sql)
  				results = cursor.fetchone()
  				return results
  		except pymysql.MySQLError as e:
			print e.args[0]

	def get_last_id(self):
		try:
			with self.conn.cursor() as cursor:
				sql = "select MAX(id) as last_id from items"
				cursor.execute(sql)
  				results = cursor.fetchone()
  				return results
  		except pymysql.MySQLError as e:
			print e.args[0]


  	def get_all(self):
  		try:
  			with self.conn.cursor() as cursor:
  				sql = "select * from items order by id desc"
  				cursor.execute(sql)
  				results = cursor.fetchall()
  				return results
  		except pymysql.MySQLError as e:
			print e.args[0]

	def get_id(self, id):
		try:
			with self.conn.cursor() as cursor:
				sql = "select * from items where id = %d" % \
					(id)

				cursor.execute(sql)
				results = cursor.fetchone()
  				return results
		finally:
  			self.conn.close()
