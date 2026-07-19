#!/usr/bin/env python3
"""make_audio_remaining.py — generate audio only for segments missing mp3 files.
Ultra-short beats to conserve ElevenLabs credits.
"""
import json, os, re, sys, urllib.request, urllib.error
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENV_CANDIDATES = [
    Path.home() / "Documents/CoWork/bear-textbooks/books/unreal-reels/.env",
    Path.home() / "Documents/CoWork/bear-textbooks/books/vox/.env",
    HERE / ".env",
]

# Ultra-short replacements for S08-S12 to fit within remaining credits
SHORT_BEATS = {
    "S08": "Liquid biopsy samples ctDNA shed from all tumor sites. Genuine advantages: whole-tumor sampling, repeatability, and resistance detection.",
    "S09": "Three limits: low shedding, clonal hematopoiesis, no architecture.",
    "S10": "DYNAMIC: ctDNA guided adjuvant decisions. Non-inferior survival.",
    "S11": "Companion diagnostics clear all three bars. Enthusiasm is not evidence.",
    "S12": "Analytic valid. Clinical valid. Utility proven. That is the filter.",
}

def load_key():
    k = os.getenv("ELEVENLABS_API_KEY")
    if k: return k
    for env in ENV_CANDIDATES:
        if env.exists():
            for line in env.read_text().splitlines():
                m = re.match(r"\s*ELEVENLABS_API_KEY\s*=\s*(.+)", line)
                if m: return m.group(1).strip().strip("'\"")
    sys.exit("[err] no ELEVENLABS_API_KEY found")

SUB = {"—": ", ", "–": ", ", "…": "...", "%": " percent",
       "PI3K": "P-I-3-K", "Bcl-2": "B-C-L-2", "AKT": "A K T", "APC": "A P C",
       "KRAS": "K-RAS", "p53": "p 53", "TP53": "T-P-53", "BAX": "backs", "C-D-Ks": "C D Ks"}

def spoken(t):
    for a, b in SUB.items(): t = t.replace(a, b)
    return re.sub(r"\s+", " ", t).strip()

def gen(text, voice, key, out):
    payload = {"text": text, "model_id": "eleven_multilingual_v2", "output_format": "mp3_44100_128",
               "voice_settings": {"stability": 0.80, "similarity_boost": 0.75, "style": 0.0,
                                  "use_speaker_boost": True, "speed": 0.94}}
    req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{voice}",
        data=json.dumps(payload).encode(), method="POST",
        headers={"Accept": "audio/mpeg", "Content-Type": "application/json", "xi-api-key": key})
    with urllib.request.urlopen(req, timeout=180) as r:
        out.write_bytes(r.read())

def measure(path):
    import subprocess
    try:
        r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                            "-of", "default=nk=1:nw=1", str(path)], capture_output=True, text=True)
        return round(float(r.stdout.strip()), 2)
    except Exception:
        return None

def main():
    key = load_key()
    sheet = json.loads((HERE / "beat_sheet.json").read_text())
    voice = os.getenv("ELEVENLABS_VOICE_NIKBEARBROWN") or sheet["voice_id"]
    adir = HERE / "audio"; adir.mkdir(exist_ok=True)

    for s in sheet["segments"]:
        sid = s["id"]
        out = adir / f"{sid}.mp3"
        if out.exists():
            print(f"  [{sid}] already exists, skipping")
            continue
        # Use short beat if available, else original
        text = SHORT_BEATS.get(sid, s["beats"][0]["text"])
        txt = spoken(text)
        print(f"  [{sid}] generating ({len(txt)} chars)...")
        try:
            gen(txt, voice, key, out)
        except urllib.error.HTTPError as e:
            body = e.read().decode('utf-8', 'ignore')[:400]
            print(f"[err] {sid} HTTP {e.code}: {body}")
            break
        dur = measure(out)
        # Update beat_sheet with the short text and duration
        s["beats"][0]["text"] = text
        s["beats"][0]["audio_file"] = f"audio/{sid}.mp3"
        s["beats"][0]["actual_duration_s"] = dur
        print(f"  [{sid}] {out.name}  {dur}s  ({out.stat().st_size//1024} KB)")

    (HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False))
    print("[ok] remaining audio done — run build_deck.py && render.py")

if __name__ == "__main__":
    main()
