from app.database.db import (
    get_engine,
    get_session
)

from app.database.models import (
    Base,
    Professor
)

from app.crawler.university_sources import (
    UNIVERSITIES
)

from app.crawler.faculty_crawler import (
    crawl_university
)

from app.enrichment.exporter import (
    export_csv
)


def normalize_email(email):

    if not email:
        return None

    return email.strip().lower()


def is_valid_professor(professor):

    name = professor.get("name")

    email = professor.get("email")

    if not name:
        return False

    if not email:
        return False

    department = professor.get(
        "department"
    )

    expertise = professor.get(
        "expertise"
    )

    research_interests = professor.get(
        "research_interests"
    )

    has_research_signal = any([

        department and len(
            str(department).strip()
        ) > 0,

        expertise and len(
            str(expertise).strip()
        ) > 0,

        research_interests and len(
            str(research_interests).strip()
        ) > 0
    ])

    return has_research_signal


def professor_exists(db, email):

    if not email:
        return False

    normalized_email = normalize_email(
        email
    )

    existing = db.query(
        Professor
    ).filter(
        Professor.email == normalized_email
    ).first()

    return existing is not None


def save_professor(
    db,
    data,
    college_name
):

    try:

        email = normalize_email(
            data.get("email")
        )

        if email:

            exists = professor_exists(
                db,
                email
            )

            if exists:

                print(
                    f"DUPLICATE EMAIL SKIPPED: "
                    f"{email}"
                )

                return False

        professor = Professor(

            college_name=college_name,

            name=data.get("name"),

            university=data.get("university"),

            department=data.get(
                "department"
            ),

            email=email,

            phone=data.get("phone"),

            profile_url=data.get(
                "profile_url"
            ),

            resume_url=data.get(
                "resume_url"
            ),

            linkedin=data.get(
                "linkedin"
            ),

            scholar=data.get(
                "scholar"
            ),

            expertise=data.get(
                "expertise"
            ),

            research_interests=data.get(
                "research_interests"
            ),

            summary=data.get(
                "summary"
            ),

            resume_text=data.get(
                "resume_text"
            ),

            score=data.get("score")
        )

        db.add(professor)

        db.commit()

        return True

    except Exception as e:

        print(
            f"DB INSERT FAILED: {e}"
        )

        return False


if __name__ == "__main__":

    print("\n" + "=" * 80)

    print("AVAILABLE UNIVERSITIES")

    print("=" * 80)

    for index, university in enumerate(
        UNIVERSITIES
    ):

        print(
            f"{index + 1}. "
            f"{university['name']}"
        )

    choice = int(
        input(
            "\nEnter university number: "
        )
    )

    selected_university = UNIVERSITIES[
        choice - 1
    ]

    college_name = selected_university[
        "name"
    ]

    # ----------------------------------------
    # COLLEGE-SPECIFIC DATABASE
    # ----------------------------------------

    engine = get_engine(
        college_name
    )

    Base.metadata.create_all(
        bind=engine
    )

    db = get_session(
        college_name
    )

    print("\n" + "=" * 80)

    print(
        f"SELECTED UNIVERSITY: "
        f"{college_name}"
    )

    print("=" * 80)

    confirm = input(
        "\nProceed with crawling? (yes/no): "
    ).strip().lower()

    if confirm != "yes":

        print("\nOperation cancelled.")

        exit()

    professors = crawl_university(

        selected_university["url"],

        college_name
    )

    valid_professors = []

    processed_count = 0

    saved_count = 0

    skipped_count = 0

    duplicate_count = 0

    for professor in professors:

        processed_count += 1

        print("\n" + "-" * 80)

        print(
            f"PROCESSING RECORD "
            f"{processed_count}/"
            f"{len(professors)}"
        )

        if not is_valid_professor(
            professor
        ):

            skipped_count += 1

            print(
                "INVALID PROFESSOR - SKIPPED"
            )

            continue

        success = save_professor(

            db,

            professor,

            college_name
        )

        if success:

            saved_count += 1

            valid_professors.append(
                professor
            )

            print(
                f"SAVED: "
                f"{professor.get('name')}"
            )

        else:

            duplicate_count += 1

            print(
                f"DUPLICATE: "
                f"{professor.get('name')}"
            )

    ranked = sorted(

        valid_professors,

        key=lambda x: x["score"],

        reverse=True
    )

    export_csv(

        ranked,

        college_name
    )

    print("\n" + "=" * 80)

    print("FINAL SUMMARY")

    print("=" * 80)

    print(
        f"University: "
        f"{college_name}"
    )

    print(
        f"Profiles Processed: "
        f"{processed_count}"
    )

    print(
        f"Profiles Saved: "
        f"{saved_count}"
    )

    print(
        f"Profiles Skipped: "
        f"{skipped_count}"
    )

    print(
        f"Duplicate Emails: "
        f"{duplicate_count}"
    )

    print("=" * 80)

    db.close()