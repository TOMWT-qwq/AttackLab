import sys
from pathlib import Path

payload = (Path(__file__).resolve().parent / "attack" / "in1").read_bytes()
sys.stdout.buffer.write(payload)
