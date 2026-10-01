import json
import re

def populate_grammar():
    with open("grammar_dump.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    with open("data/grammar/lessons-01-25.json", "r", encoding="utf-8") as f:
        grammar_data = json.load(f)
        
    current_lesson = 0
    current_point = 0
    
    current_explanation = []
    
    def save_explanation():
        if current_lesson > 0 and current_point > 0 and current_explanation:
            # find the lesson and point in grammar_data
            for lesson in grammar_data:
                if lesson["lessonId"] == current_lesson:
                    for point in lesson["grammarPoints"]:
                        if point["pointNumber"] == current_point:
                            point["notes"] = "\n".join(current_explanation).strip()
                            break
                    break
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for Lesson X
        lesson_match = re.match(r'^Lesson\s+(\d+)$', line)
        if lesson_match:
            save_explanation()
            current_lesson = int(lesson_match.group(1))
            current_point = 0
            current_explanation = []
            continue
            
        # Check for Grammar Point e.g., "1. N₁は N₂です"
        point_match = re.match(r'^(\d+)\.\s+(.*)$', line)
        if point_match and current_lesson > 0:
            save_explanation()
            current_point = int(point_match.group(1))
            current_explanation = []
            continue
            
        # Accumulate explanation
        if current_lesson > 0 and current_point > 0:
            current_explanation.append(line)
            
    # Save the last one
    save_explanation()
    
    with open("data/grammar/lessons-01-25.json", "w", encoding="utf-8") as f:
        json.dump(grammar_data, f, indent=2, ensure_ascii=False)
        
    print("Grammar population complete!")

if __name__ == '__main__':
    populate_grammar()
