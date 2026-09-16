import streamlit as st
import pandas as pd
import sys

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Hospital Appointment Management System",
    page_icon="🏥",
    layout="wide"
)

# ============================================================
# MODERN HOSPITAL UI THEME
# ============================================================

st.markdown("""
<style>

    /* ================= MAIN BACKGROUND ================= */

    .stApp {
        background: #eef4f9;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-left: 2.8rem;
        padding-right: 2.8rem;
        padding-bottom: 3rem;
        max-width: 1500px;
    }


    /* ================= SIDEBAR ================= */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #123b66 0%,
            #195384 50%,
            #21618f 100%
        );
        border-right: none;
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 1.5rem;
    }

    section[data-testid="stSidebar"] * {
        color: #f5f9fc;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: white;
    }

    section[data-testid="stSidebar"] .stRadio label {
        color: #e8f2f9;
        font-weight: 500;
    }


    /* ================= HEADINGS ================= */

    h1 {
        color: #123b66;
        font-size: 2.25rem !important;
        font-weight: 750;
        letter-spacing: -0.6px;
        margin-bottom: 0.25rem;
    }

    h2 {
        color: #174d78;
        font-weight: 700;
    }

    h3 {
        color: #245d88;
        font-weight: 650;
    }

    p {
        color: #526b80;
    }


    /* ================= DIVIDERS ================= */

    hr {
        border: none;
        border-top: 1px solid #d7e4ee;
        margin: 1.4rem 0;
    }

    /* ================= DASHBOARD KPI CARDS ================= */

    .dashboard-kpi-card {
        background: rgba(255, 255, 255, 0.96);
        border: 1px solid #d8e6f2;
        border-radius: 18px;
        padding: 22px 22px 20px 22px;
        min-height: 145px;
        box-shadow: 0 5px 18px rgba(30, 70, 100, 0.08);
        transition: 0.2s ease;
    }

    .dashboard-kpi-card:hover {
        box-shadow: 0 8px 24px rgba(30, 70, 100, 0.12);
        transform: translateY(-2px);
    }

    .dashboard-kpi-card.blue {
        border-left: 5px solid #2f80ed;
    }

    .dashboard-kpi-card.green {
        border-left: 5px solid #27ae60;
    }

    .dashboard-kpi-card.red {
        border-left: 5px solid #eb5757;
    }

    .dashboard-kpi-card.teal {
        border-left: 5px solid #2d9cdb;
    }

    .dashboard-kpi-card.purple {
        border-left: 5px solid #8b6fd8;
    }

    .kpi-icon {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 23px;
        margin-bottom: 13px;
        background: #eaf4ff;
    }

    .kpi-label {
        font-size: 15px;
        font-weight: 600;
        color: #52677a;
        margin-bottom: 5px;
    }

    .kpi-value {
        font-size: 30px;
        font-weight: 750;
        color: #123b63;
        line-height: 1.15;
        margin-bottom: 8px;
    }

    .kpi-description {
        font-size: 12px;
        line-height: 1.45;
        color: #718397;
    }
            
/* ================= PREDICTION BUTTON ================= */

.stButton > button,
.stButton > button p,
.stButton > button span {
    background: #286da5 !important;
    color: #ffffff !important;
}

.stButton > button {
    border: none !important;
    border-radius: 11px !important;
    padding: 0.7rem 1.2rem !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    box-shadow: 0 4px 12px rgba(40, 109, 165, 0.18);
}

.stButton > button:hover,
.stButton > button:hover p,
.stButton > button:hover span {
    background: #1f5d90 !important;
    color: #ffffff !important;
}
            
/* ================= INPUT CARDS ================= */

.prediction-input-card {
    background: rgba(255, 255, 255, 0.92);
    border: 1px solid #cfe1ef;
    border-radius: 15px;
    padding: 15px 16px 10px 16px;
    margin-bottom: 16px;
    box-shadow: 0 4px 14px rgba(31, 72, 105, 0.06);
}

.prediction-input-card:hover {
    border-color: #9fc9e8;
    box-shadow: 0 6px 18px rgba(31, 72, 105, 0.09);
}

/* Input labels */

.prediction-input-card label {
    color: #245d88 !important;
    font-weight: 650 !important;
}

/* Input fields */

.prediction-input-card input {
    background: #ffffff !important;
    border: 1px solid #cfe1ef !important;
    border-radius: 10px !important;
}

/* Select boxes */

.prediction-input-card div[data-baseweb="select"] {
    background: #ffffff !important;
    border: 1px solid #cfe1ef !important;
    border-radius: 10px !important;
}


/* ================= PREDICTION BUTTON ================= */

.stButton > button {
    background: #286da5 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 11px !important;
    padding: 0.7rem 1.2rem !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    box-shadow: 0 4px 12px rgba(40, 109, 165, 0.18);
}

.stButton > button:hover {
    background: #1f5d90 !important;
    color: #ffffff !important;
}
            
    /* ================= TABLES ================= */

    div[data-testid="stDataFrame"] {
        background: white;
        border: 1px solid #d7e5ef;
        border-radius: 14px;
        overflow: hidden;
        box-shadow: 0 4px 14px rgba(31, 72, 105, 0.05);
    }


    /* ================= ALERTS ================= */

    div[data-testid="stAlert"] {
        border-radius: 12px;
        border: 1px solid #d7e5ef;
    }


    /* ================= EXPANDERS ================= */

    div[data-testid="stExpander"] {
        background: white;
        border: 1px solid #d7e5ef;
        border-radius: 13px;
        box-shadow: 0 3px 12px rgba(31, 72, 105, 0.05);
    }


    /* ================= DATAFRAME TEXT ================= */

    div[data-testid="stDataFrame"] * {
        font-size: 0.92rem;
    }


    /* ================= SIDEBAR RADIO ================= */

    section[data-testid="stSidebar"] div[role="radiogroup"] {
        gap: 0.35rem;
    }

</style>
""", unsafe_allow_html=True)

