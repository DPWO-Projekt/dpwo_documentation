# DPWO Studium Procesu Wytwórczego

*February 2025*

## Spis treści
- [Wprowadzenie](#wprowadzenie)
- [Organizacja Pracy](#organizacja-pracy)
- [Narzędzia](#narzędzia)
- [Analiza Systemowa](#analiza-systemowa)
  - [Supplementary Specifications (Specyfikacja Uzupełniająca)](#supplementary-specifications-specyfikacja-uzupełniająca)
  - [Glossary (Słownik)](#glossary-słownik)
  - [Requirements Specification (Specyfikacja Wymagań)](#requirements-specification-specyfikacja-wymagań)
- [Architektura](#architektura)
  - [Wzorce projektowe](#wzorce-projektowe)
  - [Przebieg fazy analizy US](#przebieg-fazy-analizy-us)
  - [Diagramy](#diagramy)
- [Bazy Danych](#bazy-danych)
- [UI-UX](#ui-ux)
  - [Etapy tworzenia prototypu UI](#etapy-tworzenia-prototypu-ui)
  - [Wytyczne projektowania UI](#wytyczne-projektowania-ui)
- [Frontend](#frontend)
  - [Etapy](#etapy)
  - [Wytyczne do implementacji](#wytyczne-do-implementacji)
- [Backend](#backend)
  - [Etapy tworzenia komponentów](#etapy-tworzenia-komponentów)
  - [Wytyczne projektowania komponentów](#wytyczne-projektowania-komponentów)
  - [Dokumentacja i wdrożenie](#dokumentacja-i-wdrożenie)
- [Testy](#testy)
  - [Test Script (scenariusz testowy)](#test-script-scenariusz-testowy)
  - [Test Suite (zestaw testów)](#test-suite-zestaw-testów)
  - [Test Log (dziennik testów)](#test-log-dziennik-testów)
  - [Żądania zmian](#żądanía-zmian)
- [Code Review](#code-review)
  - [Cele](#cele)
  - [Kryteria oceny kodu](#kryteria-oceny-kodu)
  - [Przebieg Code Review](#przebieg-code-review)

## Wprowadzenie

Dokument stanowi studium procesu wytwórczego, opisujące kluczowe etapy, metody oraz narzędzia wykorzystywane w realizacji projektu. Zawiera wytyczne dotyczące tworzenia produktów pracy, wzbogacone o przykłady i wzorce ułatwiające ich opracowanie.

## Organizacja Pracy

Praca będzie prowadzona w 3-tygodniowych iteracjach z wykorzystaniem następujących zasad:
- Zarządzanie statusem i postępem prac w systemie Jira
- Każda funkcjonalność jako osobne User Story (US) z podzadaniami dla:
  - Analizy
  - Architektury
  - UI/UX
  - Frontendu
  - Backendu
  - Testów
- Bezpośrednie powiadamianie kolejnych wykonawców przez Discord po zakończeniu etapu

## Narzędzia

- **Project Management**: Jira, Confluence
- **UI/UX Design**: Figma
- **Frontend**: React
- **Backend**: Java, Spring Boot
- **Baza Danych**: MongoDB, MongoDB Compass
- **Testowanie**: JUnit, Selenium, Mockaroo
- **Version Control**:
  - Git, GitHub (centralna organizacja projektu)
  - Dwa dedykowane repozytoria:
    - Frontend
    - Backend
- **CI/CD**:
  - GitHub Actions (integracja z repozytoriami)
  - Amazon EC2 (docelowa infrastruktura deploymentu)
  - Automatyzacja testów i procesu wdrażania
- **Diagramy**: Enterprise Architect, Lucidchart

## Analiza Systemowa

W poniższej części dokumentu opisane zostanę kluczowe produkty, które precyzują zarówno funkcjonalne, jak i niefunkcjonalne aspekty systemu, stanowiąc podstawę do dalszych etapów projektowania i implementacji.

**Zbieranie wymagań**
- Wywiady
- Warsztaty
- Analiza dokumentacji

**Zarządzanie wymaganiami**
- Do przechowywania i zarządzania wymaganiami wykorzystane zostanie oprogramowanie Jira. Będą one opisywane za pośrednictwem przypadków użycia. Każdy przypadek użycia posiada swój numer id, nazwę oraz opis w postaci scenariusza.

![Przykładowy scenariusz dla przypadku użycia.](scenario.jpg)

- W ramach śledzenia wymagań oraz postępów projktu, wykorzystane zostaną rozmaite narzędzia oferowane przez oprogramowanie Jira oraz Confluence:
  - Tablica Kanban (Jira) - Całościowe śledzenie postępu realizacji wymagań. Podział według statusu zadań (Do zrobienia, W toku, Code Review, Gotowe).
  - Stories (Jira) - Szczegółowy opis poszczególnych przypadków użycia oraz powiązanych z nimi scenariuszy.
  - Szablon wywiadów Q&A (Confluence) - Narzędzie wspomagające przeprowadzanie wywiadów z klientem i tworzenia notatek on-line.
  - Szablon słownika (Confluence) - Narzędzie do tworzenia wersji słownika opisującego niejednoznaczne zagadnienia biznesowe.

**Priorytetyzacja oraz szacowanie pracochłonności wymagań**
- Ocena ważności wymagań realizowana będzie zgodnie z podejściem MoSCoW (must, should, could, won't).
- Przypisanie odpowiednich etykiet priorytetów w Jirze.
- Czasochłonność określana w MD (man-day) przy pomocy Scrum Poker'a.

**Wykorzystywane narzędzia**
- Jira - przechowywanie i zarządzanie wymaganiami przy pomocy tablicy Kanban oraz Stories.
- Confluence - tworzenie słownika opisowego oraz zapisu wywiadu Q&A.
- Lucidchart - tworzenie słownika w postaci diagramu klas.

### Supplementary Specifications (Specyfikacja Uzupełniająca)

**Wymagania jakościowe**
- Wydajność - określenie maksymalnego czasu odpowiedzi systemu, liczby obsługiwanych użytkowników
- Dostępność - zapewnienie wysokiej dostępności systemu (SLA)
- Bezpieczeństwo – zabezpieczenia przed atakami, autoryzacja, szyfrowanie danych
- Zgodność z regulacjami prawnymi - wymagania prawne i branżowe (np. RODO)
- Zgodność ze standardami (np. DCAT-AP)

Wszystkie wymagania niefunkcjonalne zostaną spisane w dokumencie **Specyfikacja Uzupełniająca**, który będzie jednym z produktów analizy systemowej. Dokument ten będzie podstawą do testowania i walidacji systemu w kontekście spełnienia założeń jakościowych, zgodnie z przedstawionymi w nim metrykami.

### Glossary (Słownik)

**Definiowanie kluczowych terminów oraz definicji domenowych**
- Opis podstawowych pojęć oraz skrótów i akronimów używanych w projekcie
- Opis zrealizowany zostanie za pośrednictwem diagramów klas oraz osobnego dokumentu uwzględniającego definicje konkretnych haseł
- Przykłady pojęć zawieranych w słowniku: API (Application Programming Interface), SLA (Service Level Agreement), Metadane

### Requirements Specification (Specyfikacja Wymagań)

Każdy przypadek użycia został opisany poprzez:
- unikalny identyfikator (np. **UC-DM-002**)
- priorytet według schematu MoSCoW (M-1 – krytyczne, S-2 – średnie, C-3 – niskie, W-4 – bardzo niskie)
- opis interakcji użytkownika z systemem

Przypadki użycia przedstawione są w formie diagramów oraz scenariuszy. Specyfikacja ta umożliwia przeprowadzenie implementacji zgodnie z określonymi wymaganiami funkcjonalnymi oraz zapewnia podstawę do testowania poprawności działania systemu.

## Architektura

### Wzorce projektowe

Oprogramowanie wytwarzane będzie zgodnie ze wzorcem Model-View-Controller (MVC), co zapewni jego modułowość, przejrzystość oraz łatwość utrzymania i rozwoju.

- **Modele** – Odpowiadają za logikę biznesową i operacje na danych
- **Widoki** – Odpowiadają za prezentację danych użytkownikowi
- **Kontrolery** – Odpowiadają za pośredniczenie między Widokami a Modelami, obsługując interakcje użytkownika

W ramach technologii stosowanych w projekcie:
- Frontend zostanie zaimplementowany w React, co umożliwi tworzenie dynamicznych i responsywnych interfejsów użytkownika
- Backend będzie oparty na języku Java z wykorzystaniem nowoczesnych frameworków, takich jak Spring Boot, zapewniających wysoką wydajność i łatwość integracji
- Baza danych będzie przechowywana w MongoDB, co umożliwi elastyczne zarządzanie danymi w formacie dokumentowym
- Komunikacja między frontendem a backendem odbywać się będzie poprzez REST API, co zapewni skalowalność i łatwość integracji z innymi systemami

### Przebieg fazy analizy US

- Analiza architektoniczna przypadków użycia – określenie przynależności przypadków użycia do poszczególnych komponentów systemu oraz ich roli w architekturze
- Opracowanie planu implementacji – identyfikacja kolejności wdrażania poszczególnych przypadków użycia zgodnie z priorytetami biznesowymi i technicznymi
- Definicja struktury kodu – określenie hierarchii klas, metod oraz pól w zgodzie z zasadami projektowania obiektowego oraz wzorcem MVC
- Określenie protokołu komunikacji – specyfikacja punktów końcowych API (endpoints), formatów przesyłanych danych oraz metod komunikacji pomiędzy frontendem a backendem
- Tworzenie diagramów architektonicznych – wizualizacja struktury systemu za pomocą diagramów UML, w tym diagramów przypadków użycia, diagramów klas oraz diagramów sekwencji

### Diagramy

W wyniku analizy architektonicznej będą tworzone następujące diagramy:
- **Diagram klas** – przedstawia strukturę systemu, pokazując klasy oraz ich wzajemne relacje
- **Diagram komponentów** – ilustruje fizyczną strukturę systemu, pokazując poszczególne komponenty i ich zależności
- **Diagram sekwencji** – opisuje interakcje pomiędzy obiektami w systemie w ramach określonego scenariusza

## Bazy Danych

W ramach stworzenia systemu projektanci bazy danych odpowiadają za zaprojektowanie, utworzenie oraz optymalizację struktury bazy danych. W projekcie zdecydowano się na wykorzystanie systemu zarządzania bazami danych MongoDB oraz dokumentów JSON jako formy projektu struktury dokumentów.

**Przykład dokumentu data_schema:**
```json
{
    "_id": {
        "$oid": "67c75aab6b0968ffa0850188"
    },
    "name": "sample schema",
    "elements": [{
            "name": "pole1",
            "type": "string"
        }, {
            "name": "pole2",
            "type": "int"
        }
    ]
}
