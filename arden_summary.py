import os
from dotenv import load_dotenv
from a3em_analysis.datasets import Arden

load_dotenv()

# load data-path and api token
path = os.getenv('DATA_PATH')
token = os.getenv('API_TOKEN')

# load Arden dataset
dataset = Arden(path, token)
features, _ = dataset.load_data(rumble_only=True)

# export features csv
rumble_identifiers = dataset.metadata.drop(columns=[
    'End Time (s)', 
    'call_type',
    'overlap',
    'earflap'
])
rumble_features = rumble_identifiers.join(features)
rumble_features.to_csv('arden_features.csv')

# export summary csv
summary = features.describe()
summary.to_csv('arden_summary.csv')
