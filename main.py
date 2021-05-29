from punctuator import Punctuator
import moviepy.editor as mp
import torch
import torchaudio
import os
import nemo.collections.asr as nemo_asr
import contextlib


def to_audio(video_file):
    clip = mp.VideoFileClip(video_file) 
 
    clip.audio.write_audiofile('audio.wav')

def change_samplerate():
    y, sr = torchaudio.load('audio.wav')
    y = y.mean(dim=0) # if there are multiple channels, average them to single channel
    if sr != 16000:
        resampler = torchaudio.transforms.Resample(sr, 16000)
        y_resampled = resampler(y)
    torchaudio.set_audio_backend(backend='sox')   
    torchaudio.save(src=y_resampled,sample_rate=16000,filepath='sampled_audio.wav')
    
def to_text(audio_file):
    # Helper for torch amp autocast
    if torch.cuda.is_available():
        autocast = torch.cuda.amp.autocast
    else:
        @contextlib.contextmanager
        def autocast():
            print("AMP was not available, using FP32!")
            yield
            
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = nemo_asr.models.EncDecCTCModelBPE.from_pretrained("stt_en_citrinet_256", map_location=device)
    model = model.to(device)
    
    with autocast():
        text = model.transcribe([audio_file], batch_size=1)[0]
    return text

def punctuate_text(text):
    p = Punctuator('models/INTERSPEECH-T-BRNN.pcl')
    print(p.punctuate(text))
    
def my_func(video_file):
    print('Converting to audio')
    to_audio(video_file)
    change_samplerate()
    text=to_text('sampled_audio.wav')
    os.remove('audio.wav')
    os.remove('sampled_audio.wav')    
    print('Punctuating Text')
    punctuate_text(text)

file_path='videos/Demo.mp4'
my_func(file_path)
        
