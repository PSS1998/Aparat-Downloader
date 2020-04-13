# Aparat Downloader
ب
Use "" around link to avoid bad things <br>
```python adp.py "{Link}" --quality [quality] --type [type] ```<br>
    ```python apd.py "https://www.aparat.com/v/9h1Gb"```<br>
    ```python apd.py "https://www.aparat.com/v/9h1Gb" -q 480 -t playlist```<br>
The default quality is 480.<br>
The default type is playlist.<br>
For downloading playlists give link of one of the videos in playlists.<br>
Use this options for type:<br>
1-playlist for downloading playlists.<br>
2-single for downloading single videos.<br>
3-all for downloading all videos in a channel.<br>


## requirements
first use pip install -r requirements.txt to install requirements.<br>
then install aria2c using sudo apt-get install -y aria2.<br>
