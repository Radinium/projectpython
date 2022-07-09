it is recomended that you install all the new gpu drivers
install python (dont forget the path)

you sould install packages below with pip 
tensorflow
tensorflow-gpu
opencv-python 
matplotlib
numpy

tensorflow is for machine learning deep learning
opencv is for computer vision
matplotlib is for ploting for visualizing images
numpy is for data manipulation

then we import all the dependencies into our code we did this step at the top of our code


note:fuctional api is really better when doing some complicated deep learning models

	our model for deep learning will be siamese neural networks 
	wich is really good at oneshot image recognition
	what is one shot image recognition? 
	its classificaiton model where we give computer a small number of examples for each class
	then in turn must make prediction about many unknown examples in the future
	so it parses through two images and find the similarities
	if the similarities exceed a certain amount then it does the function given
	https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf

next should import tensorflow dependencies
	model module from tensorflow.keras.models will work something like this
		we will give two inputs one vrification image and one input image and 
		we need one output does it have any similarities or it doesnt
		our model will look like something like this
			model(inputs=[inputimage,verificationimage],output=[1,0])

need to limit tensorflow for gpu usage to avoid geting out of memory errors dont forget this step its really important

now setuping path for storing the pictures 
