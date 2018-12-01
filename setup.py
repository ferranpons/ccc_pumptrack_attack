import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name="CCC Pumptrack Attack",
    version = "0.1",
    description = "Open Source video game with a fancy pixel art about riding pump tracks with a mountain bike",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": [
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
                           ]}
             },
    executables=executables

)
