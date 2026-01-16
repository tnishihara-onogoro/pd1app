# -*- coding: utf-8 -*-
import streamlit as st
from questions import QUESTIONS

# ページ設定
st.set_page_config(page_title="Salesforce PD1 Master", page_icon="☁️", layout="centered")

# カスタムCSS
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stButton>button { width: 100%; border-radius: 10px; font-weight: bold; }
    .q-card { background: white; padding: 2rem; border-radius: 15px; border: 1px solid #e2e8f0; margin-bottom: 1rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
    .exp-box { background-color: #f1f5f9; padding: 1.5rem; border-left: 5px solid #3b82f6; border-radius: 5px; margin-top: 1rem; }
    </style>
""", unsafe_allow_html=True)

# セッション状態の初期化
if 'idx' not in st.session_state: st.session_state.idx = 0
if 'screen' not in st.session_state: st.session_state.screen = 'home'
if 'revealed' not in st.session_state: st.session_state.revealed = False
if 'results' not in st.session_state: st.session_state.results = {}

def start_quiz():
    st.session_state.screen = 'quiz'
    st.session_state.idx = 0
    st.session_state.revealed = False

# ホーム画面
if st.session_state.screen == 'home':
    st.title("☁️ Salesforce PD1 Master")
    st.info("Salesforce 認定 Platform デベロッパー I 試験対策クイズ")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 クイズを開始"): start_quiz()
    with col2:
        if st.button("📊 統計を表示"): st.session_state.screen = 'status'

# クイズ画面
elif st.session_state.screen == 'quiz':
    q = QUESTIONS[st.session_state.idx]
    
    st.progress((st.session_state.idx + 1) / len(QUESTIONS))
    st.write(f"**Question {st.session_state.idx + 1} of {len(QUESTIONS)}**")
    
    with st.container():
        st.markdown(f"<div class='q-card'><h3>{q['text']}</h3></div>", unsafe_allow_html=True)
        
        # 選択肢ボタン
        for opt in q['options']:
            letter = opt[0]
            btn_label = opt
            if st.session_state.revealed:
                if letter in q['ans']: btn_label = "✅ " + opt
                else: btn_label = "⚪ " + opt
            
            if st.button(btn_label, key=opt, disabled=st.session_state.revealed):
                st.session_state.revealed = True
                st.session_state.results[st.session_state.idx] = (letter in q['ans'])
                st.rerun()

    if st.session_state.revealed:
        is_correct = st.session_state.results.get(st.session_state.idx, False)
        if is_correct: st.success("正解です！")
        else: st.error(f"不正解です。正解は {q['ans']} です。")
        
        st.markdown(f"<div class='exp-box'><strong>解説:</strong><br>{q['exp']}</div>", unsafe_allow_html=True)
        
        if st.button("次へ ➡️"):
            if st.session_state.idx < len(QUESTIONS) - 1:
                st.session_state.idx += 1
                st.session_state.revealed = False
                st.rerun()
            else:
                st.session_state.screen = 'result'
                st.rerun()

# 結果・統計
elif st.session_state.screen in ['result', 'status']:
    st.header("📊 学習結果")
    total = len(st.session_state.results)
    if total > 0:
        correct = sum(st.session_state.results.values())
        rate = (correct / total) * 100
        st.metric("正答率", f"{rate:.1f}%")
        st.write(f"解答数: {total} | 正解数: {correct}")
    else:
        st.warning("まだ解答した問題がありません。")
        
    if st.button("🏠 ホームに戻る"):
        st.session_state.screen = 'home'
        st.rerun()
