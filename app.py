# Import Library
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# Mengatur konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Portfolio Jessica Agnesia Tataung",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dekorator untuk meng-cache data dan tidak memuatnya ulang setiap kali
@st.cache_data
def generate_dashboard_data():
    # Membuat range tanggal dari 1 Januari 2024 selama 30 hari
    dates = pd.date_range('2024-01-01', periods=30)

    # Mengembalikan DataFrame dengan kolom Date, Sales, Visitors, dan Conversion
    return pd.DataFrame({
        # Kolom tanggal
        'Date': dates,

        # Kolom penjualan dengan nilai random antara 1000-5000
        'Sales': np.random.randint(1000, 5000, 30),

        # Kolom pengunjung dengan nilai random antara 500-3000
        'Visitors': np.random.randint(500, 3000, 30),

        # Kolom konversi dengan nilai random antara 0.01-0.1
        'Conversion': np.random.uniform(0.01, 0.1, 30)
    })

# Test: Lihat hasil data yang dihasilkan
dashboard_data = generate_dashboard_data()
dashboard_data.head()

# Dekorator untuk meng-cache data skills
@st.cache_data
def get_skills_data():
    return pd.DataFrame({
        'Skill': ['Python', 'SQL', 'Tableau', 'PowerBI', 'Excel', 'Statistics'],
        'Proficiency': [90, 92, 90, 95, 90, 85]
    })

# Dekorator untuk meng-cache data proyek
@st.cache_data
# Fungsi untuk mengembalikan data proyek dengan kemampuan filter
def get_projects_data():
    # Membuat list berisi data-data proyek
    projects = [
        # Proyek pertama: E-commerce Sales Analysis
        {
            # Judul proyek dengan emoji
            'title': '📊 Proyek 1: E-commerce Sales Analysis',
            # Kategori proyek
            'category': 'EDA',
            # Tahun proyek dibuat
            'year': 2025,
            # Deskripsi detail tentang proyek
            'description': '''**Deskripsi:**
This project focuses on performing an **Exploratory Data Analysis (EDA)** on an E-commerce sales dataset
to understand sales patterns, customer behavior, and business performance over time.
The analysis aims to identify meaningful trends, key drivers of revenue, and potential
opportunities for business improvement.

The project covers data cleaning, descriptive analysis, and visual exploration
to support data-driven decision making.

**Tools:** Python, Pandas, Matplotlib, Streamlit

**Key Insights:**
- Overall sales show an **upward trend**, indicating positive business growth over time.
- The **Electronics category** consistently contributes the highest revenue compared to other categories.
- Sales performance is **stronger during specific periods**, suggesting seasonality effects.
- Higher customer activity is generally associated with **increased sales volume**, although not always linearly.
- Certain product categories demonstrate **high sales volume but lower profitability**, highlighting optimization opportunities.''',
            # Flag apakah proyek memiliki gambar atau tidak
            'has_image': False,
            'url' : 'https://github.com/Jessicaagnesiat/Exploratory-data-analysis-on-E-commerce-sales/blob/main/Assignment_Advanced_EDA_Jessica_Agnesia_Tataung.ipynb'
        },
        # Proyek kedua: Customer Segmentation Dashboard
        {
            # Judul proyek dengan emoji
            'title': '📈 Proyek 2: Customer Segmentation Dashboard',
            # Kategori proyek
            'category': 'Dashboard',
            # Tahun proyek dibuat
            'year': 2025,
            # Deskripsi detail tentang proyek
            'description': '''**Deskripsi:**
This project performs an **E-Commerce Customer Segmentation Analysis** using RFM (Recency, Frequency, Monetary) modeling 
and dashboard visualization to understand customer purchasing behavior and profitability.

The analysis begins with data cleaning and preprocessing using Python, followed by RFM feature creation to score customers 
based on how recently they purchased, how often they purchased, and how much they spent. A segmentation scheme is then 
developed that categorizes customers into meaningful groups.

The results are visualized in an **interactive Power BI dashboard**, enabling stakeholders to explore segment traits, 
product performance, regional trends, and profitability drivers.

**Tools:** SQL, Tableau, Python, streamlit

**Key Insights:**
- **Loyal Customers (37.9%)** and **Champions (19.3%)** are the most valuable and active segments, generating significant revenue.  
- The **Technology product category** leads in both revenue and profit among segments.  
- **Profitability tends to decrease** as **shipping costs increase**, particularly above certain thresholds.  
- **Discounts continue to be effective** in driving purchases for top segments.  
- Targeted strategies can improve retention and growth for **at-risk** and **hibernating** segments.''',
            # Flag apakah proyek memiliki gambar atau tidak
            'has_image': False
        },
        # Proyek ketiga: Churn Prediction Model
#        {
            # Judul proyek dengan emoji
 #           'title': '🤖 Proyek 3: Churn Prediction Model',
            # Kategori proyek
  #          'category': 'Prediction',
            # Tahun proyek dibuat
   #         'year': 2025,
            # Deskripsi detail tentang proyek
#            'description': '''**Deskripsi:**
#Machine learning model untuk memprediksi customer churn dengan akurasi 85%.

#**Tools:** Python, Scikit-learn, XGBoost

#**Performance:**
#- Accuracy: 85%
#- Precision: 0.82
#- Recall: 0.88''',
            # Flag apakah proyek memiliki gambar atau tidak
      #      'has_image': False
       # }
    ]

    # Mengkonversi list projects menjadi DataFrame dan mengembalikannya
    return pd.DataFrame(projects)

