@echo off
cd /d "C:\Users\ASUS\Documents\Web apps\Wordpress\Harcèlement Croatie"

echo.
echo === Deploiement Harcelement ===
echo.

git add .

git diff --cached --quiet
if %errorlevel%==0 (
  echo Aucun changement a commiter.
) else (
  echo Fichiers inclus dans ce commit :
  git diff --cached --name-only
  echo.
  git commit -m "maj"
  if %errorlevel% neq 0 (
    echo.
    echo ERREUR lors du commit.
    pause
    exit /b 1
  )
)

git push origin main
if %errorlevel%==0 (
  echo.
  echo Done. https://amanalat.github.io/Harcelement/
) else (
  echo.
  echo ERREUR lors du push.
)

echo.
pause
