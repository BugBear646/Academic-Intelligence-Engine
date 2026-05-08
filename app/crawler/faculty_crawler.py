import re
import time

from playwright.sync_api import (
    sync_playwright
)

from app.crawler.profile_parser import (
    parse_profile
)

from app.enrichment.llm_extractor import (
    extract_professor_metadata
)

from app.enrichment.scorer import (
    calculate_score
)


EMAIL_REGEX = (
    r"^[A-Za-z0-9._%+-]+"
    r"@[A-Za-z0-9.-]+"
    r"\.[A-Za-z]{2,}$"
)


def is_valid_email(email):

    if not email:

        return False

    email = email.strip().lower()

    # ----------------------------------------
    # REGEX CHECK
    # ----------------------------------------

    if not re.match(
        EMAIL_REGEX,
        email
    ):

        return False

    # ----------------------------------------
    # INVALID PLACEHOLDERS
    # ----------------------------------------

    invalid_terms = [

        "example",

        "test",

        "sample",

        "dummy",

        "noreply",

        "no-reply"
    ]

    for term in invalid_terms:

        if term in email:

            return False

    return True


def extract_profile_links(page):

    profiles = set()

    links = page.locator("a").evaluate_all(
        """
        elements => elements.map(
            e => e.href
        )
        """
    )

    for href in links:

        if not href:
            continue

        href = href.split("#")[0]
        href = href.split("?")[0]

        # Stanford faculty profile pattern
        if (
            "/faculty-research/faculty/" in href
            and href.count("/") >= 5
        ):

            if href.endswith("/faculty"):
                continue

            profiles.add(href)

    return sorted(list(profiles))


def scroll_until_loaded(page):

    previous_profile_count = 0

    stable_rounds = 0

    max_stable_rounds = 3

    max_scroll_attempts = 50

    current_attempt = 0

    print(
        "\nStarting dynamic faculty loading..."
    )

    while current_attempt < max_scroll_attempts:

        current_attempt += 1

        # ----------------------------------------
        # SCROLL TO BOTTOM
        # ----------------------------------------

        page.evaluate(
            "window.scrollTo(0, document.body.scrollHeight)"
        )

        print(
            f"\nScroll Attempt: "
            f"{current_attempt}"
        )

        print(
            "Waiting 15 seconds for "
            "new profiles to load..."
        )

        # ----------------------------------------
        # WAIT FOR LAZY LOADING
        # ----------------------------------------

        time.sleep(15)

        current_profiles = extract_profile_links(
            page
        )

        current_profile_count = len(
            current_profiles
        )

        print(
            f"Current Faculty Profiles: "
            f"{current_profile_count}"
        )

        # ----------------------------------------
        # PROFILE GROWTH CHECK
        # ----------------------------------------

        if (
            current_profile_count
            == previous_profile_count
        ):

            stable_rounds += 1

            print(
                f"No new profiles loaded "
                f"({stable_rounds}/"
                f"{max_stable_rounds})"
            )

        else:

            new_profiles = (
                current_profile_count
                - previous_profile_count
            )

            print(
                f"New profiles discovered: "
                f"{new_profiles}"
            )

            stable_rounds = 0

        previous_profile_count = (
            current_profile_count
        )

        # ----------------------------------------
        # STOP AFTER STABILIZATION
        # ----------------------------------------

        if stable_rounds >= max_stable_rounds:

            print(
                "\nFaculty loading stabilized."
            )

            break

    print("\n" + "=" * 80)

    print(
        f"FINAL PROFILE COUNT: "
        f"{previous_profile_count}"
    )

    print("=" * 80)


