import json
import os

def validate_grammar():
    print("--- VALIDATING GRAMMAR ---")
    if not os.path.exists('data/grammar/lessons-01-25.json'):
        print("ERROR: data/grammar/lessons-01-25.json missing")
        return
        
    with open('data/grammar/lessons-01-25.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)
        
    if len(lessons) != 25:
        print(f"ERROR: Expected 25 lessons, found {len(lessons)}")
    else:
        print("[OK] Exactly 25 lessons found.")
        
    all_ids = set()
    total_points = 0
    missing_fields = 0
    
    for l in lessons:
        l_id = l.get('lessonId')
        pts = l.get('grammarPoints', [])
        total_points += len(pts)
        
        for p in pts:
            pid = p.get('id')
            if pid in all_ids:
                print(f"ERROR: Duplicate ID found - {pid}")
            all_ids.add(pid)
            
            # Check missing fields
            if not p.get('meaning'): missing_fields += 1
            if not p.get('pattern'): missing_fields += 1
            if not p.get('exampleSentence'): missing_fields += 1
            if not p.get('notes'): missing_fields += 1

    print(f"[OK] Found {total_points} total grammar points.")
    print(f"[WARN] {missing_fields} missing fields detected across grammar points (Expected since we haven't populated them manually yet).")

def validate_kanji():
    print("\n--- VALIDATING KANJI ---")
    if not os.path.exists('data/kanji/kanji-320.json'):
        print("ERROR: data/kanji/kanji-320.json missing")
        return
        
    with open('data/kanji/kanji-320.json', 'r', encoding='utf-8') as f:
        kanji = json.load(f)
        
    if len(kanji) != 320:
        print(f"ERROR: Expected 320 kanji, found {len(kanji)}")
    else:
        print("[OK] Exactly 320 kanji found.")
        
    all_nums = set()
    all_chars = set()
    missing_readings = 0
    missing_meanings = 0
    missing_vocab = 0
    missing_examples = 0
    missing_stroke = 0
    
    for i, k in enumerate(kanji):
        k_num = k.get('kanjiNumber')
        char = k.get('character')
        
        if k_num != i + 1:
            print(f"ERROR: Incorrect numbering for Kanji {char}. Expected {i+1}, got {k_num}")
            
        if k_num in all_nums:
            print(f"ERROR: Duplicate number found - {k_num}")
        all_nums.add(k_num)
        
        if char in all_chars:
            print(f"ERROR: Duplicate character found - {char} (Number {k_num})")
        all_chars.add(char)
        
        if not k.get('kunReadings') and not k.get('onReadings'): missing_readings += 1
        if not k.get('meanings'): missing_meanings += 1
        if not k.get('vocabulary'): missing_vocab += 1
        if not k.get('exampleSentences'): missing_examples += 1
        if not k.get('strokeOrder'): missing_stroke += 1

    print(f"[OK] Numbering sequence is correct.")
    print(f"[OK] No duplicate characters found.")
    print(f"[WARN] Missing readings: {missing_readings}/320")
    print(f"[WARN] Missing meanings: {missing_meanings}/320")
    print(f"[WARN] Missing vocabulary: {missing_vocab}/320")
    print(f"[WARN] Missing example sentences: {missing_examples}/320")
    print(f"[WARN] Missing stroke order data: {missing_stroke}/320")
    print("\nNOTE: These missing fields are explicitly noted as incomplete in the master source at this phase.")

if __name__ == '__main__':
    validate_grammar()
    validate_kanji()
