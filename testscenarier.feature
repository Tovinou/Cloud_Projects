# 1 — Skapa och radera widgets
# Scenario: Användaren lägger till och tar bort widgets

  Given appen är öppen
  When användaren klickar på "Add timer"
  Then ska en timer-widget visas

  When användaren klickar på "Add note"
  Then ska en antecknings-widget visas

  When användaren tar bort en timer-widget
  Then ska timern inte längre visas

# 2 — Timer start, paus, reset
# Scenario: Styra timer

  Given en timer-widget finns
  When användaren klickar "Start"
  Then ska tiden börja minska

  When användaren klickar "Pause"
  Then ska tiden sluta minska

  When användaren klickar "Reset"
  Then ska tiden återställas till startvärdet

# 3 — Anpassa starttid
# Scenario: Användaren ändrar timerinställning

  Given en timer-widget finns
  When användaren ändrar startvärdet till 10:00
  And klickar "Reset"
  Then ska timerdisplayen visa 10:00

# 4 — Redigera anteckning
# Scenario: Ändra text i anteckning

  Given en anteckning finns
  When användaren skriver ny text
  Then ska widgeten visa den uppdaterade texten

# 5 — Ändra tema
# Scenario: Byta tema

  Given att appen är öppen
  When användaren klickar på "Forest"
  Then ska appens färgtema ändras till Forest