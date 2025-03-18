
import os

ROOT_PATH = '/content/drive/MyDrive/Colab Notebooks/Stock_Market_Prediction'

RAW_DATA_PATH = os.path.join(ROOT_PATH, 'data/raw')

PROCESSED_DATA_PATH = os.path.join(ROOT_PATH, 'data/processed')

CHECKPOINTS_PATH = os.path.join(ROOT_PATH, 'checkpoints')

RESULTS_PATH = os.path.join(ROOT_PATH, 'results')

FIGURES_PATH = os.path.join(RESULTS_PATH, 'figures')

METRICS_PATH = os.path.join(RESULTS_PATH, 'metrics')

TRAIN_PATH = os.path.join(PROCESSED_DATA_PATH, 'train')
VAL_PATH = os.path.join(PROCESSED_DATA_PATH, 'val')
TEST_PATH = os.path.join(PROCESSED_DATA_PATH, 'test')
