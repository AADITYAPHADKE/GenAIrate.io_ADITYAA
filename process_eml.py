import email
from email import policy

print("Processing EML file...\n")

# path to your eml file
eml_path = "sample_files/Example_file1.eml"


# open and read eml
with open(eml_path, "r", encoding="utf-8", errors="ignore") as f:
    msg = email.message_from_file(f, policy=policy.default)

# extract details
subject = msg["subject"]
from_ = msg["from"]
to_ = msg["to"]

body = ""

if msg.is_multipart():
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            body += part.get_payload(decode=True).decode(errors="ignore")
else:
    body = msg.get_payload(decode=True).decode(errors="ignore")

# create output text
output_text = f"""
SUBJECT: {subject}
FROM: {from_}
TO: {to_}

BODY:
{body}
"""

# save to file
output_path = "EX1_output.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(output_text)

print("EML processed successfully.")
print(f"Output saved as: {output_path}")
