#!/usr/bin/env python3
"""
Systems data for HVOF - Source of truth for all system information
"""

systems_data = [
    {
        "id": 1, "name": "3CX", "type": "System", "owner": "Centralt system",
        "department": "Larmcentalen HVOF", "description": "Mjukvarubaserad telefonväxel som tar emot inkommande samtal från tryghetslarm och skickar vidare till ISM",
        "contacts": ["Patrik Wiren", "Sten Möller"], "org": "HVOF",
        "auth": "Användarnamn och lösenord", "category": "Central Systems"
    },
    {
        "id": 2, "name": "Adato", "type": "System", "owner": "Centralt system",
        "department": "Malmö stad", "description": "Dokumentation av rehabärenden",
        "contacts": [], "org": "HVOF/SEF", "auth": "Användarnamn och lösenord",
        "category": "Central Systems"
    },
    {
        "id": 3, "name": "Agera", "type": "System", "owner": "Centralt system",
        "department": "Malmö stad", "description": "Incidentrapportering, olycksfall i arbetet",
        "contacts": [], "org": "", "auth": "Användarnamn och lösenord",
        "category": "Central Systems"
    },
    {
        "id": 4, "name": "Arx passagesystem", "type": "System", "owner": "Centralt system",
        "department": "Malmö stad", "description": "Passagesystem",
        "contacts": ["Omid", "Aleksandar Simic"], "org": "", "auth": "",
        "category": "Central Systems"
    },
    {
        "id": 5, "name": "Avvikelsehanteringssystem/Synpunktssystem", "type": "System",
        "owner": "Selfpoint", "department": "Personal i Malmö stad/Medborgare i Malmö stad",
        "description": "System för personal att skriva avvikelser samt utreda avvikelser. System för medborgare att skriva synpunkter och klagomål.",
        "contacts": ["Jonas Gunnhallsson"], "org": "", "auth": "AD-inloggning",
        "category": "Central Systems"
    },
    {
        "id": 6, "name": "CMP", "type": "System", "owner": "Molntjänst",
        "department": "Larmcentalen HVOF", "description": "Remote administration och inventering av Trygghetslarmen (Neat)",
        "contacts": ["Patrik Wiren"], "org": "HVOF",
        "auth": "Användarnam och lösenord med MS Authenticator", "category": "Cloud Services"
    },
    {
        "id": 7, "name": "Easyapp", "type": "System", "owner": "Molntjänst",
        "department": "HVOF IT", "description": "Inventariesystem",
        "contacts": ["Patrik Wiren"], "org": "HVOF", "auth": "Användarnamn och lösenord",
        "category": "Cloud Services"
    },
    {
        "id": 8, "name": "EcoTech", "type": "System", "owner": "Molntjänst",
        "department": "Larmcentalen HVOF", "description": "Kvalitets och dokumnethanteringssystem (Ledningssystem)",
        "contacts": ["Patrik Wiren"], "org": "HVOF", "auth": "Användarnamn och lösenord",
        "category": "Cloud Services"
    },
    {
        "id": 9, "name": "Ekot (Raindance)", "type": "System", "owner": "Centralt system",
        "department": "Malmö stad", "description": "Ekonomisystem",
        "contacts": [], "org": "", "auth": "Användarnamn och lösenord",
        "category": "Central Systems"
    },
    {
        "id": 10, "name": "Freja eID", "type": "Inloggningsmetod", "owner": "Molntjänst",
        "department": "Malmö stad", "description": "Säker inloggning med LOA 2/3 - SSO (Single Sign-On)",
        "contacts": ["ITD"], "org": "ITD", "auth": "",
        "category": "Services"
    },
    {
        "id": 11, "name": "Guardtools", "type": "System", "owner": "Molntjänst",
        "department": "Larmcentalen HVOF", "description": "Avisering för väktare, larmorder, Avarn",
        "contacts": ["Patrik Wiren"], "org": "", "auth": "Användarnamn och lösenord",
        "category": "Cloud Services"
    },
    {
        "id": 12, "name": "HRutan", "type": "System", "owner": "Centralt system",
        "department": "Malmö stad", "description": "Personalsystem",
        "contacts": [], "org": "", "auth": "Användarnamn och lösenord/ Freja eID",
        "category": "Central Systems"
    },
    {
        "id": 13, "name": "iBinder", "type": "System", "owner": "Molntjänst",
        "department": "Lokalsamordnare HVOF", "description": "Projektleningsverktyg för lokalsamordningen",
        "contacts": [], "org": "", "auth": "Användarnamn och lösenord",
        "category": "Cloud Services"
    },
    {
        "id": 14, "name": "IFacts", "type": "System", "owner": "Centralt system",
        "department": "Malmö stad", "description": "Klassning av IT-system",
        "contacts": [], "org": "", "auth": "Användarnamn och lösenord",
        "category": "Central Systems"
    },
    {
        "id": 15, "name": "Imprivata", "type": "System", "owner": "Malmö stad",
        "department": "", "description": "",
        "contacts": ["ITD", "Jens Klemedsson"], "org": "ITD", "auth": "",
        "category": "Other"
    },
    {
        "id": 16, "name": "Interview (ISM)", "type": "System", "owner": "Centralt system",
        "department": "Larmcentalen HVOF", "description": "Larmmottagningsystem för trygghetslarm, Personlarm och inbrottslarm",
        "contacts": ["Rasmus Svensson", "Sten Möller", "Jonas"], "org": "HVOF/SEF",
        "auth": "Användarnamn och lösenord", "category": "Central Systems"
    },
    {
        "id": 17, "name": "Intunes", "type": "System", "owner": "Centralt system",
        "department": "", "description": "MDM system för mobila enheter Malmö stad",
        "contacts": ["ITD"], "org": "ITD", "auth": "",
        "category": "Central Systems"
    },
    {
        "id": 18, "name": "Keywin nyckelskåp", "type": "System", "owner": "Molntjänst",
        "department": "HVOF", "description": "Admininstration Nyckelskåp Ordbo",
        "contacts": [], "org": "", "auth": "Användarnamn och lösenord",
        "category": "Cloud Services"
    },
    {
        "id": 19, "name": "Koll - Qlikview", "type": "System", "owner": "Centralt system",
        "department": "Malmö stad", "description": "Business intelligence Ekonomi",
        "contacts": [], "org": "", "auth": "Användarnamn och lösenord",
        "category": "Central Systems"
    },
    {
        "id": 20, "name": "KomKat", "type": "System", "owner": "KFSK (Kommunföbundet Skåne)",
        "department": "HVOF, FSF", "description": "Admininstration av HSA katalogen",
        "contacts": ["KFSK"], "org": "KFSK",
        "auth": "SITHS-kort, Freja, personnummer + pin-kod", "category": "Services"
    },
    {
        "id": 21, "name": "Kuben", "type": "System", "owner": "Molntjänst",
        "department": "HSL Personal", "description": "Tidsplanering för vårdbehov av brukare",
        "contacts": ["Gustav Thoresson"], "org": "HVOF",
        "auth": "Microsoft Authenticator + AD konto", "category": "Cloud Services"
    },
    {
        "id": 22, "name": "Lifecare-Procapita", "type": "System", "owner": "Centralt system",
        "department": "HVOF, FSF", "description": "Journal och vårdsystem för HVOF och FSF",
        "contacts": ["ÖSA", "FSF"], "org": "FSF",
        "auth": "Användarnamn och lösenord, Freja eID", "category": "Central Systems"
    },
    {
        "id": 23, "name": "Lime CRM", "type": "System", "owner": "Molntjänst",
        "department": "Larmcentalen HVOF", "description": "Kunddatabas för fastighetsägaren gällande e-lås i portar, avtal m.m.",
        "contacts": ["Patrik Wiren"], "org": "", "auth": "Användarnamn och lösenord",
        "category": "Cloud Services"
    },
    {
        "id": 24, "name": "Lärkan", "type": "System", "owner": "Molntjänst TicTac",
        "department": "Chefer, leg, utförare", "description": "Utbildningsplattform",
        "contacts": ["Berne Forzelius"], "org": "", "auth": "",
        "category": "Cloud Services"
    },
    {
        "id": 25, "name": "Mateo", "type": "System", "owner": "",
        "department": "Måltidsenheten Särskilt boende", "description": "Kostdataprogram för särskilt boende",
        "contacts": ["Alexander Palmér"], "org": "", "auth": "",
        "category": "Cloud Services"
    },
    {
        "id": 26, "name": "MCSS - HVOF", "type": "System", "owner": "Molntjänst",
        "department": "Leg personal/Utförarpersonal",
        "description": "System för digital signering för delegerad personal av läkemedel samt HSL uppgifter",
        "contacts": ["ÖSA", "Kujtim Spahija"], "org": "",
        "auth": "SITHS-kort, Freja, personnummer + pin-kod", "category": "Services"
    },
    {
        "id": 27, "name": "Medvind", "type": "System", "owner": "Centralt system",
        "department": "Malmö stad", "description": "Personalsystem",
        "contacts": ["SEF"], "org": "SEF", "auth": "Användarnamn och lösenord/ Freja eID",
        "category": "Central Systems"
    },
    {
        "id": 28, "name": "Milestone", "type": "System", "owner": "Centralt system",
        "department": "Larmcentalen HVOF", "description": "Kameralarm för bevakning/ Digital tillsyn under natten",
        "contacts": ["Rasmus Svensson", "Sten Möller", "Jonas"], "org": "HVOF/SEF",
        "auth": "Användarnamn och lösenord", "category": "Cloud Services"
    },
    {
        "id": 29, "name": "Mina planer", "type": "System", "owner": "KFSK (Kommunföbundet Skåne)",
        "department": "HVOF, FSF", "description": "Samordnad vårdplanering Regionen",
        "contacts": ["ÖSA", "KFSK"], "org": "KFSK",
        "auth": "SITHS-kort, Freja, personnummer + pin-kod", "category": "Services"
    },
    {
        "id": 30, "name": "Mobilt e-Siths", "type": "Inloggningsmetod", "owner": "",
        "department": "", "description": "Mobil applikation för SITHS-inloggning", "contacts": [], "org": "", "auth": "",
        "category": "Applications"
    },
    {
        "id": 31, "name": "MSM (Marval)", "type": "System", "owner": "Centralt system",
        "department": "Malmö stad", "description": "Ärendehanteringssystem av IT frågor och beställningar för Malmö stad",
        "contacts": ["ITD", "Gökan Memisovski"], "org": "SEF",
        "auth": "Användarnamn och lösenord", "category": "Central Systems"
    },
    {
        "id": 32, "name": "Net ID", "type": "Applikation", "owner": "",
        "department": "", "description": "", "contacts": [], "org": "", "auth": "",
        "category": "Applications"
    },
    {
        "id": 33, "name": "NPÖ", "type": "System", "owner": "Inera",
        "department": "HVOF, FSF", "description": "Nationell patientöversikt",
        "contacts": ["ÖSA", "Inera"], "org": "Inera",
        "auth": "SITHS-kort, Freja, personnummer + pin-kod", "category": "Services"
    },
    {
        "id": 34, "name": "Open e-plattformen", "type": "System", "owner": "Centralt system",
        "department": "Malmö stad", "description": "E-tjänsteplattform för Malmö stad",
        "contacts": ["ITD"], "org": "", "auth": "",
        "category": "Central Systems"
    },
    {
        "id": 35, "name": "Optinet", "type": "System", "owner": "Molntjänst",
        "department": "Larmcentalen HVOF", "description": "Årendehantering och bokningssystem LC Tekniker",
        "contacts": ["Patrik Wiren"], "org": "HVOF", "auth": "Användarnamn och lösenord",
        "category": "Cloud Services"
    },
    {
        "id": 36, "name": "Pascal", "type": "System", "owner": "Inera",
        "department": "HVOF, FSF", "description": "Beställning av läkemedel, Översikt av dosexpedierade läkemedel",
        "contacts": ["ÖSA", "Inera"], "org": "Inera",
        "auth": "SITHS-kort, Freja, personnummer + pin-kod", "category": "Services"
    },
    {
        "id": 37, "name": "Phoniro Care", "type": "System", "owner": "Centralt system",
        "department": "HVOF", "description": "Tid och insatsuppföljning av Lifecare, LMO",
        "contacts": ["ÖSA", "FSF"], "org": "FSF", "auth": "Användarnamn och lösenord",
        "category": "Central Systems"
    },
    {
        "id": 38, "name": "Phoniro Lock systems/Phoniro PI - digitala lås", "type": "System",
        "owner": "Malmö stad", "department": "Omvårdnadspersonal Ordbo",
        "description": "E-lås för brukare inom hemtjänsten HVOF",
        "contacts": ["Larmcentralen", "Patrik Wiren"], "org": "FSF",
        "auth": "Freja eID via LMO appen, Säker delad mobil", "category": "Services"
    },
    {
        "id": 39, "name": "Platina", "type": "System", "owner": "Centralt system",
        "department": "Malmö stad", "description": "Dokument och ärendehantering av Nämndsfrågor",
        "contacts": [], "org": "", "auth": "",
        "category": "Central Systems"
    },
    {
        "id": 40, "name": "RCO", "type": "System", "owner": "Malmö stad",
        "department": "", "description": "Passagesystem",
        "contacts": ["Aleksandar Simic"], "org": "SEF", "auth": "Användarnamn och lösenord",
        "category": "Central Systems"
    },
    {
        "id": 41, "name": "Securecloud", "type": "System", "owner": "Molntjänst (Securia",
        "department": "Larmcentalen HVOF", "description": "",
        "contacts": ["Larmcentralen", "Rasmus Svensson", "Sten Möller", "Jonas"],
        "org": "", "auth": "", "category": "Cloud Services"
    },
    {
        "id": 42, "name": "Senior alert", "type": "System", "owner": "Region Jönköping",
        "department": "HVOF", "description": "Nationellt kvalitetsregister för att stödja vårdprevention",
        "contacts": ["Region Jönköping"], "org": "", "auth": "",
        "category": "Cloud Services"
    },
    {
        "id": 43, "name": "SITHS admin", "type": "Inloggningsmetod", "owner": "",
        "department": "", "description": "Administrationsverktyg för SITHS-kort (Säker IT i Hälso- och Sjukvården)", "contacts": [], "org": "", "auth": "",
        "category": "Applications"
    },
    {
        "id": 44, "name": "Snipe-IT", "type": "System", "owner": "Centralt system",
        "department": "HVOF IT", "description": "Inventariesystem flr HVOF IT",
        "contacts": ["Madelaine Fredriksson"], "org": "", "auth": "Användarnamn och lösenord",
        "category": "Central Systems"
    },
    {
        "id": 45, "name": "Solicard", "type": "System", "owner": "Centralt system",
        "department": "", "description": "Passagesystem",
        "contacts": ["Omid", "Aleksandar Simic"], "org": "", "auth": "",
        "category": "Central Systems"
    },
    {
        "id": 46, "name": "Stanley Unizon", "type": "System", "owner": "Centralt system",
        "department": "Malmö stad", "description": "Passagesystem",
        "contacts": ["Omid", "Aleksandar Simic"], "org": "", "auth": "",
        "category": "Central Systems"
    },
    {
        "id": 47, "name": "Stratsys", "type": "System", "owner": "Centralt system",
        "department": "Malmö stad", "description": "Rapportverktyg, Statisitk Ekonomi",
        "contacts": [], "org": "", "auth": "Användarnamn och lösenord",
        "category": "Central Systems"
    },
    {
        "id": 48, "name": "Traka HVOF", "type": "System", "owner": "Centralt system",
        "department": "HVOF", "description": "Admininstration Nyckelskåp Ordbo Traka web",
        "contacts": ["Thang Trinh"], "org": "", "auth": "Användarnamn och lösenord",
        "category": "Other"
    },
    {
        "id": 49, "name": "Vikariebanken", "type": "System", "owner": "Centralt system",
        "department": "Malmö stad", "description": "Hantering av timvikarier",
        "contacts": ["SEF"], "org": "", "auth": "Användarnamn och lösenord",
        "category": "Central Systems"
    },
    {
        "id": 50, "name": "Viser", "type": "System", "owner": "Sensiocare/Viser",
        "department": "Säbo", "description": "Larmsystem säbo",
        "contacts": ["SensioCare", "Säbo", "Jens Klemedsson"], "org": "HVOF",
        "auth": "Användarnamn och lösenord", "category": "Other"
    },
    {
        "id": 51, "name": "Visma", "type": "System", "owner": "Centralt system",
        "department": "Malmö stad", "description": "Rekryteringsverktyg för HR",
        "contacts": ["SEF"], "org": "", "auth": "Användarnamn och lösenord",
        "category": "Central Systems"
    },
    {
        "id": 52, "name": "Webb SESAM", "type": "System", "owner": "Centralt system",
        "department": "FSF, HVOF", "description": "Admininstration av Hjälpmedel till brukare",
        "contacts": [], "org": "", "auth": "",
        "category": "Central Systems"
    },
    {
        "id": 53, "name": "Sensio trygghetssensorer", "type": "System", "owner": "Molntjänst (Sensio)",
        "department": "Säbo", "description": "Trygghetssensorer som installeras i brukarnas lägenheter. Sensorer skickar larm till medarbetarnas mobiltelefoner om förutbestämda händelser sker. Larmen hanteras via Sensios uppsättning av Skyresponse.",
        "contacts": ["Ubejd Shala", "Johan Lindgren"], "org": "",
        "auth": "", "category": "Cloud Services"
    },
    {
        "id": 54, "name": "Smooth lite trygghetssensorer", "type": "System", "owner": "Molntjänst (Great security)",
        "department": "Säbo", "description": "Trygghetssensorer som installeras i brukarnas lägenheter. Sensorer skickar larm till medarbetarnas mobiltelefoner om förutbestämda händelser sker.",
        "contacts": ["Ubejd Shala", "Daniel Svensson"], "org": "", "auth": "",
        "category": "Cloud Services"
    },
    {
        "id": 55, "name": "Maskeringstjänsten", "type": "Tjänst", "owner": "Atea",
        "department": "Myndighet", "description": "AI-tjänst som identifierar och maskerar personuppgifter i allmänna handlingar inför utlämning.",
        "contacts": [], "org": "", "auth": "",
        "category": "Services"
    },
    {
        "id": 56, "name": "Miro", "type": "", "owner": "", "department": "",
        "description": "", "contacts": [], "org": "", "auth": "",
        "category": "Services"
    },
    {
        "id": 57, "name": "Chat-gpt", "type": "", "owner": "", "department": "",
        "description": "", "contacts": [], "org": "", "auth": "",
        "category": "Services"
    }
]

