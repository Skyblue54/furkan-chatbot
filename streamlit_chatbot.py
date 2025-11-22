import streamlit as st

# ---- Chatbot Bilgileri ----
bilgiler = {
    "isim": "Ben Furkan Kala'nın tanıtım chatbotuyum. Furkan, Yönetim Bilişim Sistemleri 4. sınıf öğrencisi ve bankacılık alanında staj deneyimine sahip.",
    "egitim": "Yönetim Bilişim Sistemleri 4. sınıf öğrencisi. Bilgisayar mühendisliği yüksek lisansı planlıyor.",
    "staj": "Bir bankada kredi kartı satış ve performans yönetimi bölümünde staj yaptı.",
    "beceriler": "Excel, Power BI, SQL, Python, Veri Analizi, Algoritmik Ticaret, TradingView, Matriks Prime.",
    "projeler": "Finansal algoritmik ticaret, veri madenciliği projeleri, teknik analiz tester projeleri.",
    "hedef": "Finans, veri bilimi veya yazılım alanında kariyer hedefliyor."
}

# ---- Streamlit Arayüzü ----
st.set_page_config(page_title="Furkan Kala Chatbot", page_icon="🤖")
st.title("🤖 Furkan Kala Tanıtım Chatbotu")
st.write("Merhaba! Furkan hakkında merak ettiklerini sorabilirsin. Aşağıya bir soru yaz.")

soru = st.text_input("Sorunu yaz:")

if soru:
    s = soru.lower()

    if "kim" in s or "kendini" in s or "tanıt" in s:
        st.success(bilgiler["isim"])
    elif "eğitim" in s:
        st.success(bilgiler["egitim"])
    elif "staj" in s:
        st.success(bilgiler["staj"])
    elif "beceri" in s or "yetenek" in s:
        st.success(bilgiler["beceriler"])
    elif "proje" in s:
        st.success(bilgiler["projeler"])
    elif "hedef" in s:
        st.success(bilgiler["hedef"])
    else:
        st.warning("Bu konuda hazır bir bilgim yok ama istersen ekleyebilirim!")
