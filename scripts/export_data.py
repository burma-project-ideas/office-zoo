"""Build the language-independent Office Zoo dataset from the reference data."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def read(name):
    return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))


def build():
    constants = read('bundled-constants.json')
    animals = read('animals.json')
    order = read('animalOrder.json')
    questions = read('questions.json')
    scores = read('compatibilityScores.json')
    assert len(animals) == 8 and set(order) == set(animals)
    assert len(questions) == 24 and len({q['id'] for q in questions}) == 24
    assert all(len(q['options']) == 5 for q in questions)
    assert all(o['a'] in animals for q in questions for o in q['options'])
    assert len(scores) == 36
    assert all(f'{a}-{b}' in scores or f'{b}-{a}' in scores for a in order for b in order)
    assert all(isinstance(score, int) and 0 <= score <= 100 for score in scores.values())
    traits = read('traits.json')
    assert all(set(a['traits']) == {t['key'] for t in traits} for a in animals.values())
    relationships = constants['mi']
    assert set(relationships) == set(animals)
    assert all(set(row) <= set(animals) for row in relationships.values())
    return {
        'project': {'name': 'Office Zoo', 'author': 'Harry Hein',
                    'website': 'https://office-zoo.vercel.app/',
                    'purpose': 'Learning and inspiration for building workplace quiz and team comparison apps.',
                    'languages': ['en', 'my']},
        'animalOrder': order,
        'traits': traits,
        'animals': animals,
        'questions': [
            {'id': q['id'], 'prompt': {'en': q['en'], 'my': {'self': q['self'], 'other': q['other']}},
             'options': [{'animalId': o['a'], 'text': {'en': o['en'], 'my': o['text']}} for o in q['options']]}
            for q in questions
        ],
        'compatibilityScores': scores,
        'relationships': relationships,
        'animalGuidance': constants['xf'],
        'animalKeywords': constants['Zr'],
        'archetypeLabels': constants['Ir'],
        'traitDescriptions': constants['wa'],
        'uiText': constants['ka'],
        'explanationSteps': constants['ci'],
        'calculationText': constants['mf'],
        'compatibilityVerdicts': [
            {'minScore': 80, 'en': 'Near-perfect', 'my': 'အကောင်းဆုံးနီးပါး'},
            {'minScore': 65, 'en': 'Strong', 'my': 'ကောင်းမွန်'},
            {'minScore': 50, 'en': 'Workable', 'my': 'အဆင်ပြေနိုင်'},
            {'minScore': 40, 'en': 'Tense', 'my': 'တင်းမာ'},
            {'minScore': 0, 'en': 'High friction', 'my': 'ပွတ်တိုက်မှုမြင့်'}
        ]
    }


if __name__ == '__main__':
    dataset = build()
    output = ROOT / 'OfficeZoo.json'
    output.write_text(json.dumps(dataset, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    assert json.loads(output.read_text(encoding='utf-8')) == dataset
    print('Validated and exported 8 animals, 24 questions, and 36 compatibility scores.')
