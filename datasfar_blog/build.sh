source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
API_URL=https://personal-portfolio-2024.up.railway.app reflex export --frontend-only
unzip frontend.zip -d public
rm frontend.zip 
deactivate