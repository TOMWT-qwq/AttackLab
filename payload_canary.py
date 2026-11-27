import sys
from pathlib import Path

payload = (Path(__file__).resolve().parent / "attack" / "in4").read_bytes()
sys.stdout.buffer.write(payload)
