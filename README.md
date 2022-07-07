# A TensorFlow Implementation of DC-TTS: text-to-speech model

It is the implementation of text-to-speech model, dc-tts, introduced in [Efficiently Trainable Text-to-Speech System Based on Deep Convolutional Networks with Guided Attention](https://arxiv.org/abs/1710.08969). 

## Requirements

Installing the requirements.
```
## For GPU machine
pip install -r requirements.txt

## For CPU machine
pip install -r requirements_cpu.txt
```

## Data

<img src="https://image.shutterstock.com/z/stock-vector-lj-letters-four-colors-in-abstract-background-logo-design-identity-in-circle-alphabet-letter-418687846.jpg" height="200" align="right">

The English TTS is trained on public speech dataset, [LJ Speech Dataset](https://keithito.com/LJ-Speech-Dataset/). LJ Speech Dataset is recently widely used as a benchmark dataset in the TTS task because it is publicly available, and it has 24 hours of reasonable quality samples.


## Training

  * STEP 0. Download [LJ Speech Dataset](https://keithito.com/LJ-Speech-Dataset/) or prepare your own data and place it inside the `dataset` folder.
  * STEP 1. Adjust hyper parameters in `hyperparams.py`. Run `python prepo.py` to create `mels` and `mags` folders. Make sure to delete these folders if they already exist from prior data before running `prepo.py`.
  * STEP 2. Run `python train.py 1` for training Text2Mel. 
  * STEP 3. Run `python train.py 2` for training SSRN.

You can do STEP 2 and 3 at the same time, if you have more than one gpu card.

The training has been done and the pretrained models are available on Zimmer (~/projects/accented-synthetic-speech-generation/dc_tts/saved_models)

For speech synthesis, place the latest checkpoint from `logdir` folder to `models` folder under respective `LJ01-1` and `LJ01-2` folders.

## Fine-tuning 

  * STEP 0. Prepare the data of the accented speaker in the same format as LJ Speech dataset. The audio of the speaker ideally should be ~1.5-2 hours long. Place the data inside the `dataset` folder.
  * STEP 1. Adjust hyper parameters in `hyperparams.py`. Run `python prepo.py` to create `mels` and `mags` folders. Make sure to delete these folders if they already exist from prior data before running `prepo.py`.
  * STEP 2. Copy the saved `LJ01-1` folder from pretrained model path and to `LJ01-1` in `logdir` folder.  
  * STEP 3. Run `python train.py 1` for training Text2Mel for ~670k iterations. 
  * STEP 4. Run `python train.py 2` for training SSRN for ~49k iterations.
  
For speech synthesis, place the latest checkpoint from `logdir` folder to `models` folder under respective `LJ01-1` and `LJ01-2` folders.

## Training Curves

<img src="fig/training_curves.png">

## Attention Plot
<img src="fig/attention.gif">


## Generated Samples

| Dataset       | Samples |
| :----- |:-------------|
| LJ      | [50k](https://soundcloud.com/kyubyong-park/sets/dc_tts) [200k](https://soundcloud.com/kyubyong-park/sets/dc_tts_lj_200k) [310k](https://soundcloud.com/kyubyong-park/sets/dc_tts_lj_310k) [800k](https://soundcloud.com/kyubyong-park/sets/dc_tts_lj_800k)|
 

## Notes

  * The paper didn't mention normalization, but without normalization I couldn't get it to work. So I added layer normalization.
  * The paper fixed the learning rate to 0.001, but it didn't work for me. So I decayed it.
  * I tried to train Text2Mel and SSRN simultaneously, but it didn't work. I guess separating those two networks mitigates the burden of training.
  * The authors claimed that the model can be trained within a day, but unfortunately the luck was not mine. However obviously this is much fater than Tacotron as it uses only convolution layers.
  * Thanks to the guided attention, the attention plot looks monotonic almost from the beginning. I guess this seems to hold the aligment tight so it won't lose track.
  * The paper didn't mention dropouts. I applied them as I believe it helps for regularization.
  * Check also other TTS models such as [Tacotron](https://github.com/kyubyong/tacotron) and [Deep Voice 3](https://github.com/kyubyong/deepvoice3).
  
