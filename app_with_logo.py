import streamlit as st
from rapidfuzz import process

# ------------------------------
# Logo ve başlık
# ------------------------------
st.image("sap_ai_logo.png", width=150)
st.title("🛠️ SAP & ERP Issue Solver AI")
st.markdown("Welcome! Try it in English or Deutsch and get solutions for common SAP issues.")

# ------------------------------
# Dil seçimi
# ------------------------------
language = st.selectbox("Select Language / Sprache wählen:", ["English", "Deutsch"])

# ------------------------------
# İngilizce sorun ve çözümler
# ------------------------------
sap_solutions_en = {
    "material issue": "Check material master and warehouse settings, update stock if necessary.",
    "purchase order not approved": "Check the PO approval workflow and user authorizations.",
    "material not visible in stock": "Verify material master and storage location setup, update stock records.",
    "material issue cannot be issued": "Check stock availability and movement type, resolve blocked or missing stock.",
    "invoice does not match goods receipt": "Compare GR and invoice quantity, check SAP records.",
    "user authorization missing": "Check and assign missing roles/authorizations in SU01 and PFCG.",
    "mrp not working": "Review material master and planning parameters, check MRP profiles.",
    "material price incorrect": "Check pricing conditions and vendor master data."
}

# ------------------------------
# Almanca sorun ve çözümler
# ------------------------------
sap_solutions_de = {
    "materialausgang kann nicht durchgeführt werden": "Überprüfen Sie Lagerbestand und Lagerort, prüfen Sie den richtigen Bewegungstyp, beheben Sie fehlende oder gesperrte Bestände.",
    "bestellauftrag wird nicht genehmigt": "Überprüfen Sie den Genehmigungsworkflow und die Benutzerrechte für den Bestellauftrag.",
    "material ist nicht im bestand sichtbar": "Überprüfen Sie das Materialstamm- und Lagerort-Setup, aktualisieren Sie die Bestandsdaten.",
    "material kann nicht ausgegeben werden": "Überprüfen Sie die Lagerbestände und den Bewegungstyp, beheben Sie gesperrte oder fehlende Bestände.",
    "rechnung stimmt nicht mit wareneingang überein": "Vergleichen Sie die GR- und Rechnungsmenge, überprüfen Sie SAP-Einträge.",
    "benutzerberechtigung fehlt": "Überprüfen Sie die fehlenden Rollen/Berechtigungen in SU01 und PFCG und weisen Sie sie zu.",
    "mrp funktioniert nicht": "Überprüfen Sie Materialstamm und Planungsparameter, prüfen Sie MRP-Profile.",
    "materialpreis ist falsch": "Überprüfen Sie Preisbedingungen und Lieferantenstammdaten."
}

# ------------------------------
# Mevcut sorun listesini al
# ------------------------------
if language == "English":
    issues_list = list(sap_solutions_en.keys())
else:
    issues_list = list(sap_solutions_de.keys())

# ------------------------------
# Kullanıcı inputu: öneri listesi ile
# ------------------------------
user_issue = st.selectbox("Enter your issue / Problem eingeben:", [""] + issues_list)

# ------------------------------
# Çözümü göster
# ------------------------------
if st.button("Show Solution / Lösung anzeigen") and user_issue:
    if language == "English":
        match, score, _ = process.extractOne(user_issue.lower(), sap_solutions_en.keys())
        solution = sap_solutions_en[match] if score > 60 else "This issue is not in the list, check general solution logic."
    else:
        match, score, _ = process.extractOne(user_issue.lower(), sap_solutions_de.keys())
        solution = sap_solutions_de[match] if score > 60 else "Dieses Problem ist nicht in der Liste, überprüfen Sie die allgemeine Lösungslogik."
    st.write("Solution / Lösung:", solution)
