@echo off 

REM By: Zhean Ganituen
REM For windows only

REM initialize the virtual environment
python -m venv venv

call venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

@echo Virtual environment and dependencies installed.
@echo read README.md
