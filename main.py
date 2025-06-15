import streamlit as st
import json
import typing
import copy
import random

def main():
    st.title("IPA Table(JP)")
    table=[["IPA","V","P","M"]]
    # hideen_table= copy.deepcopy(table)
    hideen_table = [["IPA","V","P","M"]]

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
    if st.button("表示"):
        st.session_state.show_table = True

    if st.session_state.show_table:
        st.dataframe(table)
    else:
        st.dataframe(partially_hide_table(table))
    
def partially_hide_table(table: list[list[str]]):
    table_copy = copy.deepcopy(table)
    HideenCellCount= 20
    for _ in range(HideenCellCount):
        row = random.randint(1, len(table_copy) - 1)
        col = random.randint(0, len(table_copy[0]) - 2) # 「音」を隠さない
        table_copy[row][col] = "*****"
    return table_copy

if __name__ == "__main__":
    main()