# Fungsi untuk menampilkan garis pemisah
def render_divider():
    # Menampilkan garis horizontal sebagai pemisah
    st.markdown("---")
    # Menampilkan pemisah di sidebar

# Fungsi untuk menampilkan navigasi di sidebar
def render_sidebar_nav():
    # Menampilkan judul navigasi di sidebar
    #st.sidebar.markdown("# 📍 Navigasi")
    st.sidebar.markdown("---")
    # Membuat tombol radio untuk memilih halaman
    st.sidebar.markdown(
    """
        ### Page:
    """)
    page = st.sidebar.radio(
        # Label untuk radio button
        " Pilih halaman:",
        # Opsi halaman yang tersedia
        ["🏠 Home", "👤 About", "📁 Project", "📊 Dashboard", "📧 Contact"]
    )

    # Menampilkan pemisah di sidebar
    st.sidebar.markdown("---")

    # Menampilkan tautan media sosial di sidebar
    st.sidebar.markdown(
        """
        ### 🔗 Media Sosial
        - [LinkedIn](https://linkedin.com/in/jessicaagnesiat)
        - [GitHub](https://github.com/Jessicaagnesiat)
        - [Email](mailto:jessicaagnesiat@gmail.com)
        """
    )

    # Menampilkan pemisah lagi di sidebar
    st.sidebar.markdown("---")

    # Menampilkan caption/teks kecil di sidebar
    st.sidebar.caption("© 2025 Portfolio Saya")

    # Mengembalikan halaman yang dipilih user
    return page

# Fungsi untuk menampilkan foto profil
def render_profile_image():
    # Mencoba untuk menampilkan foto profil
    try:
        # Menampilkan gambar dari file
        st.image(
            # Path ke file gambar profil
            "assets/profile_pic.jpg",
            # Caption yang ditampilkan di bawah gambar
            caption="Profile Picture",
            # Mengatur gambar menggunakan lebar container penuh
            use_container_width=True
        )
    # Jika file tidak ditemukan
    except FileNotFoundError:
        # Menampilkan pesan warning
        st.warning("⚠️ File 'assets/profpict.png' tidak ditemukan!")
        # Menampilkan pesan info/petunjuk
        st.info("💡 Buat folder 'assets/' dan masukkan foto Anda di sana.")

