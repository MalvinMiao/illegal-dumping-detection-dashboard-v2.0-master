from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
engine = create_engine('postgresql://localhost/cmpe295')

#SQL schema
class ImageCategories(Base):
	"""
	RDMS - table for image categories
	"""
	__tablename__ = 'imagecategory'
	category_id = Column(Integer, primary_key = True, autoincrement=True)
	category_name = Column(String(100), nullable = False)

	def __init__(self, category_name):
		self.category_name = category_name

class TrainingImageData(Base):
	"""
	RDMS - table for image data waiting for training or trained
	"""
	__tablename__ = 'imagedata'
	image_id = Column(Integer, primary_key = True)
	category_id = Column(Integer, ForeignKey("imagecategory.category_id"), nullable=True)
	path = Column(String(100), nullable = False)
	createDate = Column(DateTime, nullable = False)
	trainedDate = Column(DateTime, nullable = True, default = None)

	def __init__(self, category_id, path):
		self.category_id = category_id
		self.path = path
		self.createDate = datetime.utcnow()

class InputImageData(Base):
	"""
	RDMS - table for input image data
	"""
	__tablename__ = 'inputimagedata'
	inputimage_id = Column(Integer, primary_key = True)
	path = Column(String(100), nullable = False)
	createDate = Column(DateTime, nullable = False)

	def __init__(self, path):
		self.inputimage_id = inputimage_id
		self.path = path
		self.createDate = datetime.utcnow()

class ClassificationResult(Base):
	"""
	RDMS - table for classification result
	"""

	__tablename__ = 'classificationResult'
	classification_id =Column(Integer, primary_key = True)
	category_id = Column(Integer, ForeignKey("imagecategory.category_id"), nullable=True)
	classificationDate = Column(DateTime, nullable = False)

	def __init__(self, category_id, image_id, classificationDate):
		self.category_id = category_id
		self.image_id = image_id
		self.classificationDate = classificationDate

class UserData(Base):
	"""
	RDMS - table for user data
	"""

	__tablename__ = 'userdata'
	user_id = Column(Integer, primary_key = True)
	userName = Column(String(100), nullable = False)
	user_password = Column(String(50), nullable = False)
	workType = Column(String(50), nullable = False)
	createDate = Column(DateTime)

	def __init__(self, userName, user_password, workType):
		self.userName = userName
		self.user_password = user_password
		self.workType = workType
		self.createDate = datetime.utcnow()
