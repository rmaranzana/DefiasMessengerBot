from defiasmessengerbot.core import *
from defiasmessengerbot.config import input_n_complete, get_data_path
from pathlib import Path


if __name__=='__main__':
   # Config:
   data_file = Path(get_data_path())

   if not data_file.is_file():
      input_n_complete()

   # Run:
   run_defiasmessengerbot()