# Fungsi untuk menampilkan halaman Home
def page_home():
    # Membuat 2 kolom dengan rasio 2:1
    col1, col2 = st.columns([2, 1])

    # Menggunakan kolom pertama
    with col1:
        # Menampilkan judul besar dengan emoji
        st.title("Hi, I'm Jessica!")

        # Menampilkan teks markdown dengan pengenalan diri
        st.markdown(
            """
            A Pharmacy graduate transitioning into **Data Science**, supported by a strong analytical and research foundation. 

            Skilled in **Python** (Pandas, NumPy, scikit-learn) and **SQL**, with hands-on experience in data cleaning, visualization, and machine learning.

            Passionate about transforming data into actionable insights and developing data driven solutions that support real world decision making across various business domains
            """
        )

        # Menampilkan ruang kosong untuk spacing
        st.write(" ")

        # Membuat 2 kolom untuk tombol
        col_btn1, col_btn2 = st.columns(2)

        # Menggunakan kolom pertama untuk tombol download CV
        with col_btn1:
            with open("assets/CV Jessica Agnesia Tataung.pdf", "rb") as file:
                downloaded = st.download_button(
                    label="📄 Download CV",
                    data=file,
                    file_name="CV Jessica Agnesia Tataung.pdf",
                    mime="application/pdf"
                )
            if downloaded:
                st.success("✅ CV sudah ter-download")

        # Menggunakan kolom kedua untuk tombol hubungi
        with col_btn2:
            # Membuat tombol hubungi saya
            if st.button("💬 Hubungi Saya"):
                # Menampilkan pesan info ketika tombol ditekan
                st.info("Silakan scroll ke halaman Contact!")

    # Menggunakan kolom kedua untuk foto profil
    with col2:
        # Memanggil fungsi untuk menampilkan foto profil
        render_profile_image()

    # Menampilkan garis pemisah
    render_divider()

    # Menampilkan statistik singkat
    st.subheader("📈 Statistik Singkat")

    # Membuat 4 kolom untuk menampilkan metrik
    col1, col2, col3, col4 = st.columns(4)

    # Menampilkan metrik proyek selesai
    col1.metric("Proyek Selesai", 10, "+2")

    # Menampilkan metrik total dataset
    col2.metric("Total Dataset", 20, "-1")

    # Menampilkan metrik jumlah klien
    col3.metric("Clients", 3, "+2")

    # Menampilkan metrik tahun pengalaman
    col4.metric("Tahun Pengalaman", 1, "+1")

# Fungsi untuk menampilkan halaman About
def page_about():
    # Menampilkan judul halaman dengan emoji
    st.title("👤 About")

    # Menampilkan subheader untuk latar belakang
    st.subheader("Latar Belakang")

    # Menampilkan teks tentang latar belakang dan keahlian
    st.write(
        """
        **Fokus Keahlian:**
        - **Data Exploration & Cleaning**: Pandas, NumPy  
        - **Data Visualization**: Tableau, Power BI, Streamlit  
        - **Statistical Analysis**: A/B Testing (basic), Hypothesis Testing  
        - **Business Intelligence**: Dashboard development, KPI monitoring
        """
    )

    # Menampilkan subheader untuk technical skills
    st.subheader("🛠️ Technical Skills")

    # Memanggil fungsi untuk mendapatkan data skills dan menyimpannya dalam variable
    skills_data = get_skills_data()

    # Membuat bar chart menggunakan Plotly Express
    fig = px.bar(
        # Data yang digunakan untuk chart
        skills_data,
        # Kolom yang ditampilkan di x-axis
        x='Skill',
        # Kolom yang ditampilkan di y-axis
        y='Proficiency',
        # Judul chart
        title='Tingkat Keahlian',
        # Kolom yang digunakan untuk warna
        color='Proficiency',
        # Skala warna yang digunakan
        color_continuous_scale='Viridis',
        # Menampilkan nilai di atas bar
        text='Proficiency'
    )

    # Menampilkan chart di Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Menampilkan subheader untuk sertifikasi
   # st.subheader("📚 Sertifikasi")

    # Membuat 3 kolom untuk menampilkan sertifikasi
    #cert_col1, cert_col2, cert_col3 = st.columns(3)

    #cert_col1.markdown(
     #   """
      ## ✅ Certified, 2022
        #"""
    #)

    # Menampilkan sertifikasi SQL di kolom kedua
    #cert_col2.markdown(
     #   """
      #  **SQL for Data Analysis**
       # ✅ Certified, 2021
       # """
    #)

    # Menampilkan sertifikasi Tableau di kolom ketiga
    #cert_col3.markdown(
     #   """
     #   **Data Visualization with Tableau**
      #  ✅ Certified, 2023
       # """
    #)

# asumsi: fungsi-fungsi ini tersedia di tempat lain dalam project
# from your_module import render_divider, get_projects_data

