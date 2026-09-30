import streamlit as st
from services.persistence.exercise_repository import get_or_create_user


def render_profile_card():
    username = st.session_state.get("username", "User")
    user_id = st.session_state.get("user_id", "")

    st.sidebar.markdown(
        f"""
        <div style="
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 8px;
            padding: 14px 16px;
            margin-bottom: 8px;
        ">
            <div style="display:flex; align-items:center; gap:10px;">
                <div style="
                    width:40px; height:40px;
                    border-radius:50%;
                    background: linear-gradient(135deg, #f5a623, #00d4ff);
                    display:flex; align-items:center; justify-content:center;
                    font-size:18px; font-weight:bold; color:#000;
                    flex-shrink:0;
                ">
                    {username[0].upper()}
                </div>
                <div>
                    <div style="font-weight:600; font-size:15px; color:#eee;">
                        {username}
                    </div>
                    <div style="font-size:11px; color:#666;">
                        ID: {user_id}
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.sidebar.button("🚪 Logout", key="logout_btn", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True
    
    st.title("🏋️‍♂️ AI Real-time GYM Trainer")
    st.markdown("### Welcome! Please enter a username to start.")

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Name (unique)", placeholder="unique name e.g. aicoach69")
        submit_button = st.form_submit_button("Start Session", width="stretch")

    if submit_button:
        if not username:
            st.error("Name cannot be empty.")
            return False
        
        user = get_or_create_user(username)
    
        st.session_state["user_id"] = user["id"]
        st.session_state["username"] = user["username"]

        st.rerun()

    return False

