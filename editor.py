from moviepy.editor import VideoFileClip
from moviepy.video import fx
from pathlib import Path
from datetime import datetime
from conf import OUTPUT_DIR, BASE_DIR, SOURCE_DIR

"""
video=VideoFileClip(str(Path.joinpath(SOURCE_DIR,"shop.mp4" )))
dur=int(video.duration)
w, h=video.size
print("video duration %.2d:%.2d:%.2d" % (dur/3600,dur/60,dur%60))
print("Width = %d, Height = %d" % (w, h))
video.close()
"""

def get_storage_name(extention=None):
	"""
	Return a new full name that represents the
	file storage location in the drive. The file
	name extention is based on the flag
	"""
	assert extention is not None,"supply file extention"

	name="output_%s%s" % (datetime.now().strftime("%d_%m_%H%M%S"),extention)

	return str(Path.joinpath(OUTPUT_DIR,name))

def get_duration(clip):
	"""
	Finds the duration of a given video clip
	return the duration of the video clip
	"""
	#find if the clip exists
	location=Path(clip)
	if not location.exists():
		return "location does not exist"


def crop_center(clip,height):
    vid=VideoFileClip(clip)
    vidx,vidy=vid.size
    y1=vidy//2 -height//2
    x1=0
    y2=y1+height
    x2=vidx
    print("x1 ={},x2 = {}, y1 ={}, y2 = {}".format(x1,x2,y1,y2))
    print(vidx,vidy)
    
    new_vid=vid.crop(x1=x1,y1=y1,x2=x2,y2=y2)
    
    new_vid.write_videofile(get_storage_name(extention=".mp4"))
    #new_vid.write_gif(get_storage_name(extention=".gif"))
    new_vid.close()
    vid.close()

def save_frames(clip,frames=5):
	vid=VideoFileClip(clip)
	vid=vid.resize(newsize=(vid.size[1],vid.size[0]))
	for i in range(1, frames+1):
		vid.save_frame(get_storage_name(extention=".jpeg"),t=i)

	vid.close()
