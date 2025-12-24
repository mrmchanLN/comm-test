import streamlit as st
import pandas as pd

# 1. 質問とカテゴリの定義
questions = [
    ("1. 自己主張することが下手だと思う", "A"), ("2. 常に未来に対して、情熱を持っているほうだ", "B"),
    ("3. 他人のためにしたことを感謝されないと悔しく思うことがよくある", "C"), ("4. 嫌なことは嫌と、はっきり言える", "D"),
    ("5. 人にはなかなか気を許さない", "A"), ("6. 人から楽しい人とよく言われる", "B"),
    ("7. 短い時間に出来るだけ多くのことをしようとする", "C"), ("8. 失敗しても立ち直りが早い", "D"),
    ("9. 人からものを頼まれるとなかなかノーと言えない", "A"), ("10. たくさんの情報を検討してから決断をくだす", "B"),
    ("11. 人の話を聞くことよりも、自分が話していることのほうが多い", "C"), ("12. どちらかというと人見知りするほうだ", "D"),
    ("13. 自分と他人をよく比較する", "A"), ("14. 変化に強く対応力がある", "B"),
    ("15. 何事も自分の感情を表現することが苦手だ", "C"), ("16. 相手の好き嫌いに関わらず、人の世話をしてしまう", "D"),
    ("17. 自分が思ったことはストレートに言う", "A"), ("18. 仕事の出来栄えについて人から認められたい", "B"),
    ("19. 競争心が強い", "C"), ("20. 何事でも完全にしないと気が済まない", "D"),
]

# タイプ名と解説
type_names = {"A": "コントローラー", "B": "プロモーター", "C": "サポーター", "D": "アナライザー"}
type_descriptions = {
    "A": "行動的で決断が早く、結果を重視するタイプ。効率を好み、単刀直入なコミュニケーションを好みます。",
    "B": "活気に満ち、アイデアが豊富。人を巻き込むのが得意で、変化や刺激を好みます。",
    "C": "協調性が高く、周囲への配慮を大切にする。聞き上手で、チームの和を重視します。",
    "D": "客観的なデータや論理を重視。慎重に分析してから行動し、正確さを大切にします。"
}

st.set_page_config(page_title="コミュニケーション診断")
st.title("📊 コミュニケーション診断")
st.write("各項目について、自分にどの程度あてはまるか選択してください。")

# 集計用
scores = {"A": 0, "B": 0, "C": 0, "D": 0}
options = {1: "あてはまらない", 2: "あまりあてはまらない", 3: "あてはまる", 4: "よくあてはまる"}

with st.form("survey_form"):
    for q_text, cat in questions:
        res = st.radio(q_text, options=[1, 2, 3, 4], format_func=lambda x: options[x], horizontal=True)
        scores[cat] += res
    submitted = st.form_submit_button("診断結果を表示する")

if submitted:
    st.divider()
    
    # 1. 最大スコアとタイプの判定（同率対応）
    max_val = max(scores.values())
    max_types = [k for k, v in scores.items() if v == max_val]
    result_names = [type_names[t] for t in max_types]
    
    st.header(f"診断結果：あなたは 「{' ・ '.join(result_names)}」 タイプです")

    # 2. グラフの表示（ここが復活した部分です！）
    res_df = pd.DataFrame([{"タイプ": type_names[k], "スコア": v} for k, v in scores.items()])
    st.bar_chart(res_df.set_index("タイプ"))

    # 3. 各タイプの特徴表示
    for t in max_types:
        with st.expander(f"💡 {type_names[t]} の特徴をもっと見る"):
            st.write(type_descriptions[t])

    # 4. 数値詳細
    st.write("### スコア詳細")
    st.table(res_df)}」 タイプです")
