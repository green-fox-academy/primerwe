# Add "My todo:" to the beginning of the todoText
# Add " - Download games" to the end of the todoText
# Add " - Diablo" to the end of the todoText but with indention

# Expected outpt:

# My todo:
#  - Buy milk
#  - Download games
#      - Diablo


todoText = " - Buy milk\n"

toDos = " - Download games\n"
games = "    - Diablo"

todoText = "".join((todoText, toDos, games))
print(todoText)