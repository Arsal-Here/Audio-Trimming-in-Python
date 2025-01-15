from pydub import AudioSegment
from pydub.playback import play
import simpleaudio

def func():
    song_input = str(input("Enter name of song to trim: "))
    song_name = song_input+".mp3"
    song = AudioSegment.from_mp3(song_name)
    
    
    time = input("Enter timestamp of starting point: ")
    minutes,seconds = [int(i) for i in time.split(':')]
    
    time2 = input("Enter timestamp of ending point: ")
    minutes_last,seconds_last = [int(i) for i in time2.split(':')]
    
    if minutes_last>0:
        end_time = (minutes_last* 60) * seconds_last *1000
    else:
        end_time = seconds_last *1000
    
    if minutes>0:
        start_time = (minutes* 60) * seconds *1000
    else:
        start_time = seconds *1000
    
    
    print("Start time: ",start_time)
    print("End time: ",end_time)
    sliced_song = song[start_time:end_time]
    
    
    ans = str(input("Song has Been Trimmed.\nDo you want to play the trimmed song right now? "))
    ans = ans.lower()
    
    
    if ans=='yes':
        play(sliced_song)
        save = str(input("Do you want to save the trimmed song? "))
        save = save.lower()
        if save=='yes':
            song_name = song_input + "_Sliced.mp3"
            sliced_song.export(song_name,format = "mp3")
            print("Song Saved.")
    else:
        save = str(input("Do you want to save the trimmed song? "))
        save = save.lower()
        if save=='yes':
            song_name = song_input + "_Sliced.mp3"
            sliced_song.export(song_name,format = "mp3")
            print("Song Saved.")

if __name__ == '__main__':
    func()