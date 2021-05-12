from moviepy.editor import VideoFileClip
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




def save_frames(clip,frames=5):
	vid=VideoFileClip(clip)
	vid=vid.resize(newsize=(vid.size[1],vid.size[0]))
	for i in range(1, frames+1):
		vid.save_frame(get_storage_name(extention=".jpeg"),t=i)

	vid.close()
