import streamlit as st

# 초기값 설정
if "num1" not in st.session_state:
    st.session_state.num1 = 0
if "num2" not in st.session_state:
    st.session_state.num2 = 0
if "result" not in st.session_state:
    st.session_state.result = None

st.title("✨ 계산기")
# st.markdown(
#     """
#     숫자를 입력하거나 버튼으로 조작하여 계산을 수행하세요.  
#     **연산 버튼을 클릭**하면 결과가 아래에 표시됩니다.
#     """
# )

# 첫 번째 숫자 입력과 버튼 조작
st.subheader("🔢 첫 번째 숫자:")
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("➖ 1", key="dec_num1"):
        st.session_state.num1 -= 1
with col2:
    num1 = st.number_input("첫 번째 숫자를 입력하세요", value=st.session_state.num1, step=1, key="input_num1")
    st.session_state.num1 = num1  # 입력 값을 세션 상태에 저장
with col3:
    if st.button("➕ 1", key="inc_num1"):
        st.session_state.num1 += 1

# 두 번째 숫자 입력과 버튼 조작
st.subheader("🔢 두 번째 숫자:")
col4, col5, col6 = st.columns([1, 2, 1])
with col4:
    if st.button("➖ 1", key="dec_num2"):
        st.session_state.num2 -= 1
with col5:
    num2 = st.number_input("두 번째 숫자를 입력하세요", value=st.session_state.num2, step=1, key="input_num2")
    st.session_state.num2 = num2  # 입력 값을 세션 상태에 저장
with col6:
    if st.button("➕ 1", key="inc_num2"):
        st.session_state.num2 += 1

# 연산 버튼 섹션
st.subheader("⚙️ 연산:")
col7, col8, col9, col10 = st.columns(4)
with col7:
    if st.button("➕ 덧셈"):
        st.session_state.result = st.session_state.num1 + st.session_state.num2
with col8:
    if st.button("➖ 뺄셈"):
        st.session_state.result = st.session_state.num1 - st.session_state.num2
with col9:
    if st.button("✖️ 곱셈"):
        st.session_state.result = st.session_state.num1 * st.session_state.num2
with col10:
    if st.button("➗ 나눗셈"):
        if st.session_state.num2 == 0:
            st.session_state.result = "에러: 0으로 나눌 수 없습니다."
        else:
            st.session_state.result = st.session_state.num1 / st.session_state.num2

# 결과 출력
st.markdown("---")
st.subheader("📝 결과:")
if st.session_state.result is not None:
    st.success(f"계산 결과: {st.session_state.result}")
else:
    st.info("연산 버튼을 클릭하여 결과를 확인하세요.")
