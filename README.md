# TextGen
LSTM Recurrent Neural Network for Text Generation

## Getting Started

- Install dependencies: `pip install -r requirements.txt`

- Train the model: `python3 train.py input/matrix.txt`

- Generate text: `python3 generate.py input/matrix.txt checkpoints/weights-improvement-20-1.5858-bigger.hdf5`

## Possible Improvements to the Model
- Predict fewer than 1,000 characters as output for a given seed.
- Remove all punctuation from the source text, and therefore from the models’ vocabulary.
- Try a one hot encoded for the input sequences.
- Train the model on padded sentences rather than random sequences of characters.
- Increase the number of training epochs to 100 or many hundreds.
- Add dropout to the visible input layer and consider tuning the dropout percentage.
- Tune the batch size, try a batch size of 1 as a (very slow) baseline and larger sizes from there.
- Add more memory units to the layers and/or more layers.
- Experiment with scale factors (temperature) when interpreting the prediction probabilities.
- Change the LSTM layers to be “stateful” to maintain state across batches.
