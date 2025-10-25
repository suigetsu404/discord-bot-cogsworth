[🇬🇧 English version](./README.md) | [🇵🇱 Wersja polska](./README_PL.md)
***
# Cogsworth - Wielozadaniowy Bot Discord

Cogsworth to wielozadaniowy bot na Discorda napisany w Pythonie przy użyciu biblioteki `discord.py`. Bot integruje się z zewnętrznymi API oraz zarządza serwerem, moderacją i trwałymi danymi użytkowników przy użyciu SQLite.

Projekt ten został zbudowany modułowo z użyciem systemu "Cogs", aby zapewnić czystość i skalowalność kodu.

---

## 🤖 Integracja z AI i API

* `?ask [pytanie]`
    * Bezpośrednia interakcja z AI Google Gemini.
    * **Uwaga:** Komenda nie przechowuje historii poprzednich rozmów.
* `?weather [miasto]`
    * Pobiera aktualną prognozę pogody dla wybranej lokalizacji.
* `?dictionary [słowo]`
    * Wyszukuje angielską definicję słowa lub frazy.

---

## 💾 Pamięć i Baza Danych (SQLite)

* `?remind [czas] [wiadomość]`
    * Ustawia przypomnienie (np. "1h", "30m", "1d"). Bot wyśle Ci prywatną wiadomość o ustalonej porze. Zasilane przez `asyncio tasks.loop` i `sqlite3`.
* `?thx @uzytkownik`
    * Daje punkt "karmy" innemu użytkownikowi.
* `?karma [@uzytkownik]`
    * Sprawdza liczbę punktów karmy (własnych lub oznaczonej osoby).

---

## 🛡️ Moderacja

* `?kick @uzytkownik [powód]`
    * Wyrzuca użytkownika z serwera. Wymaga uprawnień "Wyrzucanie członków".
* `?purge [liczba]`
    * Usuwa określoną liczbę wiadomości z kanału. Wymaga uprawnień "Zarządzanie wiadomościami".

---

## 🎉 Zabawa i Narzędzia

* `?poll [pytanie]`
    * Tworzy prostą ankietę z reakcjami (🟢/🟡/🔴).
* `?diceroll [liczba]`
    * Rzuca kością (domyślnie 6 ścianek).
* `?coinflip`
    * Rzuca monetą (Orzeł lub Reszka).
* `?8ball [pytanie]`
    * Zadaje pytanie magicznej kuli 8.
* `?user [@uzytkownik]`
    * Wyświetla informacje o użytkowniku (kiedy dołączył, kiedy stworzył konto).
* `?message [id_uzytkownika] [wiadomość]`
    * Wysyła prywatną wiadomość do użytkownika.
---

## 🔔 Automatyczne Zdarzenia

* **Powitania:** Automatycznie wita nowych użytkowników na wyznaczonym kanale.
* **Pożegnania:** Żegna użytkowników, którzy opuścili serwer.

---

## 🛠️ Użyte Technologie

* **Python 3.10+**
* **discord.py** (Do interakcji z API Discorda i tworzenia Cogs)
* **sqlite3** (Do trwałego zapisu danych dla przypomnień i karmy)
* **google-generativeai** (Do integracji z API Google Gemini)
* **aiohttp** (Do asynchronicznych zapytań API pogody i słownika)
* **asyncio** (Do obsługi zadań w tle, np. pętli przypomnień)

---

## 🚀 Jak Uruchomić

1.  Sklonuj repozytorium:
    `git clone https://github.com/TwojaNazwa/discord-bot-cogsworth.git`
2.  Przejdź do folderu projektu:
    `cd discord-bot-cogsworth`
3.  Stwórz i aktywuj wirtualne środowisko:
    `python -m venv venv`
    `.\venv\Scripts\activate` (Windows) lub `source venv/bin/activate` (Mac/Linux)
4.  Zainstaluj zależności:
    `pip install -r requirements.txt`
5.  Stwórz plik `.env` i uzupełnij klucze API:
    ```
    DISCORD_TOKEN="TWÓJ_TOKEN_BOTA_DISCORD"
    GEMINI_TOKEN="TWÓJ_KLUCZ_API_GEMINI"
    WEATHER_TOKEN="TWÓJ_KLUCZ_API_OPENWEATHERMAP"
    ```
6.  Uruchom bota:
    `python main.py`