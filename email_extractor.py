import re

# Input and output files
input_file = "sample_emails.txt"
output_file = "extracted_emails.txt"


# Read the text file
with open(input_file, "r") as file:
    text = file.read()


# Pattern used to find email addresses
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


# Extract email addresses
emails = re.findall(email_pattern, text)


# Remove duplicate emails
emails = list(set(emails))


# Save emails to an output file
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")


# Display results
print("=" * 40)
print("       EMAIL EXTRACTION TOOL")
print("=" * 40)

print(f"\nEmails found: {len(emails)}")

for email in emails:
    print(email)

print(f"\nEmails saved to {output_file}")