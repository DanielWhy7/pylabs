import argparse
import re

def parse_profiles(text : str) -> List
  """
  Parses the file text into separate profiles.
  Each profile starts with a number like '1)', '2)', etc.
  Inside a profile, fields have the form 'Key: value'.
  """
  profiles = []
  blocks = re.split(r'\n(?=\d+\))', text.strip())
  for block in blocks:
    lines = [line.strip() for line in block.strip().split('\n') if line.strip()]
    if not lines:
      continue
    if re.fullmatch(r'\d+\)', lines[0]):
      lines = lines[1:]
    profile = {}
    for line in lines:
      match = re.match(r'^([^:]+):\s*(.*)$', line)
      if match:
        key = match.group(1).strip()
        value = match.group(2).strip()
        profile[key] = value
    if profile:
      profiles.append(profile)
  return profiles


def is_valid_gender_male(gender : str):
  """Checks whether the gender is male."""
  male_pattern = r'^(М|м|Мужской|мужской)$'
  return re.fullmatch(male_pattern, gender.strip()) is not None


def profile_to_text(profile, index):
  """Builds the profile text for saving to a file."""
  lines = [f"{index})"]
  for key in ['Фамилия', 'Имя', 'Пол', 'Дата рождения', 'Номер телефона или email', 'Город']:
    if key in profile:
      lines.append(f"{key}: {profile[key]}")
  return '\n'.join(lines)


def main():
  parser = argparse.ArgumentParser(description='Counting male profiles')
  parser.add_argument('filename', type=str, help='path to the file with profiles')
  parser.add_argument('-o', '--output', type=str, default='males.txt',
            help='file to save male profiles (default: males.txt)')
  args = parser.parse_args()

  with open(args.filename, 'r', encoding='utf-8') as file:
    text = file.read()

  profiles = parse_profiles(text)

  male_profiles = []
  for profile in profiles:
    gender = profile.get('Пол', '')
    if is_valid_gender_male(gender):
      male_profiles.append(profile)

  print(f"Number of male profiles: {len(male_profiles)}")

  with open(args.output, 'w', encoding='utf-8') as out_file:
    for i, profile in enumerate(male_profiles, start=1):
      out_file.write(profile_to_text(profile, i) + '\n\n')

  print(f"Profiles saved to file: {args.output}")


if __name__ == '__main__':
  main()