def page_project():
    # Menampilkan judul halaman dengan emoji
    st.title("📁 Project")

    # Menampilkan subheader untuk filter proyek
    st.subheader("🔍 Filter Project")

    # Membuat 2 kolom untuk filter
    col1, col2 = st.columns(2)

    # Menggunakan kolom pertama untuk filter kategori
    with col1:
        selected_category = st.multiselect(
            "Kategori:",
            ['EDA', 'Dashboard', 'Prediction', 'Visualization'],
            default=['EDA', 'Dashboard', 'Prediction']
        )

    # Menggunakan kolom kedua untuk filter tahun
    with col2:
        selected_year = st.slider(
            "Tahun:",
            2025,
            2026,
            (2025, 2026)
        )

    # Menampilkan garis pemisah (pastikan render_divider() didefinisikan)
    render_divider()

    # Memanggil fungsi untuk mendapatkan data proyek (harus mengembalikan pandas.DataFrame)
    projects_df = get_projects_data()

    # Pastikan selected_year adalah tuple (jika user mengkonfigurasi slider sebagai single value)
    if isinstance(selected_year, int):
        year_min, year_max = selected_year, selected_year
    else:
        year_min, year_max = selected_year

    # Melakukan filter pada data proyek berdasarkan kategori dan tahun yang dipilih
    filtered_projects = projects_df[
        (projects_df['category'].isin(selected_category)) &
        (projects_df['year'] >= year_min) &
        (projects_df['year'] <= year_max)
    ]

    # Mengecek apakah ada proyek yang sesuai dengan filter
    if filtered_projects.empty:
        st.info("📭 Tidak ada proyek yang sesuai dengan filter Anda")
        return

    # Loop untuk menampilkan setiap proyek yang telah difilter
    # Gunakan enumerate untuk membuat key tombol unik (agar tidak bentrok jika index DataFrame bukan 0..n-1)
    for i, (_, project) in enumerate(filtered_projects.iterrows()):
        # Membuat expander untuk setiap proyek (dapat diklik untuk membuka/menutup)
        with st.expander(f"{project.get('title', 'Untitled')} ({project.get('year', '')})", expanded=(i == 0)):
            # Membuat 2 kolom jika proyek memiliki gambar, jika tidak membuat 1 kolom (container)
            if project.get('has_image', False):
                col_left, col_right = st.columns([2, 1])
            else:
                col_left = st.container()
                col_right = None

            # Menggunakan kolom pertama untuk deskripsi
            with col_left:
                st.markdown(project.get('description', ''))

                # Jika ada URL proyek, gunakan itu; kalau tidak, hanya tampilkan tombol info
                proj_url = project.get('url', None)
                if proj_url:
                    # Tombol untuk membuka link di tab baru: gunakan markdown link (Streamlit akan membuka di tab baru)
                    if st.button("🔗 View Project", key=f"project_{i}"):
                        st.write(f"[Membuka project]({proj_url})")
                else:
                    if st.button("🔗 View Project", key=f"project_{i}"):
                        st.info(f"Link ke project {project.get('title', '')} akan dibuka!")

            # Mengecek apakah kolom kedua ada dan proyek memiliki gambar
            if col_right is not None and project.get('has_image', False):
                with col_right:
                    img_path = project.get('image_path', 'assets/project1_ss.png')
                    # Resolve path relative ke working directory jika bukan absolute
                    img_path = Path(img_path)
                    if not img_path.is_absolute():
                        img_path = Path.cwd() / img_path
                    if img_path.exists():
                        st.image(str(img_path), caption="Project Screenshot")
                    else:
                        st.info("📷 Screenshot tidak tersedia")

