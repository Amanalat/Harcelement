@echo off
cd /d "C:\Users\ASUS\Documents\Web apps\Wordpress\Harcèlement Croatie"

echo.
echo === Deploiement Harcelement ===
echo.

git add .
git commit -m "maj"
git push origin main

echo.
echo Done. https://amanalat.github.io/Harcelement/
echo.
pause
