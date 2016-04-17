from random import randint
import datetime
import os
import subprocess
# -*- coding: UTF-8 -*-

#max changes files is 712 files in folder
music_folder = "/media/serj/5F4C-7028/666/"
#music_folder = "/media/serj/8AB6EFEAB6EFD4AB/TestFolder/"


def date_of_generation():
    year = 2000
    month = randint(1,12)
    day = randint(1,28)
    hour = randint(10,23)
    minute = randint(10,59)

    generated_data= str(datetime.datetime(year, month, day, hour, minute))
    generated_data = generated_data.replace('-', '').replace(':', '').replace(' ', '')
    generated_data = generated_data[0:-2]
    return generated_data

def script_for_music(path):
    song_list = os.listdir(path)
    for song in song_list:
        song.decode('utf8')
        #subprocess.call(['mv', music_folder + song, music_folder + song[0:20] + '.mp3'])
        generated_data= date_of_generation()
        print(song)
        print(generated_data)
        subprocess.call(['touch', '-t' + generated_data, path + song])

script_for_music(music_folder)


