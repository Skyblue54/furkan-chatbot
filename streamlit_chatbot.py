import streamlit as st

# ---- Profil Bilgileri ----
bilgiler = {
    "isim": "Furkan Safa Kala",
    "yas": "22",
    "dogum_tarihi": "09.01.2003",
    "dogum_yeri": "Beykoz / İstanbul",
    "universite": "İstanbul Medipol Üniversitesi, Yönetim Bilişim Sistemleri (Mezun)",
    "gpa": "3.41",
    "staj": "DenizBank – 6 ay, Kredi Kartı Satış & Performans Yönetimi",
    "teknik_beceriler": ["Python", "SQL", "Excel", "Power BI", "Algoritmik Trading"],
    "soft_beceriler": ["Analitik düşünme", "Problem çözme", "İletişim", "Planlama", "Takım çalışması"],
    "projeler": ["Data mining projesi: D-7 ülkelerinin ekonomik verilerini analiz ederek ticari banka şubeleri, ATM sayısı, işsizlik oranı ve kişi başına GSYİH üzerine çalışıldı."],
    "tanitim_cumlesi": "Merhaba, ben Furkan Safa Kala. Veri analizi ve finans teknolojileri alanına ilgi duyan, analitik düşünen, çözüm odaklı bir mezunum. Staj deneyimim DenizBank’ta 6 ay boyunca Kredi Kartı Satış ve Performans Yönetimi üzerine çalışmayı içeriyor. Teknik olarak Python, SQL, Excel ve Power BI konularında yetkinim. Profesyonel hedefim veri analizi ve finansal projelerde kendimi geliştirmek."
}

# ---- Streamlit Arayüzü ----
st.set_page_config(page_title="Furkan Kala Chatbot", page_icon="🤖")
st.title("🤖 Furkan Safa Tanıtım Chatbotu")
st.write("Merhaba! Furkan hakkında merak ettiklerini sorabilirsin veya sekmeler üzerinden bilgi alabilirsin.")

# ---- Sekmeler ----
tabs = st.tabs(["Genel Bilgi", "Eğitim & Staj", "Beceriler", "Projeler", "Tanıtım Cümlesi"])

with tabs[0]:
    st.subheader("Genel Bilgi")
    st.write(f"**İsim:** {bilgiler['isim']}")
    st.write(f"**Yaş:** {bilgiler['yas']}")
    st.write(f"**Doğum Tarihi:** {bilgiler['dogum_tarihi']}")
    st.write(f"**Doğum Yeri:** {bilgiler['dogum_yeri']}")

with tabs[1]:
    st.subheader("Eğitim & Staj")
    st.write(f"**Üniversite:** {bilgiler['universite']} (GPA: {bilgiler['gpa']})")
    st.write(f"**Staj:** {bilgiler['staj']}")

with tabs[2]:
    st.subheader("Beceriler")
    st.write("**Teknik Beceriler:**")
    for beceri in bilgiler['teknik_beceriler']:
        st.markdown(f"- {beceri}")
    st.write("**Soft Skills:**")
    for skill in bilgiler['soft_beceriler']:
        st.markdown(f"- {skill}")

with tabs[3]:
    st.subheader("Projeler")
    for proje in bilgiler['projeler']:
        st.markdown(f"- {proje}")

with tabs[4]:
    st.subheader("Tanıtım Cümlesi")
    st.write(bilgiler['tanitim_cumlesi'])

# ---- Chatbot Soru-Cevap ----
st.write("---")
st.subheader("Soru-Cevap Bölümü")
soru = st.text_input("Sorunu yaz:")

if soru:
    s = soru.lower()
    if any(x in s for x in ["isim", "kim"]):
        st.success(bilgiler["isim"])
    elif any(x in s for x in ["yaş", "kaç"]):
        st.success(bilgiler["yas"])
    elif any(x in s for x in ["doğum", "nerede", "tarih"]):
        st.success(f"Doğum tarihi: {bilgiler['dogum_tarihi']}, Doğum yeri: {bilgiler['dogum_yeri']}")
    elif any(x in s for x in ["üniversite", "okul", "mezun"]):
        st.success(f"{bilgiler['universite']} (GPA: {bilgiler['gpa']})")
    elif any(x in s for x in ["staj", "deneyim"]):
        st.success(bilgiler["staj"])
    elif any(x in s for x in ["teknik", "beceri", "yetenek"]):
        st.success(", ".join(bilgiler["teknik_beceriler"]))
    elif any(x in s for x in ["soft", "kişisel", "karakter"]):
        st.success(", ".join(bilgiler["soft_beceriler"]))
    elif any(x in s for x in ["proje", "projeler"]):
        st.success("; ".join(bilgiler["projeler"]))
    elif any(x in s for x in ["tanıtım", "kendini anlat"]):
        st.success(bilgiler["tanitim_cumlesi"])
    else:
        st.warning("Bu konuda Furkan hakkında hazır bir bilgim yok, ancak ekleyebilirsin!")