# Fungsi untuk menampilkan halaman dashboard
def page_dashboard():
    # Menampilkan judul halaman dengan emoji
    st.title("📊 Interactive Dashboard")

    # Memanggil fungsi untuk mendapatkan data dashboard yang sudah di-cache
    dashboard_data = generate_dashboard_data()

    # Menampilkan subheader untuk KPI metrics
    st.subheader("📌 KPI Metrics")

    # Membuat 4 kolom untuk menampilkan KPI
    col1, col2, col3, col4 = st.columns(4)

    # Menghitung total penjualan dengan menjumlahkan kolom Sales
    total_sales = dashboard_data['Sales'].sum()

    # Menghitung total pengunjung dengan menjumlahkan kolom Visitors
    total_visitors = dashboard_data['Visitors'].sum()

    # Menghitung rata-rata konversi dengan merata-rata kolom Conversion
    avg_conversion = dashboard_data['Conversion'].mean()

    # Menghitung rata-rata nilai order dengan merata-rata kolom Sales
    avg_order_value = dashboard_data['Sales'].mean()

    # Menampilkan metric total penjualan di kolom pertama
    col1.metric("Total Sales", f"Rp {total_sales:,.0f}", "+15%")

    # Menampilkan metric total pengunjung di kolom kedua
    col2.metric("Total Visitors", f"{total_visitors:,}", "+12%")

    # Menampilkan metric rata-rata konversi di kolom ketiga
    col3.metric("Avg Conversion", f"{avg_conversion:.2%}", "+8%")

    # Menampilkan metric rata-rata nilai order di kolom keempat
    col4.metric("Avg Order Value", f"Rp {avg_order_value:,.0f}", "-3%")

    # Menampilkan garis pemisah
    render_divider()

    # Menampilkan subheader untuk sales trend
    st.subheader("📈 Sales Trend")

    # Membuat line chart untuk menampilkan tren penjualan harian
    fig1 = px.line(
        # Data yang digunakan untuk chart
        dashboard_data,
        # Kolom yang ditampilkan di x-axis
        x='Date',
        # Kolom yang ditampilkan di y-axis
        y='Sales',
        # Judul chart
        title='Daily Sales',
        # Menampilkan marker pada setiap data point
        markers=True
    )

    # Menampilkan chart di Streamlit
    st.plotly_chart(fig1, use_container_width=True)

    # Membuat 2 kolom untuk menampilkan 2 chart sekaligus
    col1, col2 = st.columns(2)

    # Menggunakan kolom pertama untuk chart pengunjung harian
    with col1:
        # Membuat bar chart untuk menampilkan pengunjung harian
        fig2 = px.bar(
            # Mengelompokkan data berdasarkan tanggal dan menjumlahkan nilai numerik
            dashboard_data.groupby('Date').sum(numeric_only=True).reset_index(),
            # Kolom yang ditampilkan di x-axis
            x='Date',
            # Kolom yang ditampilkan di y-axis
            y='Visitors',
            # Judul chart
            title='Daily Visitors'
        )

        # Menampilkan chart di Streamlit
        st.plotly_chart(fig2, use_container_width=True)

    # Menggunakan kolom kedua untuk scatter plot
    with col2:
        # Membuat scatter plot untuk menampilkan hubungan antara pengunjung dan penjualan
        fig3 = px.scatter(
            # Data yang digunakan untuk chart
            dashboard_data,
            # Kolom yang ditampilkan di x-axis
            x='Visitors',
            # Kolom yang ditampilkan di y-axis
            y='Sales',
            # Kolom yang digunakan untuk ukuran bubble
            size='Conversion',
            # Judul chart
            title='Visitors vs Sales',
            # Kolom yang digunakan untuk warna
            color='Conversion',
            # Skala warna yang digunakan
            color_continuous_scale='Viridis'
        )

        # Menampilkan chart di Streamlit
        st.plotly_chart(fig3, use_container_width=True)

import re
from typing import Optional

import streamlit as st

# Optional: provide a simple divider if render_divider isn't defined elsewhere
if "render_divider" not in globals():
    def render_divider():
        st.markdown("---")


def _is_valid_email(email: str) -> bool:
    """Very small email validity check (sufficient for simple form validation)."""
    if not email:
        return False
    # basic pattern: something@something.something
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email) is not None


