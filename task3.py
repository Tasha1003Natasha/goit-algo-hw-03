import re

def normalize_phone(phone_number):
  """
  Normalizes phone numbers to the standard format, leaving only the digits and the '+' symbol at the beginning.
  """

  phone_number = phone_number.strip()
  pattern = r"[+\d]"
  matches = re.findall(pattern, phone_number)
  normalized = "".join(matches)


  if  normalized.startswith("+"):
        return  normalized
  elif  normalized.startswith("380"):
        return "+" +  normalized
  else:
        return "+38" +  normalized
