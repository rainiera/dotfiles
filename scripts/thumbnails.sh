# Get frame rate if video frame rate is non-variable
args=("$@")
ffmpeg -i ${args[1]}
ffmpeg -i ${args[1]} 2>&1 | sed -n "s/.*, \(.*\) fp.*/\1/p"

# 24 images every 1 second
ffmpeg -i ${args[1]} -vf fps=24/1 filename-%05d.jpg

