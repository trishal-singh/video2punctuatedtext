from punctuator import Punctuator
import moviepy.editor as mp
import torch
import zipfile
import torchaudio
from glob import glob

def to_audio(video_file):
    clip = mp.VideoFileClip(video_file) 
 
    clip.audio.write_audiofile('audio.wav')

def to_text():
    device = torch.device('cpu')  # gpu also works, but our models are fast enough for CPU
    model, decoder, utils = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                       model='silero_stt',
                                       language='en', # also available 'de', 'es'
                                       device=device)
    (read_batch, split_into_batches,
    read_audio, prepare_model_input) = utils  # see function signature for details

# download a single file, any format compatible with TorchAudio
#torch.hub.download_url_to_file('https://opus-codec.org/static/examples/samples/speech_orig.wav',
                               #dst ='speech_orig.wav', progress=True)
    test_files = glob('audio.wav') 
    batches = split_into_batches(test_files, batch_size=10)
    input = prepare_model_input(read_batch(batches[0]),
                            device=device)

    output = model(input)
    text=""
    for example in output:
        text+=decoder(example.cpu())
    return text

def punctuate_text(text):
    p = Punctuator('models/INTERSPEECH-T-BRNN.pcl')
    print(p.punctuate(text))
    
def my_func(video_file):
    print('Converting to audio.wav')
    to_audio(video_file)
    print('Done')
    print('Converting audio to text')
    text=to_text()
    
    print('Punctuating Text')
    punctuate_text(text)

file_path='videos/Demo.mp4'
my_func(file_path)
        
