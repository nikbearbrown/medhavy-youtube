#!/usr/bin/env python3
"""make_audio_retry.py — like make_audio.py but skips already-generated mp3s
and adds a short inter-request pause to avoid rate limits.
"""
import json, os, re, sys, time, urllib.request, urllib.error
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENV_CANDIDATES = [
    Path.home() / "Documents/CoWork/bear-textbooks/books/unreal-reels/.env",
    HERE / ".env",
]

def load_key():
    k = os.getenv("ELEVENLABS_API_KEY")
    if k: return k
    for env in ENV_CANDIDATES:
        if env.exists():
            for line in env.read_text().splitlines():
                m = re.match(r"\s*ELEVENLABS_API_KEY\s*=\s*(.+)", line)
                if m: return m.group(1).strip().strip("'\"")
    sys.exit("[err] no ELEVENLABS_API_KEY")

SUB = {"—": ", ", "–": ", ", "…": "...", "%": " percent",
       "PI3K": "P-I-3-K", "Bcl-2": "B-C-L-2", "AKT": "A K T", "APC": "A P C",
       "KRAS": "K-RAS", "p53": "p 53", "TP53": "T-P-53", "BAX": "backs", "C-D-Ks": "C D Ks"}

def spoken(t):
    for a, b in SUB.items(): t = t.replace(a, b)
    return re.sub(r"\s+", " ", t).strip()

def gen(text, voice, key, out, retries=4):
    payload = {"text": text, "model_id": "eleven_multilingual_v2", "output_format": "mp3_44100_128",
               "voice_settings": {"stability": 0.80, "similarity_boost": 0.75, "style": 0.0,
                                  "use_speaker_boost": True, "speed": 0.94}}
    for attempt in range(retries):
        try:
            req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{voice}",
                data=json.dumps(payload).encode(), method="POST",
                headers={"Accept": "audio/mpeg", "Content-Type": "application/json", "xi-api-key": key})
            with urllib.request.urlopen(req, timeout=180) as r:
                out.write_bytes(r.read())
            return
        except urllib.error.HTTPError as e:
            body = e.read().decode('utf-8', 'ignore')[:200]
            if e.code == 429 and attempt < retries - 1:
                wait = 8 * (attempt + 1)
                print(f"    [429 rate limit] waiting {wait}s before retry {attempt+2}/{retries}...")
                time.sleep(wait)
            else:
                sys.exit(f"[err] {out.name} HTTP {e.code}: {body}")

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
    total = 0.0
    changed = False
    for s in sheet["segments"]:
        out = adir / f"{s['id']}.mp3"
        if out.exists() and out.stat().st_size > 10000:
            dur = measure(out)
            s["beats"][0]["audio_file"] = f"audio/{s['id']}.mp3"
            s["beats"][0]["actual_duration_s"] = dur
            if dur: total += dur
            print(f"  [{s['id']}] SKIP (exists)  {dur}s  ({out.stat().st_size//1024} KB)")
            continue
        txt = spoken(s["beats"][0]["text"])
        gen(txt, voice, key, out)
        dur = measure(out)
        s["beats"][0]["audio_file"] = f"audio/{s['id']}.mp3"
        s["beats"][0]["actual_duration_s"] = dur
        if dur: total += dur
        changed = True
        print(f"  [{s['id']}] {out.name}  {dur if dur else '?'}s  ({out.stat().st_size//1024} KB)")
        time.sleep(2)   # small inter-request pause
    (HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False))
    print(f"\n[ok] {len(sheet['segments'])} mp3s · {total:.0f}s · durations written back to beat_sheet.json")
    print("[next] run:  python3 brutalist-art/runtime/scripts/build_deck.py <folder> && python3 brutalist-art/runtime/scripts/render.py <folder>")

if __name__ == "__main__":
    main()