# Fungsi untuk menampilkan halaman contact
def page_contact() -> None:
    # Menampilkan judul halaman dengan emoji
    st.title("📧 Get in Touch")

    # Menampilkan teks penjelasan
    st.write(
        "Jika Anda tertarik untuk berkolaborasi atau memiliki pertanyaan, "
        "silakan hubungi saya melalui form di bawah!"
    )

    # Menampilkan garis pemisah
    render_divider()

    # Membuat form untuk contact
    with st.form("contact_form"):
        # Membuat input text untuk nama lengkap
        nama = st.text_input("Nama Lengkap")

        # Membuat input text untuk email
        email = st.text_input("Email")

        # Membuat selectbox untuk subjek
        subject = st.selectbox(
            "Subjek:",
            ['Project Inquiry', 'Collaboration', 'General Question', 'Others']
        )

        # Membuat text area untuk pesan dengan tinggi 150 pixel
        message = st.text_area("Pesan:", height=150)

        # Membuat tombol submit untuk mengirim form
        submitted = st.form_submit_button("📤 Send Message")

        # Mengecek apakah form telah disubmit
        if submitted:
            # Validasi sederhana
            if not nama or not email or not message:
                st.error("❌ Mohon isi semua field!")
            elif not _is_valid_email(email):
                st.error("❌ Format email tidak valid. Contoh: nama@domain.com")
            else:
                # Menampilkan pesan sukses dengan nama user
                st.success(
                    f"✅ Terima kasih, {nama}! Pesan Anda telah dikirim. "
                    "Saya akan menghubungi Anda dalam 24 jam."
                )
                # (Opsional) tampilkan ringkasan
                st.markdown("**Rincian pesan:**")
                st.write(f"- Email: {email}")
                st.write(f"- Subject: {subject}")
                st.write(f"- Pesan: {message}")

    # Menampilkan garis pemisah
    render_divider()

    # Menampilkan subheader untuk kontak lainnya
    st.subheader("🔗 Kontak Lainnya")

    # Membuat 3 kolom untuk menampilkan kontak lainnya
    col1, col2, col3 = st.columns(3)

    # Menampilkan kontak email di kolom pertama
    col1.markdown(
        """
        **Email**
        📧 [jessicaagnesiat@gmail.com](mailto:jessicaagnesiat@gmail.com)
        """
    )

    # Menampilkan kontak LinkedIn di kolom kedua
    col2.markdown(
        """
        **LinkedIn**
        💼 [linkedin.com/in/jessicaagnesiat](https://linkedin.com/in/jessicaagnesiat)
        """
    )

    # Menampilkan kontak GitHub di kolom ketiga
    col3.markdown(
        """
        **GitHub**
        🐙 [github.com/jessicaagnesiat](https://github.com/Jessicaagnesiat)
        """
    )

import streamlit as st
from typing import Callable, Dict

# Attempt to import page functions; if they are defined in other modules,
# adjust the import paths accordingly.
try:
    from pages import page_home, page_tentang_saya, page_project, page_dashboard, page_contact  # type: ignore
except Exception:
    # If the pages are defined in the same module, the above import will fail;
    # fall back to attributes in the current module (caller should define them).
    page_home = globals().get("page_home")
    page_about = globals().get("page_about")
    page_project = globals().get("page_project")
    page_dashboard = globals().get("page_dashboard")
    page_contact = globals().get("page_contact")


def _missing_page(name: str) -> Callable[[], None]:
    """Return a function that shows an error for missing pages."""
    def _show_missing():
        st.error(f"Halaman '{name}' belum diimplementasikan atau tidak dapat diimpor.")
    return _show_missing


def main() -> None:
    # Optional: configure the Streamlit page (adjust as needed)
    st.set_page_config(page_title="Portfolio Jessica Agnesia Tataung", layout="wide")

    # Build mapping from sidebar labels to page callables.
    pages: Dict[str, Callable[[], None]] = {
        "🏠 Home": page_home or _missing_page("🏠 Home"),
        "👤 About": page_about or _missing_page("👤 About"),
        "📁 Project": page_project or _missing_page("📁 Project"),
        "📊 Dashboard": page_dashboard or _missing_page("📊 Dashboard"),
        "📧 Contact": page_contact or _missing_page("📧 Contact"),
    }

    # Render the sidebar navigation. This function should return one of the keys above.
    # If render_sidebar_nav is defined elsewhere, call it; otherwise show a simple selectbox.
    renderer = globals().get("render_sidebar_nav")
    if callable(renderer):
        try:
            selected_page = renderer()
        except Exception as e:
            st.error(f"Terjadi error saat merender sidebar: {e}")
            selected_page = None
    else:
        # Fallback: simple selectbox in sidebar
        selected_page = st.sidebar.selectbox("Navigate to", list(pages.keys()))

    # If the renderer returned None or an unexpected value, default to the first page.
    if not selected_page or selected_page not in pages:
        selected_page = list(pages.keys())[0]

    # Call the page function
    page_func = pages[selected_page]
    try:
        page_func()
    except Exception as e:
        st.exception(e)


if __name__ == "__main__":
    main()
    