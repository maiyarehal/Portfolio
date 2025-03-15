import func
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier as kn


if __name__ == "__main__":

	#Array to hold mean accuracies
	mean_arr = []

	#Loop through 1 to 20
	for k in range(1,21):
		#Variable to hold total accuracy
		acc_total = 0.0
		#Loop through 1 to 5
		for i in range(1,6):
			#Load training set and test set
			training_set , test_set = func.load_dataset('iris.data', 0.66)

			#Create Kn object
			iris = kn(n_neighbors=k)

			#Grab every value but the last value of each row in the training set
			#Last value is the ground truth y value
			x_train = training_set[:, :-1].astype(float)

			#Grab the y values of the training set
			y_train = training_set[:, -1]

			#Grab every value but the last value of each row in the test set
			#Last value is the ground truth y value
			x_test = test_set[:, :-1].astype(float)

			#Grab the y values of the test set
			y_test = test_set[:, -1]
			
			#Train the Model
			iris.fit(x_train,y_train)

			#Calculate the accuracy of the model
			accuracy = iris.score(x_test, y_test) * 100

			acc_total += accuracy
		
		mean_accuracy = acc_total/5

		mean_arr.append(mean_accuracy) 


	for i,value in enumerate(mean_arr):
		print(f"K value of {i + 1} mean accuracy is {value}%")

		
	#Create the line plot
	plt.plot(range(1,21), mean_arr)

	plt.title("K 1 to 20 Mean Accuracies")
	plt.xlabel("K Values")
	plt.ylabel("Accuracies")
	plt.xticks(range(1,21))

	plt.grid(True)
	plt.savefig('kvalues.png')
