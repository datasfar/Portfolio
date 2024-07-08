source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
API_URL=https://portfolio-production-aa1d.up.railway.app/ reflex export --frontend-only
unzip frontend.zip -d public
rm frontend.zip 
deactivate