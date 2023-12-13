import json
import _pcr_data as p

with open('chara_name.json', 'w', encoding='utf-8') as f:
    json.dump(p.CHARA_NAME, f, ensure_ascii=False, indent=2)

with open('unavailable_chara.json', 'w', encoding='utf-8') as f:
    json.dump(list(p.UnavailableChara), f, ensure_ascii=False, indent=2)

with open('chara_profile.json', 'w', encoding='utf-8') as f:
    json.dump(p.CHARA_PROFILE, f, ensure_ascii=False, indent=2)
