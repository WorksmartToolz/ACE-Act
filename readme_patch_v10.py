with open('README.md', 'r') as f:
    content = f.read()

# Change raw links to blob links so GitHub opens viewer instead of forcing download
replacements = [
    ('https://github.com/WorksmartToolz/ACE-Community-and-Development-Act/raw/main/documents/ACE_Act_v1.5_2026-06.pdf',
     'https://github.com/WorksmartToolz/ACE-Community-and-Development-Act/blob/main/documents/ACE_Act_v1.5_2026-06.pdf'),
    ('https://github.com/WorksmartToolz/ACE-Community-and-Development-Act/raw/main/documents/ACE_Executive_Summary_v1.5_2026-06.pdf',
     'https://github.com/WorksmartToolz/ACE-Community-and-Development-Act/blob/main/documents/ACE_Executive_Summary_v1.5_2026-06.pdf'),
    ('https://github.com/WorksmartToolz/ACE-Community-and-Development-Act/raw/main/documents/ACE_Outreach_Package_v1.5_2026-06.pdf',
     'https://github.com/WorksmartToolz/ACE-Community-and-Development-Act/blob/main/documents/ACE_Outreach_Package_v1.5_2026-06.pdf'),
    ('https://github.com/WorksmartToolz/ACE-Community-and-Development-Act/raw/main/onepagers/ACE_OnePager_Covers_v1.5_2026-06.pdf',
     'https://github.com/WorksmartToolz/ACE-Community-and-Development-Act/blob/main/onepagers/ACE_OnePager_Covers_v1.5_2026-06.pdf'),
    # Also fix old ACE-Act raw links if any remain
    ('https://github.com/WorksmartToolz/ACE-Act/raw/main/',
     'https://github.com/WorksmartToolz/ACE-Community-and-Development-Act/blob/main/'),
]

fixed = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        fixed += 1
        print(f"Fixed: {old[50:90]}...")
    else:
        print(f"NOT FOUND: {old[50:90]}...")

# Also update link labels from "Read PDF" to "View PDF"
content = content.replace('[Read PDF]', '[View PDF]')

with open('README.md', 'w') as f:
    f.write(content)
print(f"\nDone — {fixed} links updated")
