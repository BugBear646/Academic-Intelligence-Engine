from sqlalchemy.orm import Session

from app.database.db import engine
from app.database.models import Professor

from sqlalchemy.orm import sessionmaker


SessionLocal = sessionmaker(bind=engine)


def normalize_email(email):

    if not email:
        return None

    return email.strip().lower()


def remove_duplicate_professors():

    db: Session = SessionLocal()

    professors = db.query(Professor).all()

    print(
        f"\nTotal records before cleanup: "
        f"{len(professors)}"
    )

    seen_emails = set()

    duplicate_ids = []

    no_email_count = 0

    for professor in professors:

        email = normalize_email(
            professor.email
        )

        # Skip empty emails
        if not email:

            no_email_count += 1

            continue

        # Duplicate detected
        if email in seen_emails:

            duplicate_ids.append(
                professor.id
            )

            print(
                f"DUPLICATE FOUND:"
            )

            print(
                f"ID: {professor.id}"
            )

            print(
                f"Name: {professor.name}"
            )

            print(
                f"Email: {email}"
            )

            print("-" * 50)

        else:

            seen_emails.add(email)

    print(
        f"\nTotal duplicates found: "
        f"{len(duplicate_ids)}"
    )

    # ----------------------------------------
    # DELETE DUPLICATES
    # ----------------------------------------

    deleted_count = 0

    for duplicate_id in duplicate_ids:

        professor = db.query(
            Professor
        ).filter(
            Professor.id == duplicate_id
        ).first()

        if professor:

            db.delete(professor)

            deleted_count += 1

    db.commit()

    final_count = db.query(
        Professor
    ).count()

    print("\n" + "=" * 80)

    print("DATABASE CLEANUP SUMMARY")

    print("=" * 80)

    print(
        f"Initial Records: "
        f"{len(professors)}"
    )

    print(
        f"Duplicates Removed: "
        f"{deleted_count}"
    )

    print(
        f"Records Without Email: "
        f"{no_email_count}"
    )

    print(
        f"Final Records: "
        f"{final_count}"
    )

    print("=" * 80)

    db.close()


if __name__ == "__main__":

    remove_duplicate_professors()