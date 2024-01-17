from moviepy.editor import *
import graphics

class Video:
    def __init__(self) -> None:
        self.clip = VideoFileClip('assets/videos/intro_no_cut.mp4')
    def run(self):
        self.clip.preview()