import json
import re

def parse_readings(text):
    kun = []
    on = []
    meanings = []
    
    # Extract Kun
    kun_match = re.search(r'Kun:\s*([^OnM]+)', text)
    if kun_match:
        kun_raw = kun_match.group(1).strip()
        kun = [k.strip() for k in kun_raw.split('、') if k.strip()]
        
    # Extract On
    on_match = re.search(r'On:\s*([^M]+)', text)
    if on_match:
        on_raw = on_match.group(1).strip()
        on = [o.strip() for o in on_raw.split('、') if o.strip()]
        
    # Extract Meaning
    meaning_match = re.search(r'Meaning of the kanji:\s*(.+)', text)
    if meaning_match:
        meanings = [m.strip() for m in meaning_match.group(1).split(';') if m.strip()]
        
    return kun, on, meanings

def populate_kanji():
    with open("table_nested_inspect.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    with open("data/kanji/kanji-320.json", "r", encoding="utf-8") as f:
        kanji_data = json.load(f)
        
    current_kanji_idx = -1
    
    for line in lines:
        line = line.strip()
        if line.startswith("Col 1 text:"):
            # Example: Col 1 text: 1   人     Kun: ひと     On: ジン、ニン
            text = line.replace("Col 1 text:", "").strip()
            # Match number and character
            match = re.match(r'^(\d+)\s+(\S+)', text)
            if match:
                k_num = int(match.group(1))
                char = match.group(2)
                
                # Find matching kanji in json
                for i, k in enumerate(kanji_data):
                    if k["kanjiNumber"] == k_num:
                        current_kanji_idx = i
                        break
                
                kun, on, meanings = parse_readings(text)
                kanji_data[current_kanji_idx]["character"] = char
                kanji_data[current_kanji_idx]["kunReadings"] = kun
                kanji_data[current_kanji_idx]["onReadings"] = on
                kanji_data[current_kanji_idx]["meanings"] = meanings
                kanji_data[current_kanji_idx]["vocabulary"] = []
                kanji_data[current_kanji_idx]["exampleSentences"] = []
                
        elif line.startswith("Col 1 Inner Table -> Row"):
            # Example: Col 1 Inner Table -> Row 0: | 人 | ひと | person | ここは人が多いですね。 |
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 5 and current_kanji_idx != -1:
                word = parts[1]
                reading = parts[2]
                meaning = parts[3]
                example = parts[4]
                
                # Sometime word is empty but reading is not, or meaning is.
                if word or reading or meaning or example:
                    vocab = {
                        "word": word,
                        "reading": reading,
                        "meaning": meaning,
                        "example": example
                    }
                    kanji_data[current_kanji_idx]["vocabulary"].append(vocab)
                    if example and example not in kanji_data[current_kanji_idx]["exampleSentences"]:
                        kanji_data[current_kanji_idx]["exampleSentences"].append(example)

    with open("data/kanji/kanji-320.json", "w", encoding="utf-8") as f:
        json.dump(kanji_data, f, indent=2, ensure_ascii=False)
        
    print("Kanji population complete!")

if __name__ == '__main__':
    populate_kanji()
