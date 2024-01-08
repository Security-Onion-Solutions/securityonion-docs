BUILDDIR=/tmp/securityonion-docs/autobuild
python -m venv .venv
source .venv/bin/activate
python -m pip install pip
pip install -r requirements.txt
pip install sphinx-autobuild
sphinx-autobuild --port 4444 -b html -d $BUILDDIR/doctrees -T -j auto -W . $BUILDDIR/html