# Add src folder
if "src" not in sys.path:
    sys.path.append("src")

from prediction import (
    load_no_show_model,
    predict_no_show,
    classify_no_show_risk
)
from preprocessing import prepare_appointment_data
from booking import (
    load_bookings,
    is_slot_booked,
    save_booking
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    df = pd.read_csv("data/KaggleV2-May-2016.csv")

    df["Attendance_Status"] = df["No-show"].map({
        "No": "Attended",
        "Yes": "No-Show"
    })

    df["Waiting_Days"] = (
        pd.to_datetime(df["AppointmentDay"]) -
        pd.to_datetime(df["ScheduledDay"])
    ).dt.days.clip(lower=0)

    df["Weekday"] = pd.to_datetime(
        df["AppointmentDay"]
    ).dt.day_name()

    df["Age_Clean"] = df["Age"].replace(-1, float("nan"))

    return df


@st.cache_data
def load_hospital_config():
    return pd.read_csv("data/hospital_config.csv")


@st.cache_data
def load_available_slots():
    return pd.read_csv("data/available_slots.csv")


@st.cache_resource
def load_prediction_model():
    return load_no_show_model(
        "models/no_show_model.pkl"
    )


df = load_data()
hospital_config = load_hospital_config()
available_slots = load_available_slots()

model, prediction_threshold = load_prediction_model()


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.title("🏥 Hospital System")
st.sidebar.caption("Appointment & Capacity Management")

page = st.sidebar.radio(
    "Navigate to",
    [
        "🏠 Dashboard",
        "📊 Appointment Analytics",
        "🤖 No-Show Prediction",
        "🏥 Capacity Management",
        "📅 Appointment Scheduling",
        "ℹ️ About Project"
    ]
)

st.sidebar.divider()
st.sidebar.caption(
    "Data-driven hospital operations system"
)


# ============================================================
# COMMON KPI VALUES
# ============================================================

total_appointments = len(df)

attended_appointments = (
    df["No-show"] == "No"
).sum()

no_show_appointments = (
    df["No-show"] == "Yes"
).sum()

attendance_rate = (
    attended_appointments /
    total_appointments * 100
)

no_show_rate = (
    no_show_appointments /
    total_appointments * 100
)

# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.title("🏥 Hospital Appointment Management System")
    st.write(
        "Smart appointment scheduling, no-show prediction "
        "and capacity management"
    )

    st.divider()

    st.subheader("📊 Key Performance Indicators")

    # ============================================================
    # KPI CARDS - ROW 1
    # ============================================================

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown(
            f"""
            <div class="dashboard-kpi-card blue">
                <div class="kpi-icon">📅</div>
                <div class="kpi-label">Total Appointments</div>
                <div class="kpi-value">{total_appointments:,}</div>
                <div class="kpi-description">
                    Total appointments in the historical dataset.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="dashboard-kpi-card green">
                <div class="kpi-icon">👥</div>
                <div class="kpi-label">Attended</div>
                <div class="kpi-value">{attended_appointments:,}</div>
                <div class="kpi-description">
                    Appointments where the patient attended.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="dashboard-kpi-card red">
                <div class="kpi-icon">🚫</div>
                <div class="kpi-label">No-Shows</div>
                <div class="kpi-value">{no_show_appointments:,}</div>
                <div class="kpi-description">
                    Appointments where the patient did not attend.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ============================================================
    # KPI CARDS - ROW 2
    # ============================================================

    st.write("")

    col4, col5 = st.columns(2, gap="large")

    with col4:
        st.markdown(
            f"""
            <div class="dashboard-kpi-card teal">
                <div class="kpi-icon">📈</div>
                <div class="kpi-label">Attendance Rate</div>
                <div class="kpi-value">{attendance_rate:.2f}%</div>
                <div class="kpi-description">
                    Percentage of appointments attended.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col5:
        st.markdown(
            f"""
            <div class="dashboard-kpi-card purple">
                <div class="kpi-icon">↘️</div>
                <div class="kpi-label">No-Show Rate</div>
                <div class="kpi-value">{no_show_rate:.2f}%</div>
                <div class="kpi-description">
                    Percentage of appointments recorded as no-shows.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()
    # ============================================================
    # APPOINTMENT OVERVIEW
    # ============================================================

    st.subheader("📋 Appointment Overview")

    # ============================================================
    # OVERVIEW PANELS
    # ============================================================

    col1, col2 = st.columns(2, gap="large")

    # ------------------------------------------------------------
    # ATTENDANCE DISTRIBUTION
    # ------------------------------------------------------------

    with col1:
        with st.container(border=True):

            st.markdown(
                """
                <div style="
                    font-size: 18px;
                    font-weight: 700;
                    color: #174d78;
                    margin-bottom: 10px;
                ">
                    📊 Attendance Distribution
                </div>
                """,
                unsafe_allow_html=True
            )

            attendance_counts = (
                df["Attendance_Status"]
                .value_counts()
            )

            st.bar_chart(
                attendance_counts,
                height=280
            )

    # ------------------------------------------------------------
    # DATASET INFORMATION
    # ------------------------------------------------------------

    with col2:
        with st.container(border=True):

            st.markdown(
                """
                <div style="
                    font-size: 18px;
                    font-weight: 700;
                    color: #174d78;
                    margin-bottom: 20px;
                ">
                    📁 Dataset Information
                </div>
                """,
                unsafe_allow_html=True
            )

            info_col1, info_col2, info_col3 = st.columns(3)

            with info_col1:
                st.markdown(
                    f"""
                    <div style="
                        text-align: center;
                        padding: 18px 8px;
                        background: #f3f8fc;
                        border-radius: 12px;
                    ">
                        <div style="
                            font-size: 13px;
                            color: #627b90;
                            font-weight: 600;
                        ">
                            Records
                        </div>
                        <div style="
                            font-size: 26px;
                            color: #174d78;
                            font-weight: 750;
                            margin-top: 6px;
                        ">
                            {len(df):,}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with info_col2:
                st.markdown(
                    f"""
                    <div style="
                        text-align: center;
                        padding: 18px 8px;
                        background: #f3f8fc;
                        border-radius: 12px;
                    ">
                        <div style="
                            font-size: 13px;
                            color: #627b90;
                            font-weight: 600;
                        ">
                            Variables
                        </div>
                        <div style="
                            font-size: 26px;
                            color: #174d78;
                            font-weight: 750;
                            margin-top: 6px;
                        ">
                            {df.shape[1]}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with info_col3:
                st.markdown(
                    f"""
                    <div style="
                        text-align: center;
                        padding: 18px 8px;
                        background: #f3f8fc;
                        border-radius: 12px;
                    ">
                        <div style="
                            font-size: 13px;
                            color: #627b90;
                            font-weight: 600;
                        ">
                            Neighbourhoods
                        </div>
                        <div style="
                            font-size: 26px;
                            color: #174d78;
                            font-weight: 750;
                            margin-top: 6px;
                        ">
                            {df['Neighbourhood'].nunique()}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.write("")
    # ============================================================
    # NO-SHOW SUMMARY
    # ============================================================

    st.info(
        f"📌 **Attendance Summary**\n\n"
        f"Approximately **{no_show_rate:.1f}%** of appointments "
        f"in the dataset were recorded as no-shows."
    )
    # ============================================================
    # SYSTEM FEATURES
    # ============================================================

    st.subheader("🔎 System Features")

    feature_col1, feature_col2, feature_col3 = st.columns(
        3,
        gap="large"
    )

    with feature_col1:
        with st.container(border=True):

            st.markdown(
                """
                <div style="
                    font-size: 22px;
                    margin-bottom: 8px;
                ">
                    📊
                </div>

                <div style="
                    font-size: 17px;
                    font-weight: 700;
                    color: #174d78;
                    margin-bottom: 8px;
                ">
                    Appointment Analytics
                </div>

                <div style="
                    font-size: 13px;
                    line-height: 1.6;
                    color: #627b90;
                ">
                    Explore appointment patterns, waiting time,
                    SMS reminders, age groups and neighbourhood
                    trends.
                </div>
                """,
                unsafe_allow_html=True
            )

    with feature_col2:
        with st.container(border=True):

            st.markdown(
                """
                <div style="
                    font-size: 22px;
                    margin-bottom: 8px;
                ">
                    🤖
                </div>

                <div style="
                    font-size: 17px;
                    font-weight: 700;
                    color: #174d78;
                    margin-bottom: 8px;
                ">
                    No-Show Prediction
                </div>

                <div style="
                    font-size: 13px;
                    line-height: 1.6;
                    color: #627b90;
                ">
                    Estimate appointment no-show probability
                    using the trained machine learning model.
                </div>
                """,
                unsafe_allow_html=True
            )

    with feature_col3:
        with st.container(border=True):

            st.markdown(
                """
                <div style="
                    font-size: 22px;
                    margin-bottom: 8px;
                ">
                    🏥
                </div>

                <div style="
                    font-size: 17px;
                    font-weight: 700;
                    color: #174d78;
                    margin-bottom: 8px;
                ">
                    Capacity & Scheduling
                </div>

                <div style="
                    font-size: 13px;
                    line-height: 1.6;
                    color: #627b90;
                ">
                    Monitor simulated departmental capacity
                    and recommend available appointment slots.
                </div>
                """,
                unsafe_allow_html=True
            )

    st.divider()

# ============================================================
# APPOINTMENT ANALYTICS
# ============================================================

elif page == "📊 Appointment Analytics":

    st.divider()

    st.header("📊 Appointment Analytics")

    st.write(
        "Explore appointment attendance and no-show patterns "
        "from the historical appointment dataset."
    )

    # --------------------------------------------------------
    # WEEKDAY ANALYSIS
    # --------------------------------------------------------

    st.subheader(
        "📅 Appointments and No-Show Rate by Weekday"
    )

    weekday_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    weekday_analysis = (
        df.groupby("Weekday")
        .agg(
            Appointments=("AppointmentID", "count"),
            No_Shows=(
                "No-show",
                lambda x: (x == "Yes").sum()
            )
        )
        .reindex(weekday_order)
    )

    weekday_analysis["No_Show_Rate"] = (
        weekday_analysis["No_Shows"] /
        weekday_analysis["Appointments"] * 100
    ).round(2)

    st.dataframe(
        weekday_analysis,
        use_container_width=True
    )

    # --------------------------------------------------------
    # WAITING TIME
    # --------------------------------------------------------

    st.subheader("⏳ No-Show Rate by Waiting Time")

    waiting_bins = [
        -1, 0, 7, 14, 30, 60, float("inf")
    ]

    waiting_labels = [
        "Same Day",
        "1-7 Days",
        "8-14 Days",
        "15-30 Days",
        "31-60 Days",
        "61+ Days"
    ]

    df["Waiting_Group"] = pd.cut(
        df["Waiting_Days"],
        bins=waiting_bins,
        labels=waiting_labels
    )

    waiting_analysis = (
        df.groupby(
            "Waiting_Group",
            observed=False
        )
        .agg(
            Appointments=("AppointmentID", "count"),
            No_Shows=(
                "No-show",
                lambda x: (x == "Yes").sum()
            )
        )
    )

    waiting_analysis["No_Show_Rate"] = (
        waiting_analysis["No_Shows"] /
        waiting_analysis["Appointments"] * 100
    ).round(2)

    st.dataframe(
        waiting_analysis,
        use_container_width=True
    )

    # --------------------------------------------------------
    # SMS ANALYSIS
    # --------------------------------------------------------

    st.subheader("📱 No-Show Rate by SMS Reminder")

    sms_analysis = (
        df.groupby("SMS_received")
        .agg(
            Appointments=("AppointmentID", "count"),
            No_Shows=(
                "No-show",
                lambda x: (x == "Yes").sum()
            )
        )
    )

    sms_analysis["No_Show_Rate"] = (
        sms_analysis["No_Shows"] /
        sms_analysis["Appointments"] * 100
    ).round(2)

    sms_analysis.index = sms_analysis.index.map({
        0: "No SMS Received",
        1: "SMS Received"
    })

    st.dataframe(
        sms_analysis,
        use_container_width=True
    )

    # --------------------------------------------------------
    # AGE GROUP
    # --------------------------------------------------------

    st.subheader("👥 No-Show Rate by Age Group")

    df["Age_Group"] = pd.cut(
        df["Age_Clean"],
        bins=[-1, 17, 30, 45, 60, 120],
        labels=[
            "0-17",
            "18-30",
            "31-45",
            "46-60",
            "61+"
        ]
    )

    age_analysis = (
        df.groupby(
            "Age_Group",
            observed=False
        )
        .agg(
            Appointments=("AppointmentID", "count"),
            No_Shows=(
                "No-show",
                lambda x: (x == "Yes").sum()
            )
        )
    )

    age_analysis["No_Show_Rate"] = (
        age_analysis["No_Shows"] /
        age_analysis["Appointments"] * 100
    ).round(2)

    st.dataframe(
        age_analysis,
        use_container_width=True
    )

    # --------------------------------------------------------
    # NEIGHBOURHOOD
    # --------------------------------------------------------

    st.subheader("📍 No-Show Rate by Neighbourhood")

    neighbourhood_analysis = (
        df.groupby("Neighbourhood")
        .agg(
            Appointments=("AppointmentID", "count"),
            No_Shows=(
                "No-show",
                lambda x: (x == "Yes").sum()
            )
        )
    )

    neighbourhood_analysis["No_Show_Rate"] = (
        neighbourhood_analysis["No_Shows"] /
        neighbourhood_analysis["Appointments"] * 100
    ).round(2)

    neighbourhood_analysis = (
        neighbourhood_analysis[
            neighbourhood_analysis["Appointments"] >= 500
        ]
        .sort_values(
            "No_Show_Rate",
            ascending=False
        )
    )

    st.dataframe(
        neighbourhood_analysis,
        use_container_width=True
    )

    st.caption(
        "Neighbourhoods with fewer than 500 appointments "
        "are excluded from this table to reduce the influence "
        "of very small samples."
    )


# ============================================================
# NO-SHOW PREDICTION
# ============================================================

elif page == "🤖 No-Show Prediction":

    st.divider()

    st.header("🤖 No-Show Risk Prediction")

    st.write(
        "Enter appointment details to estimate the probability "
        "of the appointment being a no-show."
    )

    st.info(
        "This prediction is intended to support hospital "
        "appointment planning and reminder decisions. "
        "It is not a medical diagnosis or clinical "
        "decision-making tool."
    )

    # --------------------------------------------------------
    # INPUTS
    # --------------------------------------------------------

    col1, col2, col3 = st.columns(3, gap="large")

    # ========================================================
    # COLUMN 1
    # ========================================================

    with col1:

        with st.container(border=True):
            gender = st.selectbox(
                "Gender",
                ["F", "M"]
            )

        with st.container(border=True):
            age = st.number_input(
                "Age",
                min_value=0,
                max_value=120,
                value=30
            )

        with st.container(border=True):
            neighbourhood = st.selectbox(
                "Neighbourhood",
                sorted(
                    df["Neighbourhood"]
                    .dropna()
                    .unique()
                )
            )

        with st.container(border=True):
            scholarship = st.selectbox(
                "Scholarship",
                [0, 1]
            )

    # ========================================================
    # COLUMN 2
    # ========================================================

    with col2:

        with st.container(border=True):
            hypertension = st.selectbox(
                "Hypertension",
                [0, 1]
            )

        with st.container(border=True):
            diabetes = st.selectbox(
                "Diabetes",
                [0, 1]
            )

        with st.container(border=True):
            alcoholism = st.selectbox(
                "Alcoholism",
                [0, 1]
            )

        with st.container(border=True):
            handcap = st.selectbox(
                "Handicap",
                [0, 1, 2, 3, 4]
            )

    # ========================================================
    # COLUMN 3
    # ========================================================

    with col3:

        with st.container(border=True):
            sms_received = st.selectbox(
                "SMS Received",
                [0, 1]
            )

        with st.container(border=True):
            waiting_days = st.number_input(
                "Waiting Days",
                min_value=0,
                max_value=365,
                value=10
            )

        with st.container(border=True):
            appointment_weekday = st.selectbox(
                "Appointment Weekday",
                list(range(7)),
                format_func=lambda x: [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                    "Sunday"
                ][x]
            )

        with st.container(border=True):
            appointment_month = st.selectbox(
                "Appointment Month",
                list(range(1, 13))
            )

        with st.container(border=True):
            scheduled_hour = st.number_input(
                "Scheduled Hour",
                min_value=0,
                max_value=23,
                value=10
            )

    st.divider()

    if st.button(
        "🔍 Predict No-Show Risk",
        use_container_width=True
    ):

        appointment_data = prepare_appointment_data(
            gender,
            age,
            neighbourhood,
            scholarship,
            hypertension,
            diabetes,
            alcoholism,
            handcap,
            sms_received,
            waiting_days,
            appointment_weekday,
            appointment_month,
            scheduled_hour
        )

        probability = predict_no_show(
            model,
            appointment_data
        )

        risk = classify_no_show_risk(
            probability
        )

        st.session_state[
            "prediction_probability"
        ] = probability

        st.session_state[
            "prediction_risk"
        ] = risk

        st.subheader("Prediction Result")

        result_col1, result_col2 = st.columns(2)

        with result_col1:

            st.metric(
                "No-Show Probability",
                f"{probability * 100:.2f}%"
            )

        with result_col2:

            if risk == "Low Risk":
                st.success(
                    f"Risk Level: {risk}"
                )

            elif risk == "Medium Risk":
                st.warning(
                    f"Risk Level: {risk}"
                )

            else:
                st.error(
                    f"Risk Level: {risk}"
                )

        st.info(
            "This prediction is based on patterns learned "
            "from the historical appointment dataset and "
            "should be used as an operational planning aid."
        )


# ============================================================
# CAPACITY MANAGEMENT
# ============================================================

elif page == "🏥 Capacity Management":

    st.divider()

    st.header("🏥 Capacity Management")

    st.write(
        "Compare estimated departmental demand with "
        "simulated hospital capacity to identify areas "
        "with available or insufficient capacity."
    )

    st.info(
        "ℹ️ Department capacities and demand weights are "
        "simulated operational values created for project "
        "demonstration. They are not actual hospital data."
    )

    # --------------------------------------------------------
    # DEMAND WEIGHTS
    # --------------------------------------------------------

    demand_weights = {
        "General Medicine": 1.20,
        "Cardiology": 0.80,
        "Orthopedics": 1.10,
        "Pediatrics": 0.90,
        "Dermatology": 0.65
    }

    capacity_data = hospital_config.copy()

    capacity_data["Demand_Weight"] = (
        capacity_data["Department"]
        .map(demand_weights)
    )

    capacity_data["Weighted_Demand"] = (
        capacity_data["Daily_Capacity"] *
        capacity_data["Demand_Weight"]
    )

    total_weighted_demand = (
        capacity_data["Weighted_Demand"].sum()
    )

    # IMPORTANT:
    # Demand is scaled to the simulated total daily capacity,
    # as used in the validated project calculation.

    capacity_data["Estimated_Daily_Demand"] = (
        capacity_data["Weighted_Demand"]
        / total_weighted_demand
        * capacity_data["Daily_Capacity"].sum()
    ).round().astype(int)

    capacity_data["Estimated_Utilization"] = (
        capacity_data["Estimated_Daily_Demand"]
        / capacity_data["Daily_Capacity"] * 100
    ).round(2)

    capacity_data["Spare_Capacity"] = (
        capacity_data["Daily_Capacity"]
        - capacity_data["Estimated_Daily_Demand"]
    )

    def get_capacity_status(utilization):

        if utilization < 70:
            return "Low"

        elif utilization < 90:
            return "Normal"

        elif utilization <= 100:
            return "High"

        else:
            return "Over Capacity"

    capacity_data["Capacity_Status"] = (
        capacity_data["Estimated_Utilization"]
        .apply(get_capacity_status)
    )

    def get_capacity_recommendation(row):

        if row["Spare_Capacity"] < 0:
            return (
                "Consider additional slots or "
                "capacity reallocation"
            )

        elif row["Spare_Capacity"] == 0:
            return "Capacity fully utilized"

        elif row["Estimated_Utilization"] >= 85:
            return "Monitor capacity closely"

        else:
            return "Capacity available"

    capacity_data["Recommendation"] = (
        capacity_data.apply(
            get_capacity_recommendation,
            axis=1
        )
    )

    # --------------------------------------------------------
    # STATUS SUMMARY
    # --------------------------------------------------------

    st.subheader("📌 Capacity Status Summary")

    over_capacity = (
        capacity_data["Capacity_Status"]
        == "Over Capacity"
    ).sum()

    available_capacity = (
        capacity_data["Capacity_Status"]
        == "Low"
    ).sum()

    monitor_capacity = (
        capacity_data["Capacity_Status"]
        .isin(["Normal", "High"])
    ).sum()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🔴 Over Capacity",
            f"{over_capacity} Departments"
        )

    with col2:
        st.metric(
            "🟢 Available Capacity",
            f"{available_capacity} Departments"
        )

    with col3:
        st.metric(
            "🟡 Monitor",
            f"{monitor_capacity} Departments"
        )

    # --------------------------------------------------------
    # CAPACITY TABLE
    # --------------------------------------------------------

    st.subheader("Department Capacity Overview")

    display_columns = [
        "Department",
        "Doctors",
        "Daily_Capacity",
        "Estimated_Daily_Demand",
        "Estimated_Utilization",
        "Spare_Capacity",
        "Capacity_Status",
        "Recommendation"
    ]

    st.dataframe(
        capacity_data[display_columns],
        use_container_width=True
    )

    st.info(
        "Note: Department capacity and demand values are "
        "simulated because the original dataset does not "
        "contain hospital department, doctor or "
        "slot-capacity information."
    )


# ============================================================
# APPOINTMENT SCHEDULING
# ============================================================

elif page == "📅 Appointment Scheduling":

    st.divider()

    st.header("📅 Appointment Scheduling & Booking")

    st.write(
        "Select a patient, department, appointment date "
        "and preferred time to find and book an available "
        "appointment slot."
    )

    st.info(
        "💡 Selecting a slot does not book it. "
        "A booking is confirmed only after you click "
        "'Book Appointment'."
    )

    # --------------------------------------------------------
    # BOOKINGS
    # --------------------------------------------------------

    bookings = load_bookings(
        "data/bookings.csv"
    )

    # --------------------------------------------------------
    # DEPARTMENTS
    # --------------------------------------------------------

    available_departments = [
        "Cardiology",
        "Pediatrics",
        "Dermatology"
    ]

    st.success(
        "Departments currently available for appointment: "
        "Cardiology | Pediatrics | Dermatology"
    )

    st.warning(
        "General Medicine and Orthopedics are currently "
        "over simulated capacity and are not recommended "
        "for new appointments."
    )
    # --------------------------------------------------------
    # PATIENT DETAILS
    # --------------------------------------------------------

    st.subheader("Patient & Appointment Details")

    col1, col2 = st.columns(2, gap="large")

    # ========================================================
    # LEFT COLUMN
    # ========================================================

    with col1:

        with st.container(border=True):
            patient_name = st.text_input(
                "Patient Name"
            )

        with st.container(border=True):
            selected_department = st.selectbox(
                "Select Department",
                available_departments
            )

    # ========================================================
    # RIGHT COLUMN
    # ========================================================

    with col2:

        with st.container(border=True):
            appointment_date = st.date_input(
                "Appointment Date",
                min_value=pd.Timestamp.today().date(),
                max_value=(
                    pd.Timestamp.today() +
                    pd.Timedelta(days=90)
                ).date()
            )

        with st.container(border=True):
            preferred_time = st.selectbox(
                "Preferred Appointment Time",
                [
                    "09:00 AM",
                    "09:30 AM",
                    "10:00 AM",
                    "10:30 AM",
                    "11:00 AM",
                    "11:30 AM",
                    "12:00 PM",
                    "12:30 PM",
                    "01:00 PM",
                    "01:30 PM",
                    "02:00 PM",
                    "02:30 PM",
                    "03:00 PM",
                    "03:30 PM",
                    "04:00 PM",
                    "04:30 PM",
                    "05:00 PM",
                    "05:30 PM",
                    "06:00 PM"
                ]
            )

    # ========================================================
    # NUMBER OF SLOTS
    # ========================================================

    with st.container(border=True):
        number_of_slots = st.slider(
            "Number of slots to recommend",
            min_value=1,
            max_value=10,
            value=5
        )
    # --------------------------------------------------------
    # FIND AVAILABLE SLOTS
    # --------------------------------------------------------

    if st.button(
        "🔎 Find Available Slots",
        use_container_width=True
    ):

        department_slots = available_slots[
            available_slots["Department"]
            == selected_department
        ].copy()

        available_for_date = []

        for _, slot in department_slots.iterrows():

            already_booked = is_slot_booked(
                bookings,
                selected_department,
                slot["Doctor"],
                str(appointment_date),
                slot["Appointment_Time"]
            )

            if not already_booked:
                available_for_date.append(
                    slot
                )

        department_slots = pd.DataFrame(
            available_for_date
        )

        if department_slots.empty:

            st.error(
                "No available slots found for this "
                "department and date."
            )

            st.session_state.pop(
                "recommended_slots",
                None
            )

        else:

            preferred = pd.to_datetime(
                preferred_time,
                format="%I:%M %p"
            )

            department_slots[
                "Appointment_Time_dt"
            ] = pd.to_datetime(
                department_slots[
                    "Appointment_Time"
                ],
                format="%I:%M %p"
            )

            department_slots[
                "Time_Difference_Minutes"
            ] = (
                department_slots[
                    "Appointment_Time_dt"
                ] - preferred
            ).abs().dt.total_seconds() / 60

            department_slots = (
                department_slots
                .sort_values(
                    "Time_Difference_Minutes"
                )
            )

            recommended_slots = (
                department_slots
                .head(number_of_slots)
                .copy()
            )

            recommended_slots[
                "Recommendation_Rank"
            ] = range(
                1,
                len(recommended_slots) + 1
            )

            recommended_slots = (
                recommended_slots[
                    [
                        "Recommendation_Rank",
                        "Department",
                        "Doctor",
                        "Slot_Number",
                        "Appointment_Time",
                        "Time_Difference_Minutes"
                    ]
                ]
            )

            st.session_state[
                "recommended_slots"
            ] = recommended_slots

            st.session_state[
                "selected_date"
            ] = str(appointment_date)

            st.session_state[
                "selected_department"
            ] = selected_department

            st.success(
                f"{len(recommended_slots)} available "
                f"slot(s) found for {appointment_date}."
            )

    # --------------------------------------------------------
    # DISPLAY RECOMMENDED SLOTS
    # --------------------------------------------------------

    if "recommended_slots" in st.session_state:

        st.divider()

        st.subheader(
            "Recommended Appointment Slots"
        )

        recommended_slots = (
            st.session_state[
                "recommended_slots"
            ]
        )

        st.dataframe(
            recommended_slots,
            use_container_width=True
        )

        # ----------------------------------------------------
        # BOOKING FORM
        # ----------------------------------------------------

        st.subheader("Book an Appointment")

        with st.form("booking_form"):

            selected_slot_index = st.selectbox(
                "Select a slot to book",
                recommended_slots.index,
                format_func=lambda x:
                    f'{recommended_slots.loc[x, "Doctor"]}'
                    f' — '
                    f'{recommended_slots.loc[x, "Appointment_Time"]}'
            )

            selected_slot = (
                recommended_slots.loc[
                    selected_slot_index
                ]
            )

            book_now = st.form_submit_button(
                "✅ Book Appointment"
            )

        if book_now:

            if not patient_name.strip():

                st.error(
                    "Please enter the patient name "
                    "before booking."
                )

            else:

                # Reload latest bookings before checking
                # to prevent duplicate booking.

                bookings = load_bookings(
                    "data/bookings.csv"
                )

                already_booked = is_slot_booked(
                    bookings,
                    selected_slot["Department"],
                    selected_slot["Doctor"],
                    st.session_state[
                        "selected_date"
                    ],
                    selected_slot[
                        "Appointment_Time"
                    ]
                )

                if already_booked:

                    st.error(
                        "This slot has already been booked. "
                        "Please find available slots again."
                    )

                else:

                    booking_probability = (
                        st.session_state.get(
                            "prediction_probability",
                            0.0
                        )
                    )

                    booking_risk = (
                        st.session_state.get(
                            "prediction_risk",
                            "Not Predicted"
                        )
                    )

                    bookings, appointment_id = (
                        save_booking(
                            bookings,
                            patient_name,
                            selected_slot["Department"],
                            selected_slot["Doctor"],
                            st.session_state[
                                "selected_date"
                            ],
                            selected_slot[
                                "Appointment_Time"
                            ],
                            booking_probability,
                            booking_risk,
                            "data/bookings.csv"
                        )
                    )

                    st.success(
                        "Appointment booked successfully!"
                    )

                    st.write(
                        f"**Appointment ID:** "
                        f"{appointment_id}"
                    )

                    st.write(
                        f"**Patient:** {patient_name}"
                    )

                    st.write(
                        f"**Department:** "
                        f"{selected_slot['Department']}"
                    )

                    st.write(
                        f"**Doctor:** "
                        f"{selected_slot['Doctor']}"
                    )

                    st.write(
                        f"**Date:** "
                        f"{st.session_state['selected_date']}"
                    )

                    st.write(
                        f"**Time:** "
                        f"{selected_slot['Appointment_Time']}"
                    )

                    st.write(
                        f"**No-Show Probability:** "
                        f"{booking_probability * 100:.2f}%"
                    )

                    st.write(
                        f"**Risk Level:** "
                        f"{booking_risk}"
                    )

    st.caption(
        "Note: Doctor schedules, appointment slots and "
        "capacity are simulated for demonstration because "
        "the original dataset does not contain real hospital "
        "scheduling data."
    )


# ============================================================
# ABOUT PROJECT
# ============================================================

elif page == "ℹ️ About Project":

    st.divider()

    st.header("ℹ️ About the Project")

    st.write(
        "### Hospital Appointment Scheduling & "
        "Capacity Management System"
    )

    st.write(
        "This project is a data-driven hospital operations "
        "system developed using Python, Machine Learning "
        "and Streamlit."
    )

    st.divider()

    st.subheader("🎯 Project Objectives")

    st.markdown(
        """
        - Analyse historical hospital appointment data.
        - Identify appointment and attendance patterns.
        - Estimate the probability of appointment no-shows.
        - Analyse departmental capacity and demand.
        - Recommend suitable appointment slots.
        - Provide an interactive hospital operations dashboard.
        """
    )

    st.subheader("🧩 Main Modules")

    module_data = pd.DataFrame({
        "Module": [
            "Data Collection & Preprocessing",
            "Appointment Analytics",
            "No-Show Prediction",
            "Capacity Management",
            "Appointment Scheduling",
            "Streamlit Dashboard"
        ],
        "Purpose": [
            "Clean and prepare appointment data.",
            "Analyse appointment and attendance patterns.",
            "Estimate no-show probability.",
            "Compare simulated demand with capacity.",
            "Recommend and book available slots.",
            "Provide an interactive user interface."
        ]
    })

    st.dataframe(
        module_data,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("🛠️ Technologies Used")

    tech_col1, tech_col2, tech_col3 = st.columns(3)

    with tech_col1:
        st.markdown(
            "**Programming**\n\n"
            "Python\n\n"
            "Pandas\n\n"
            "NumPy"
        )

    with tech_col2:
        st.markdown(
            "**Machine Learning**\n\n"
            "Scikit-learn\n\n"
            "Random Forest\n\n"
            "Joblib"
        )

    with tech_col3:
        st.markdown(
            "**Interface**\n\n"
            "Streamlit\n\n"
            "Data Visualisation\n\n"
            "Interactive Dashboard"
        )

    st.divider()

    st.subheader("📊 Dataset")

    st.write(
        "The primary dataset is the Medical Appointment "
        "No Shows dataset containing historical appointment "
        "records. It is used for appointment analytics and "
        "no-show prediction."
    )

    st.warning(
        "Hospital departments, doctors, appointment slots "
        "and capacity values are simulated operational "
        "values created for demonstration because these "
        "details are not available in the original dataset."
    )

    st.divider()

    st.subheader("🔄 System Workflow")

    st.code(
        "Dataset\n"
        "   ↓\n"
        "Data Cleaning & Preprocessing\n"
        "   ↓\n"
        "Exploratory Data Analysis\n"
        "   ↓\n"
        "Machine Learning Prediction\n"
        "   ↓\n"
        "Capacity Analysis\n"
        "   ↓\n"
        "Appointment Slot Recommendation\n"
        "   ↓\n"
        "Streamlit Dashboard"
    )

    st.success(
        "The system is designed as an academic project "
        "demonstrating how data science and machine learning "
        "can support hospital appointment operations."
    )