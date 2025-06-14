import streamlit as st
import json
import typing

def main():
    st.title("IPA Table(JP)")
    table=[["IPA","V","P","M"]]
    with open('data/ipa_description_ja.json', 'r', encoding='utf-8') as f:
        data: list[dict[str,str]] = json.load(f)
        for elem in data:
            vpm:list[str]=elem.get("IPA Description","").split(" ")
            char=elem["Character"]
            table.append([char]+vpm)
    
    st.dataframe(table)



if __name__ == "__main__":
    main()
