# MNIST classifier. OOP.

You have 3 different models to solve MNIST (handwritten digits database) classification
problem:
- Convolutional Neural Network (any architecture, any framework); input: tensor 28x28x1;
- Random Forest classifier; input: 1-d numpy array of length 784 (28x28 pixels);
- Model that provides random value (for simplicity) as a result of classification; input: 10x10 numpy array, the center crop of the image.

The goal is to build a DigitClassifier model that takes an algorithm as an input
parameter. Possible values for the algorithm are: cnn, rf, rand for the three models
described above.

There is NO need to implement a training function inside DigitClassifier and focus on
the quality of the model, just raise a Not implemented exception. We need to focus only
on the predict function that takes a 28x28x1 image as input and provides a single
integer value as output.

Ideally, the solution should contain:
- Interface for models like Convolutional Neural Network, Random Forest classifier,
Random model. Potentially other developers will develop new models, so we
need to have an interface for them. Let’s call it DigitClassificationInterface. 
- 3 classes (1 for each model) that implement DigitClassificationInterface. 
- DigitClassifier, which takes as an input parameter the name of the algorithm
and provides predictions with exactly the same structure (inputs and outputs) not
depending on the selected algorithm.

### Files:

main.py - the solution