pyinstaller --clean --onefile --noconfirm --noupx main.py
move "dist\main.exe" "main.exe"

rd /s /q "dist"
rd /s /q "build"
del main.spec