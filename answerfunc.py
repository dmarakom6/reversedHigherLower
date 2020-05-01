def answer(prompt, true_list, false_list):
  choice = input(prompt).lower()
  if choice in true_list:
    return True
  elif choice in false_list:
    return False
  while True:
      if choice not in true_list or false_list:
          return answer(prompt, true_list, false_list)
