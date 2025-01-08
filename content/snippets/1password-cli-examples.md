Title: 1password CLI Examples
Date: 2024-11-15 12:00
Category: snippets
Tags: 1password

Snippets for using the 1password CLI tool; learned about this tool today while reading
a [blog post](https://simonwillison.net/2024/Nov/15/recraft-v3/#atom-everything) by Simon Willison -- very handy tool.

Remainder of this post written by Claude 3.5 Sonnet V2 as a quick reference.

```bash
# Get API token from 1Password and use in API call
export API_TOKEN="$(
op item get "Service API Key" --fields label=password \
--format json | jq -r .value)"

curl https://api.example.com/v1/endpoint \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $API_TOKEN" \
-d '{
"param1": "value1",
"param2": "value2"
}'
```

```bash
# View all items in a vault
op item list --vault "Personal"
```

```bash
# Get a password (outputs only the password value)
op item get "MyLogin" --fields label=password
```

```bash
# Get a password in raw format (useful for scripts)
op item get "MyLogin" --fields label=password --format json | jq -r .value
```

```bash
# Create a new login item
op item create --category login \
--title "New Service" \
--vault "Personal" \
username="user@example.com" \
password="mysecret123" \
url="https://example.com"
```

```bash
# Generate and store a new password
op item create --category password \
--title "Generated Password" \
--generate-password
```

```bash
# Get all fields for an item
op item get "MyLogin"
```

```bash
# Create a secure note
op item create --category "Secure Note" \
--title "Project Notes" \
--vault "Work" \
'notesPlain[text]="Important project details..."'
```

```bash
# Use secrets in environment variables
eval $(op signin)
export DB_PASSWORD="$(op item get "Database" --fields label=password)"
export API_KEY="$(op item get "API Keys" --fields label=key)"
```

```bash
# Read SSH keys or certificates
op item get "SSH Key" --fields label=private_key
```

```bash
# List all vaults
op vault list
```

```bash
# Search for items
op item list --query "database"
```
Here's the revised version of your update, with improved grammar, flow, and formatting:

---

## Update on 2025-01-08

Recently, I integrated the CLI usage of the `op` tool into a Python Streamlit app that I run locally on my MacBook. This integration allows me to securely manage Google credentials and an OAuth token, enabling programmatic access to my Google Calendars. Here's how I achieved it:

### Python Code Example

The following code snippet demonstrates how I retrieve credentials and tokens from 1Password, use them to initialize a calendar access class, and then update the token back to 1Password if it changes:

```python
from tempfile import NamedTemporaryFile
import subprocess
import json
import os
from supersullytools.gcalendar_access import GoogleCalendarDataAccess


def get_calendar_access():
    """
    Fetches Google OAuth credentials from 1Password, writes them to temporary files,
    initializes GoogleCalendarDataAccess, and updates the token back to 1Password if needed.
    """

    def op_get_field(item_name: str, field_name: str):
        """
        Uses the 1Password CLI (`op`) to retrieve the raw JSON content of a specified field.
        """
        cmd = [
            "op",
            "item",
            "get",
            item_name,
            "--fields",
            field_name,
            "--format",
            "json",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)["value"]  # Returns the field's raw JSON content

    def op_set_field(item_name: str, field_name: str, new_value: str) -> bool:
        """
        Updates the content of a specific field in a 1Password item using the `op` CLI.
        Returns True if successful, otherwise False.
        """
        cmd = ["op", "item", "edit", item_name, f"{field_name}={new_value}"]
        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error updating 1Password field: {e}")
            return False

    # Retrieve the credentials and token JSON from 1Password
    creds_json = op_get_field(
        os.environ["ONEPASS_GOOGLE_CREDS_ITEM"],  # Adjust item name/ID as needed
        "notesPlain",  # json str stored in a Secure Note
    )

    token_json = op_get_field(
        os.environ["ONEPASS_GOOGLE_TOKEN_ITEM"],  # Adjust item name/ID as needed
        "notesPlain",  # json str stored in a Secure Note
    )

    # Write the credentials and token to temporary files
    with NamedTemporaryFile(mode="w+") as tmp_file1, NamedTemporaryFile(mode="w+") as tmp_file2:
        tmp_file1.write(creds_json)
        tmp_file1.flush()
        tmp_file1.seek(0)
        temp_credentials_path = tmp_file1.name

        tmp_file2.write(token_json)
        tmp_file2.flush()
        tmp_file2.seek(0)
        temp_token_path = tmp_file2.name

        # Initialize the GoogleCalendarDataAccess class
        calendar = GoogleCalendarDataAccess(
            credentials_file=temp_credentials_path,
            token_file=temp_token_path,
            default_calendar_id=os.environ["EVENT_CALENDAR_ID"],
            fallback_timezone="America/Los_Angeles",
        )

        # Check if the token was updated and save it back to 1Password if necessary
        tmp_file2.seek(0)
        updated_token_json = tmp_file2.read()
        if updated_token_json != token_json:
            op_set_field(
                os.environ["ONEPASS_GOOGLE_TOKEN_ITEM"],  # Adjust item name/ID as needed
                "notesPlain",  # json str stored in a Secure Note
                updated_token_json,
            )

    return calendar
```

A really cool benefit of this is that it automatically integrates into the 1password Biometrics / fingerprint scanner on my Macbook when it needs to regain access to the protected items

![1passbio.png]({attach}1passbio.png)
