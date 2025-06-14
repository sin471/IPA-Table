import json
from typing import Union
enToJpDict = {
    "Voiced": "有声",
    "Voiceless": "無声",
    "bilabial": "両唇",
    "labiodental": "唇歯",
    "dental": "歯",
    "postalveolar": "後部歯茎",
    "alveolar": "歯茎",
    "retroflex": "そり舌",
    "palatal": "硬口蓋",
    "velar": "軟口蓋",
    "uvular": "口蓋垂",
    "pharyngeal": "咽頭",
    "glottal": "声門",
    "Glottal": "声門",
    "plosive": "破裂",
    "nasal": "鼻",
    "trill": "ふるえ",
    "tap": "たたき",
    "flap": "はじき",
    "lateral fricative": "側面摩擦",
    "fricative": "摩擦",
    "lateral approximant": "側面接近",
    "lateral approximate": "側面接近", #元データのスペルミス
    "approximant": "接近",
    "approximate": "接近",
}

def translate(text:str) -> str:
    for en, jp in enToJpDict.items():
        text = text.replace(en, jp)
    return text

# 例: IPA DescriptionのJSONファイルを読み込む
with open('data/ipaBook.json', 'r', encoding='utf-8') as f:
    data: list[dict[str,Union[str,int]]] = json.load(f)
    new_data=[]
    for i in range(len(data)):
        if data[i]["IPA Number"]>158:
            break
        text=data[i]["IPA Description"]  
        result=translate(text)  
        data[i]["IPA Description"]=result+"音"
        # print(text)
        new_data.append(data[i])
        print(data[i]["Character"],result)  
# 置換処理

# 新しいJSONファイルとして保存
with open('data/ipa_description_ja.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=2)
