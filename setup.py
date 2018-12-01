from cx_Freeze import setup, Executable

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
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"], 'include_files': include_files}

cx_Freeze.setup(
    name="CCC Pumptrack Attack",
    version="0.1",
    description="Open Source video game with a fancy pixel art about riding pump tracks with a mountain bike",
    author='Ferran Pons',
    options={"build_exe": build_exe_options},
    executables=[Executable(script="game.py", base="Win32GUI", targetName="YASS.exe")]
)
