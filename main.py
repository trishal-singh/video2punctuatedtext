from punctuator import Punctuator
import speech_recognition as sr
import moviepy.editor as mp

def to_audio(video_file):
    clip = mp.VideoFileClip(video_file) 
 
    clip.audio.write_audiofile('audio.wav')

def to_text():
    
    r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable

    with sr.AudioFile('audio.wav') as source:
    
        audio_text = r.listen(source)
    
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
        
        # using google speech recognition
            print('Converting audio transcripts into text ...')
            text = r.recognize_google(audio_text)
            
            print("Done")
            return text
     
        except:
             print('Sorry.. run again...')

def punctuate_text(text):
    p = Punctuator('models/INTERSPEECH-T-BRNN.pcl')
    print(p.punctuate(text))
    
def my_func(video_file):
    print('Converting to audio.wav')
    to_audio(video_file)
    print('Done')
    
    text=to_text()
    
    print('Punctuating Text')
    punctuate_text(text)

file_path='videos/Demo.mp4'
my_func(file_path)
        
