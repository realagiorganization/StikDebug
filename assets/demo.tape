Output assets/demo.gif
Set Width 900
Set Height 520
Set FontSize 16
Set Theme "Dracula"

Type "echo 'StikDebug BDD demo'"
Enter
Sleep 1s
Type "python3 -m behave --format progress2 --summary bdd/features"
Enter
Sleep 2s
