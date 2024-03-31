from cmu_graphics import *

# Requires os, pathlib
import os, pathlib



def loadSound(relativePath):
    # Convert to absolute path (because pathlib.Path only takes absolute paths)
    absolutePath = os.path.abspath(relativePath)
    # Get local file URL
    url = pathlib.Path(absolutePath).as_uri()
    # Load Sound file from local URL
    return Sound(url)


def onAppStart(app):
    
    # The Sound() constructor takes in a local URL to a sound file.
    # Why? I do not know. Probably an artifact of Online CS Academy.
    # So, for example: Sound("file:///C:/Users/shawn/Desktop/soundDemo/bulletSound.mp3")
    # You can technically get this by dragging a soundfile into a web browser, then copying the address field...
    # but that's ridiculous, and creates an absolute file path -- rendering it unusable on other computers.
    # As such, I've written a function that takes a relative filepath,
    # does the heavy work, and outputs a loaded Sound().
    
    app.sound1 = loadSound("sounds/bulletSound.mp3")
    app.sound2 = loadSound("sounds/roundStart.mp3")
    app.music = loadSound("sounds/themeSong.mp3")
    app.playing = False
    
def redrawAll(app):
    drawLabel("Sound Demo", app.width/2, app.height/2 - 40, size = 30)
    drawLabel("Press space to play sound!", app.width/2, app.height/2)
    drawLabel("Press s to play jingle!", app.width/2, app.height/2 + 20)
    drawLabel(f"Press m to {'play' if not app.playing else 'pause'} music!", app.width/2, app.height/2 + 40)
    
def onKeyPress(app, key):
    if key == "space":
        # Allows you to "spam" sounds -- i.e., doesn't wait for sound to end
        # for it to play the sound again
        app.sound1.play(restart = True)
    if key == "s":
        # Without it, you cannot spam sounds.
        # We must wait until sound ends to replay it.
        app.sound2.play()
    if key == "m":
        if not app.playing:
            # This is for looping sounds!
            app.music.play(loop = True)
            app.playing = True
        else:
            # And for pausing the looped sounds 
            # (this is kinda iffy sometimes idk why)
            app.music.pause()
            app.playing = False

def main():
    runApp()
    
main()