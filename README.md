# VLCWorkoutScheduler
Simple python script to generate 'playlist' for workout.
### Usage
```sh
$ createWorkoutScript.py -d "P90X3.txt" -n "script.py"
```
Where `P90X3.txt` is file where every line is path to workout and line number is the workout number. 
Run it once and it will get the date of first run, it will save next day as the starting day of exercises. Now only run generated script to play video.
### Requirements
It's based on VLC player <https://www.videolan.org/> and PATH must be set with it.