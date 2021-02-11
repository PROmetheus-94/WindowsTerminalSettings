import os
from pathlib import Path
from shutil import copy

source = Path.cwd().joinpath("res")
destination = Path(f"{os.environ['USERPROFILE']}/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState")

for item in os.listdir(source):
    copy(source.joinpath(item), destination)

os.system('wt')