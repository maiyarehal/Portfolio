import pandas as pd
import random


def load_dataset(filename, split):
	training_set=[]
	test_set=[]
	df = pd.read_csv(filename, header=None)
	array = df.to_numpy()
	random.shuffle(array)
	training_len = int(len(array)*split)
	training_set = array[:training_len]
	test_set = array[training_len:]
	return training_set, test_set
