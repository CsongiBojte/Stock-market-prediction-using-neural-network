
import os

ROOT_PATH = '/content/drive/MyDrive/Colab Notebooks/Stock_Market_Prediction'
BASE_PATH = os.path.join(ROOT_PATH, 'models/lstm')
RAW_DATA_PATH = os.path.join(BASE_PATH, 'data/raw')
PROCESSED_DATA_PATH = os.path.join(BASE_PATH, 'data/processed')
CHECKPOINTS_PATH = os.path.join(BASE_PATH, 'models/checkpoints')
RESULTS_PATH = os.path.join(BASE_PATH, 'results')
FIGURES_PATH = os.path.join(RESULTS_PATH, 'figures')
METRICS_PATH = os.path.join(RESULTS_PATH, 'metrics')
NOTEBOOKS_PATH = os.path.join(BASE_PATH, 'notebooks')

WINDOW_SIZE = 14
BATCH_SIZE = 15
EPOCHS = 32
LSTM_UNITS = 64
DROPOUT_RATE = 0.2
