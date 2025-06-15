import streamlit as st
import json
import copy
import random
import pandas as pd

MASK = "*****"
def main():
    st.title("IPA Table(JP)")
    table=[["IPA","V","P","M"," "]]

    with open('data/ipa_description_ja.json', 'r', encoding='utf-8') as f:
        data: list[dict[str,str]] = json.load(f)
        for elem in data:
            vpm:list[str]=elem.get("IPA Description","").split(" ")
            char=elem["Character"]
            table.append([char]+vpm)
    
    if "show_table" not in st.session_state:
        st.session_state.show_table = True    
    if st.button("隠す"):
        st.session_state.show_table = False
    if st.button("すべて表示"):
        st.session_state.show_table = True

    if st.session_state.show_table:
        st.dataframe(pd.DataFrame(table[1:], columns=table[0]))
    else:
        hidden = partially_hide_table(table)
        df = pd.DataFrame(hidden[1:], columns=hidden[0])
        styled = df.style.map(lambda x:'background-color: gray' if x == MASK else '')
        st.dataframe(styled)
        
def partially_hide_table(table: list[list[str]]):
    table_copy = copy.deepcopy(table)
    HideenCellCount= 20
    for _ in range(HideenCellCount):
        row = random.randint(1, len(table_copy) - 1)
        col = random.randint(0, len(table_copy[0]) - 2) # 「音」を隠さない
        table_copy[row][col] = MASK
    return table_copy

if __name__ == "__main__":
    main()
