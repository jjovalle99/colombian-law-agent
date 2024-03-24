import shlex
import subprocess
from pathlib import Path

import modal

image = modal.Image.debian_slim(python_version="3.11").pip_install(
    "streamlit==1.32.2", "langserve[all]==0.0.51", "python-dotenv"
)

stub = modal.Stub(
    name="ui-colombia-law-agent", image=image, secrets=[modal.Secret.from_name(label="legal-colombia-agent-ui")]
)

mounts_map = {
    "streamlit": {"local_path": Path(__file__).parent / "app.py", "remote_path": "/root/app.py"},
    "assets": {"local_path": Path(__file__).parent.parent / "assets/flow.png", "remote_path": "/root/assets/flow.png"},
}

streamlit_script_mount = modal.Mount.from_local_file(**mounts_map["streamlit"])
assets_mount = modal.Mount.from_local_file(**mounts_map["assets"])


@stub.function(
    allow_concurrent_inputs=100,
    mounts=[streamlit_script_mount, assets_mount],
    keep_warm=1,
)
@modal.web_server(8000)
def run():
    target = shlex.quote(str(mounts_map["streamlit"]["remote_path"]))
    cmd = f"streamlit run {target} --server.port 8000 --server.enableCORS=false --server.enableXsrfProtection=false"
    subprocess.Popen(cmd, shell=True)
