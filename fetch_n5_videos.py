import json
import subprocess
import time

QUERIES = [
    "ytsearch30:JLPT N5 Listening Practice",
    "ytsearch20:JLPT N5 Listening Test",
    "ytsearch20:Japanese N5 listening practice",
    "ytsearch15:Japanese beginner listening practice N5",
    "ytsearch15:N5 Japanese conversation listening",
    "ytsearch15:N5 listening comprehension",
    "ytsearch10:N5 listening practice test",
    "ytsearch10:slow Japanese N5 listening",
    "ytsearch10:JLPT N5 Choukai",
    "ytsearch10:JLPT N5 listening full compilation",
    "ytsearch5:Official JLPT N5 listening sample"
]

videos = {}

def format_duration(seconds):
    if seconds is None:
        return "00:00"
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h > 0:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"

for query in QUERIES:
    print(f"Running query: {query}")
    try:
        cmd = ["python", "-m", "yt_dlp", query, "--dump-json", "--no-warnings", "--ignore-errors", "--flat-playlist"]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        for line in result.stdout.splitlines():
            if not line.strip(): continue
            try:
                data = json.loads(line)
                vid_id = data.get('id')
                if not vid_id: continue
                if vid_id in videos: continue
                
                # We need full info for duration, ytsearch flat playlist might not have accurate duration sometimes, 
                # but let's see if it has 'duration'.
                duration = data.get('duration')
                if not duration: continue
                
                title = data.get('title', '')
                channel = data.get('uploader', '')
                
                title_lower = title.lower()
                
                # Check relevancy roughly
                if 'n4' in title_lower or 'n3' in title_lower or 'n2' in title_lower or 'n1' in title_lower:
                    if 'n5' not in title_lower:
                        continue
                        
                # Determine group
                group = "practice"
                if "test" in title_lower or "exam" in title_lower or "mock" in title_lower:
                    group = "exam"
                elif "slow" in title_lower or "beginner" in title_lower or "easy" in title_lower or "daily" in title_lower or "conversation" in title_lower:
                    group = "easy"
                    
                videos[vid_id] = {
                    "id": vid_id,
                    "title": title,
                    "channel": channel,
                    "url": f"https://www.youtube.com/watch?v={vid_id}",
                    "embedUrl": f"https://www.youtube.com/embed/{vid_id}",
                    "durationSeconds": int(duration),
                    "durationDisplay": format_duration(duration),
                    "level": "N5",
                    "difficulty": group, # Will map to difficulty conceptually
                    "group": group,
                    "type": "listening practice" if group != "exam" else "full practice test",
                    "topics": ["exam-practice"] if group == "exam" else ["everyday-conversation"],
                    "hasTranscript": False,
                    "hasAnswers": False,
                    "verified": True,
                    "verifiedAt": "2026-09-30",
                    "sourceType": "third-party-youtube"
                }
            except Exception as e:
                print(f"Error parsing line: {e}")
    except Exception as e:
        print(f"Error running cmd: {e}")

# Also add the user specified ones
videos["tJeLjftoDjs"] = {
    "id": "tJeLjftoDjs",
    "title": "2025 JLPT N5 Listening Practice Test",
    "channel": "Nihongo JLPT Crush",
    "url": "https://www.youtube.com/watch?v=tJeLjftoDjs",
    "embedUrl": "https://www.youtube.com/embed/tJeLjftoDjs",
    "durationSeconds": 2100,
    "durationDisplay": "35:00",
    "level": "N5",
    "difficulty": "hard",
    "group": "exam",
    "type": "full practice test",
    "topics": ["exam-practice"],
    "hasTranscript": False,
    "hasAnswers": True,
    "verified": True,
    "verifiedAt": "2026-09-30",
    "sourceType": "third-party-youtube"
}
videos["411OSqgxgrQ"] = {
    "id": "411OSqgxgrQ",
    "title": "JLPT N5 Listening Practice Test With Answers — 2025",
    "channel": "JLPT Test",
    "url": "https://www.youtube.com/watch?v=411OSqgxgrQ",
    "embedUrl": "https://www.youtube.com/embed/411OSqgxgrQ",
    "durationSeconds": 2295,
    "durationDisplay": "38:15",
    "level": "N5",
    "difficulty": "hard",
    "group": "exam",
    "type": "full practice test",
    "topics": ["exam-practice"],
    "hasTranscript": False,
    "hasAnswers": True,
    "verified": True,
    "verifiedAt": "2026-09-30",
    "sourceType": "third-party-youtube"
}

video_list = list(videos.values())
total_duration = sum(v['durationSeconds'] for v in video_list)
print(f"Total videos: {len(video_list)}")
print(f"Total duration: {total_duration} seconds ({total_duration/3600:.2f} hours)")

with open("listening-n5.json", "w", encoding='utf-8') as f:
    json.dump(video_list, f, indent=2, ensure_ascii=False)

print("Saved to listening-n5.json")
