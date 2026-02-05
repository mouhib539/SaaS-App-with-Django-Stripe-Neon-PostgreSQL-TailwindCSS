import requests
from pathlib import Path    

def download_to_local(url: str, out_path: Path, parent_mkdirs: bool = True) :
    if not isinstance(out_path, Path):
        raise ValueError(f"{out_path}out_path must be a pathlib.Path object")
    if parent_mkdirs:
        out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        with open(out_path, 'wb') as f:
            f.write(response.content)
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