def is_valid_professor(record):

    # ----------------------------------------
    # REQUIRED NAME
    # ----------------------------------------

    name = record.get("name")

    if not name:

        print(
            "Validation Failed: Missing Name"
        )

        return False

    if len(str(name).strip()) == 0:

        print(
            "Validation Failed: Blank Name"
        )

        return False

    # ----------------------------------------
    # REQUIRED EMAIL
    # ----------------------------------------

    email = record.get("email")

    if not is_valid_email(email):

        print(
            f"Validation Failed: "
            f"Invalid Email -> {email}"
        )

        return False

    # ----------------------------------------
    # RESEARCH SIGNAL
    # ----------------------------------------

    department = record.get(
        "department"
    )

    expertise = record.get(
        "expertise"
    )

    research_interests = record.get(
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

    if not has_research_signal:

        print(
            "Validation Failed: "
            "No Research Signal"
        )

        return False

    return True


def crawl_university(directory_url, university_name):

    all_profiles = []

    unique_links = set()

    processed_urls = set()

    processed_names = set()

    processed_emails = set()

    processed_count = 0

    saved_count = 0

    failed_count = 0

    duplicate_count = 0

    with sync_playwright() as p:

        browser = p.chromium.launch(

            headless=False
        )

        page = browser.new_page()

        print("\n" + "=" * 80)

        print(
            f"Opening University: "
            f"{university_name}"
        )

        print("=" * 80)

        page.goto(

            directory_url,

            timeout=60000
        )

        print(
            "\nWaiting for faculty page "
            "to initialize..."
        )

        time.sleep(10)

        # ----------------------------------------
        # LOAD ENTIRE FACULTY DIRECTORY
        # ----------------------------------------

        scroll_until_loaded(page)

        # ----------------------------------------
        # EXTRACT FINAL LINKS
        # ----------------------------------------

        print(
            "\nExtracting faculty links..."
        )

        profile_links = extract_profile_links(
            page
        )

        for link in profile_links:

            unique_links.add(link)

        print("\n" + "=" * 80)

        print(
            f"TOTAL UNIQUE FACULTY LINKS: "
            f"{len(unique_links)}"
        )

        print("=" * 80)

        # ----------------------------------------
        # PROCESS EACH FACULTY PROFILE
        # ----------------------------------------

        for link in sorted(unique_links):

            try:

                # ----------------------------------------
                # DUPLICATE URL CHECK
                # ----------------------------------------

                if link in processed_urls:

                    duplicate_count += 1

                    continue

                processed_urls.add(link)

                processed_count += 1

                print("\n" + "-" * 80)

                print(
                    f"PROFILE "
                    f"{processed_count}/"
                    f"{len(unique_links)}"
                )

                print(f"URL: {link}")

                page.goto(

                    link,

                    timeout=30000
                )

                time.sleep(5)

                profile_html = page.content()

                # ----------------------------------------
                # PARSE PROFILE
                # ----------------------------------------

                parsed = parse_profile(

                    link,

                    profile_html
                )

                combined_input = (

                    parsed.get("summary", "")

                    + "\n\n"

                    + parsed.get(
                        "resume_text",
                        ""
                    )
                )

                combined_input = combined_input[
                    :12000
                ]

                # ----------------------------------------
                # LLM EXTRACTION
                # ----------------------------------------

                metadata = extract_professor_metadata(

                    combined_input,

                    extracted_email=parsed.get(
                        "email"
                    )
                )

                # ----------------------------------------
                # SCORE CALCULATION
                # ----------------------------------------

                combined_text = (

                    str(
                        metadata.get(
                            "expertise",
                            ""
                        )
                    )

                    + " "

                    + str(
                        metadata.get(
                            "research_interests",
                            ""
                        )
                    )

                    + " "

                    + parsed.get(
                        "summary",
                        ""
                    )
                )

                score = calculate_score(
                    combined_text
                )

                # ----------------------------------------
                # FINAL STRUCTURED RECORD
                # ----------------------------------------

                final_record = {

                    **parsed,

                    **metadata,

                    "profile_url": link,

                    "college_name": university_name,

                    "university": university_name,

                    "score": score
                }

                # ----------------------------------------
                # VALIDATION
                # ----------------------------------------

                if not is_valid_professor(
                    final_record
                ):

                    failed_count += 1

                    print(
                        "INVALID RECORD - SKIPPED"
                    )

                    continue

                professor_name = (
                    final_record.get(
                        "name",
                        ""
                    )
                    .strip()
                    .lower()
                )

                professor_email = (
                    final_record.get(
                        "email",
                        ""
                    )
                    .strip()
                    .lower()
                )

                # ----------------------------------------
                # DUPLICATE NAME CHECK
                # ----------------------------------------

                if (
                    professor_name
                    in processed_names
                ):

                    duplicate_count += 1

                    print(
                        f"DUPLICATE PROFESSOR: "
                        f"{final_record.get('name')}"
                    )

                    continue

                # ----------------------------------------
                # DUPLICATE EMAIL CHECK
                # ----------------------------------------

                if (
                    professor_email
                    in processed_emails
                ):

                    duplicate_count += 1

                    print(
                        f"DUPLICATE EMAIL: "
                        f"{professor_email}"
                    )

                    continue

                processed_names.add(
                    professor_name
                )

                processed_emails.add(
                    professor_email
                )

                all_profiles.append(
                    final_record
                )

                saved_count += 1

                print(
                    f"SUCCESS: "
                    f"{final_record.get('name')}"
                )

                print(
                    f"EMAIL: "
                    f"{final_record.get('email')}"
                )

                print(
                    f"SCORE: "
                    f"{score}"
                )

                print(
                    f"TOTAL SAVED: "
                    f"{saved_count}"
                )

            except Exception as e:

                failed_count += 1

                print(
                    f"FAILED PROFILE: {link}"
                )

                print(f"ERROR: {e}")

        browser.close()

    print("\n" + "=" * 80)

    print("CRAWL SUMMARY")

    print("=" * 80)

    print(
        f"University: "
        f"{university_name}"
    )

    print(
        f"Total Links Found: "
        f"{len(unique_links)}"
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
        f"Profiles Failed: "
        f"{failed_count}"
    )

    print(
        f"Duplicates Skipped: "
        f"{duplicate_count}"
    )

    print("=" * 80)

    return all_profiles