# Testdokumentation – Timer & Note Widget App

## 📌 Översikt
Denna dokumentation beskriver user stories, acceptanskriterier, testscenarier och automatiserade end-to-end tester för projektet. Fokus ligger på funktionalitet för timers, anteckningar, widgets och temahantering.

Applikation: `https://tovinou.github.io/test/`  
Kodbas: `https://github.com/Tovinou/test.git`  
Status: ✅ Deployad och fungerar

---

## 1. User Stories

### Skapa och ta bort widgets
- Som användare vill jag kunna skapa en timer-widget så att jag kan hålla koll på tid för olika aktiviteter.
- Som användare vill jag kunna skapa en antecknings-widget så att jag kan skriva ner saker jag behöver komma ihåg.
- Som användare vill jag kunna ta bort en widget så att jag kan rensa bort sådant jag inte längre behöver.

### Flytta eller byta plats på widgets
- Som användare vill jag kunna byta plats på två widgets så att jag kan organisera innehållet i den ordning jag föredrar.

### Timerinställningar & styrning
- Som användare vill jag kunna ändra tiden på en timer så att den passar mitt aktuella behov.
- Som användare vill jag kunna starta en timer så att nedräkningen börjar.
- Som användare vill jag kunna pausa timern så att jag tillfälligt kan stoppa nedräkningen.
- Som användare vill jag kunna återställa timern så att den går tillbaka till sin ursprungliga tid.

### Anteckningar
- Som användare vill jag kunna ändra text på en anteckning så att jag kan uppdatera innehållet när något ändras.

### Tema & design
- Som användare vill jag kunna ändra appens temafärg så att gränssnittet får ett utseende jag föredrar.

---

## 2. Acceptanskriterier

### Skapa timer
| Kriterium | Beskrivning |
|-----------|-------------|
| UI-knapp | En knapp "Add timer" ska finnas |
| Ny widget skapas | När knappen klickas skapas en timer |
| Standardtid | Timer startar med defaultvärde, t.ex. 15:00 |

### Skapa anteckning
| Kriterium | Beskrivning |
|-----------|-------------|
| UI-knapp | En knapp "Add note" ska finnas |
| Ny widget skapas | När knappen klickas visas en anteckning |
| Defaulttext | Standardtext visas tills användaren ändrar den |

### Ta bort widget
| Kriterium | Beskrivning |
|-----------|-------------|
| UI-knapp | Varje widget ska kunna raderas |
| Effekt | Widget tas bort från visningen |

### Hantera flera widgets
| Kriterium | Beskrivning |
|-----------|-------------|
| Mixed layout | Appen kan visa både timers och notes samtidigt |
| Widget-ordning | Timers renderas först, sedan notes |
| Notera | Drag-and-drop är inte implementerat i nuvarande version |

### Timerfunktioner
| Funktion | Kriterier |
|----------|-----------|
| Start | Timer börjar räkna ner |
| Pause | Timer stoppar utan att återställas |
| Reset | Timer återgår till startvärde |
| Ändra tid | Ny starttid sparas och används vid reset |

### Anteckningsredigering
| Kriterium | Beskrivning |
|-----------|-------------|
| Redigerbart textfält | Text kan ändras |
| Automatiskt sparande | Ändringen visas direkt |

### Ändra tema
| Kriterium | Beskrivning |
|-----------|-------------|
| Tema-knappar | Teman kan väljas |
| UI ändras | Färger uppdateras när tema byts |

---

## 3. Testscenarier (Gherkin)

### Skapa & ta bort widgets
```gherkin
Scenario: Skapa och radera widgets
  Given appen är öppen
  When användaren klickar "Add timer"
  Then ska en timer-widget visas

  When användaren klickar "Add note"
  Then ska en anteckning visas

  When användaren tar bort en timer-widget
  Then ska widgeten inte längre visas
