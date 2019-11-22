import os
import sys
import math
import keras
import logging
import numpy as np
import datetime as dt
import tensorflow as tf
from numpy import newaxis
from core.util.timer import Timer
from keras.models import Sequential, load_model
from keras.layers import Dense, SimpleRNN, LSTM
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.optimizers import Adam
from keras import losses
from sklearn.metrics import mean_squared_error

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

class Model():
	"""A class for an building and inferencing an lstm model"""
	
	def __init__(self):
		self.model = Sequential()
		self.model.add(SimpleRNN(units=10, input_shape=(1, 1)))
		self.model.add(Dense(1))
		adam = Adam(lr=0.001)
		self.model.compile(loss=losses.mean_squared_error, optimizer=adam)

		self.model.summary()

	def build_model(self, model_configs):
		with Timer(logger, "Building Model"):
			for layer in model_configs['model']['layers']:
				units = layer['units'] if 'units' in layer else None
				dropout_rate = layer['rate'] if 'rate' in layer else None
				activation = layer['activation'] if 'activation' in layer else None
				return_seq = layer['return_seq'] if 'return_seq' in layer else None
				input_timesteps = layer['input_timesteps'] if 'input_timesteps' in layer else None
				input_dim = layer['input_dim'] if 'input_dim' in layer else None

				'''
				if layer['type'] == 'dense':
					self.model.add(Dense(units, activation=activation))
				if layer['type'] == 'simple':
					self.model.add(SimpleRNN(units, input_shape=(input_timesteps, input_dim)))
				if layer['type'] == 'lstm':
					self.model.add(LSTM(units, input_shape=(input_timesteps, input_dim), return_sequences=return_seq))
				if layer['type'] == 'dropout':
					self.model.add(Dropout(dropout_rate))
				'''
			
			'''
			self.model.add(SimpleRNN(units=10, input_shape=(1, 1)))
			self.model.add(Dense(1))
			self.model.compile(loss='mean_squared_error', optimizer='adam')
			'''

	def train(self, X_train, y_train, nb_epoch, batch_size):
		with Timer(logger, "[Model] Training Started:  %s epochs, %s batch size " % (nb_epoch, batch_size)):

			#save_fname = os.path.join(save_dir, '%s-e%s.h5' % (dt.datetime.now().strftime('%d%m%Y-%H%M%S'), str(epochs)))
			#self.model.fit(X, y, epochs=nb_epoch, batch_size=16)
		

			nb_epoch = 30
			self.model.fit(X_train, y_train, epochs=nb_epoch, batch_size=16)
			#self.model.save(save_fname)

	def train_generator(self, data_gen, epochs, batch_size, steps_per_epoch, save_dir):
		with Timer(logger, 
		'[Model] Training Started:  %s epochs, %s batch size, %s batches per epoch' % (epochs, batch_size, steps_per_epoch) ):

			save_fname = os.path.join(save_dir, '%s-e%s.h5' % (dt.datetime.now().strftime('%d%m%Y-%H%M%S'), str(epochs)))
			callbacks = [
				ModelCheckpoint(filepath=save_fname, monitor='loss', save_best_only=True)
			]
			self.model.fit_generator(
				data_gen,
				steps_per_epoch=steps_per_epoch,
				epochs=epochs,
				callbacks=callbacks,
				workers=1
			)

	def predict_point_by_point(self, data):
		#Predict each timestep given the last sequence of true data, in effect only predicting 1 step ahead each time
		print('[Model] Predicting Point-by-Point...')
		predicted = self.model.predict(data)
		predicted = np.reshape(predicted, (predicted.size,))
		return predicted

	def predict_sequences_multiple(self, data, window_size, prediction_len):
		#Predict sequence of 50 steps before shifting prediction run forward by 50 steps
		print('[Model] Predicting Sequences Multiple...')
		prediction_seqs = []
		for i in range(int(len(data)/prediction_len)):
			curr_frame = data[i*prediction_len]
			predicted = []
			for j in range(prediction_len):
				predicted.append(self.model.predict(curr_frame[newaxis,:,:])[0,0])
				curr_frame = curr_frame[1:]
				curr_frame = np.insert(curr_frame, [window_size-2], predicted[-1], axis=0)
			prediction_seqs.append(predicted)
		return prediction_seqs

	def predict_sequence_full(self, data, window_size):
		#Shift the window by 1 new prediction each time, re-run predictions on new window
		print('[Model] Predicting Sequences Full...')
		curr_frame = data[0]
		predicted = []
		for i in range(len(data)):
			predicted.append(self.model.predict(curr_frame[newaxis,:,:])[0,0])
			curr_frame = curr_frame[1:]
			curr_frame = np.insert(curr_frame, [window_size-2], predicted[-1], axis=0)
		return predicted
