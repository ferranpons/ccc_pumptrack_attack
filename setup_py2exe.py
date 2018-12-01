import os
import sys

include_files = [
    "data/background_menu.png",
    "data/background_title.png",
    "data/ccc_logo.png",
    "data/ccc_pumptrack_attack_title.png",
    "data/fps_logo.png",
    "data/intro_ball.gif",
    "data/leaderboard.txt",
    "data/menu_line.png",
    "data/pumptrack.png"
    "data/pygame_badge_SMA.png",
    "data/rider1_placeholder.png",
    "data/Windom_Earle_07_screw_wave.mp3"
]

from distutils.core import setup
import py2exe
import glob

# path = os.path.dirname(__file__).replace('\\library.zip', '')
# xml_file = open(os.path.join(path, 'gui.xml'))

setup(
    name="CCC Pumtrack Attack",
    windows=[
        {
            'script': 'game.py',
        }
    ],

    options={
        'py2exe': {
            "optimize": 2,
            'includes': 'pygame',
            "compressed": 1,
            "bundle_files": 1
        }
    },
    data_files=[
        ("data", ["data\\background_menu.png",
                  "data\\background_title.png",
                  "data\\ccc_logo.png",
                  "data\\ccc_pumptrack_attack_title.png",
                  "data\\fps_logo.png",
                  "data\\intro_ball.gif",
                  "data\\leaderboard.txt",
                  "data\\menu_line.png",
                  "data\\pumptrack.png",
                  "data\\pygame_badge_SMA.png",
                  "data\\rider1_placeholder.png",
                  "data\\Windom_Earle_07_screw_wave.mp3"
                  ])
    ],
    zipfile=None
)
