# Skapa timer
# Scenario: Användaren skapar en timer-widget
  Given att appen är öppen
  When användaren klickar på "Add timer"
  Then ska en ny timer-widget visas i listan av widgets

# Skapa anteckning
# Scenario: Användaren skapar en antecknings-widget
  Given att appen är öppen
  When användaren klickar på "Add note"
  Then ska en antecknings-widget visas i listan av widgets

# Ta bort widget
# Scenario: Användaren tar bort en widget
  Given att det finns minst en widget
  When användaren klickar på widgetens "Remove"-knapp
  Then ska widgeten tas bort från vyn

# Byta plats på widgets
#Scenario: Användaren byter plats på två widgets
  Given att det finns minst två widgets
  When användaren drar en widget till en annan widgets position
  Then ska deras placering bytas

# Timerfunktioner
# Ändra tidsinställning
# Scenario: Användaren ändrar timerinställningen
  Given att en timer-widget finns
  When användaren öppnar inställningar och ändrar värdet
  Then ska timern visa den nya starttiden

# Starta timer
# Scenario: Användaren startar timern
  Given att en timer-widget finns
  And timern står på startvärdet
  When användaren klickar på "Start"
  Then ska timern börja räkna ner

# Pausa timer
# Scenario: Användaren pausar timern
  Given att en timer räknar ner
  When användaren klickar på "Pause"
  Then ska nedräkningen stanna men inte återställas

# Återställa timer
# Scenario: Användaren återställer timern
  Given att en timer körs eller är pausad
  When användaren klickar på "Reset"
  Then ska timern återgå till utgångstiden och sluta räkna

# Anteckningar
# Ändra text
Scenario: Användaren redigerar text i en antecknings-widget
  Given att en antecknings-widget finns
  When användaren klickar på textområdet och skriver ny text
  Then ska widgetens text uppdateras

# Ändra temafärg
# Scenario: Användaren byter tema
  Given att appen är öppen
  When användaren klickar på en temaknapp (ex. "Dark", "Forest", "Light")
  Then ska appens färgschema ändras till valt tema