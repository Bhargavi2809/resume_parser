import pandas as pd
import os

FILE_NAME = "candidates.xlsx"


def save_to_excel(name, email, phone, matched, missing, score, status):

    print("Saving to Excel:", name, score)   

    try:

        new_row = pd.DataFrame([{
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Skills": ", ".join(matched),
            "Missing Skills": ", ".join(missing),
            "ATS Score": score,
            "Status": status
        }])

        # If file exists
        if os.path.exists(FILE_NAME):

            old_data = pd.read_excel(FILE_NAME)

            updated = pd.concat([old_data, new_row], ignore_index=True)

            updated.to_excel(FILE_NAME, index=False)

        else:

            new_row.to_excel(FILE_NAME, index=False)

        print("✅ Excel saved successfully")

    except Exception as e:
        print("❌ Excel Error:", e)