import re
import requests

from bs4 import BeautifulSoup

from urllib.parse import (
    urljoin
)

from app.crawler.pdf_extractor import (
    extract_pdf_text
)


EMAIL_REGEX = (
    r"[A-Za-z0-9._%+-]+"
    r"@[A-Za-z0-9.-]+"
    r"\.[A-Za-z]{2,}"
)


def extract_email_from_text(text):

    matches = re.findall(
        EMAIL_REGEX,
        text
    )

    if matches:

        return matches[0]

    return None


def extract_email(soup, html):

    # ----------------------------------------
    # MAILTO LINKS
    # ----------------------------------------

    mailto_links = soup.select(
        'a[href^="mailto:"]'
    )

    for link in mailto_links:

        href = link.get("href", "")

        email = href.replace(
            "mailto:",
            ""
        ).strip()

        if email:

            return email

    # ----------------------------------------
    # RAW HTML EXTRACTION
    # ----------------------------------------

    email = extract_email_from_text(
        html
    )

    if email:

        return email

    # ----------------------------------------
    # OBFUSCATED EMAILS
    # ----------------------------------------

    cleaned_html = (

        html
        .replace(" [at] ", "@")
        .replace(" (at) ", "@")
        .replace(" at ", "@")
        .replace(" [dot] ", ".")
        .replace(" (dot) ", ".")
        .replace(" dot ", ".")
    )

    email = extract_email_from_text(
        cleaned_html
    )

    if email:

        return email

    return None


def crawl_personal_website(url):

    try:

        response = requests.get(

            url,

            timeout=20,

            headers={
                "User-Agent":
                "Mozilla/5.0"
            }
        )

        html = response.text

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        # ----------------------------------------
        # DIRECT EMAIL
        # ----------------------------------------

        email = extract_email(
            soup,
            html
        )

        if email:

            return email, None

        # ----------------------------------------
        # CV / BIO DISCOVERY
        # ----------------------------------------

        for a in soup.find_all(
            "a",
            href=True
        ):

            href = a["href"]

            href_lower = href.lower()

            if any(keyword in href_lower for keyword in [

                "cv",

                "resume",

                "vita",

                "bio",

                ".pdf"
            ]):

                full_url = urljoin(
                    url,
                    href
                )

                return None, full_url

    except Exception as e:

        print(
            f"PERSONAL WEBSITE "
            f"CRAWL FAILED: {url}"
        )

        print(e)

    return None, None


def extract_links(soup, profile_url):

    linkedin = None

    scholar = None

    resume_url = None

    personal_website = None

    for a in soup.find_all(
        "a",
        href=True
    ):

        href = a["href"]

        href_lower = href.lower()

        # ----------------------------------------
        # NORMALIZE RELATIVE URLS
        # ----------------------------------------

        full_url = urljoin(
            profile_url,
            href
        )

        # ----------------------------------------
        # LINKEDIN
        # ----------------------------------------

        if (
            "linkedin.com"
            in href_lower
        ):

            linkedin = full_url

        # ----------------------------------------
        # GOOGLE SCHOLAR
        # ----------------------------------------

        if (
            "scholar.google"
            in href_lower
        ):

            scholar = full_url

        # ----------------------------------------
        # PERSONAL WEBSITE
        # ----------------------------------------

        if any(keyword in href_lower for keyword in [

            "personal",

            "homepage",

            "website"
        ]):

            personal_website = full_url

        # ----------------------------------------
        # RESUME / CV
        # ----------------------------------------

        if any(keyword in href_lower for keyword in [

            "cv",

            "resume",

            "vita",

            ".pdf"
        ]):

            resume_url = full_url

    return (

        linkedin,

        scholar,

        resume_url,

        personal_website
    )


def extract_summary(soup):

    paragraphs = soup.find_all("p")

    summary_parts = []

    for p in paragraphs[:20]:

        text = p.get_text(
            " ",
            strip=True
        )

        if len(text) > 40:

            summary_parts.append(text)

    return "\n".join(summary_parts)


def parse_profile(profile_url, html):

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    # ----------------------------------------
    # DIRECT EMAIL EXTRACTION
    # ----------------------------------------

    email = extract_email(
        soup,
        html
    )

    # ----------------------------------------
    # EXTRACT LINKS
    # ----------------------------------------

    (
        linkedin,
        scholar,
        resume_url,
        personal_website
    ) = extract_links(

        soup,

        profile_url
    )

    # ----------------------------------------
    # PERSONAL WEBSITE CRAWL
    # ----------------------------------------

    if not email and personal_website:

        print(
            "Attempting personal website crawl..."
        )

        personal_email, discovered_cv = (
            crawl_personal_website(
                personal_website
            )
        )

        if personal_email:

            email = personal_email

        if discovered_cv and not resume_url:

            resume_url = discovered_cv

    # ----------------------------------------
    # SUMMARY
    # ----------------------------------------

    summary = extract_summary(
        soup
    )

    # ----------------------------------------
    # RESUME PDF EXTRACTION
    # ----------------------------------------

    resume_text = ""

    if resume_url:

        try:

            print(
                f"Extracting CV: "
                f"{resume_url}"
            )

            resume_text = extract_pdf_text(
                resume_url
            )

            # ----------------------------------------
            # EMAIL FROM PDF
            # ----------------------------------------

            if not email:

                pdf_email = (
                    extract_email_from_text(
                        resume_text
                    )
                )

                if pdf_email:

                    email = pdf_email

                    print(
                        f"Email discovered "
                        f"from CV: {email}"
                    )

        except Exception as e:

            print(
                f"PDF EXTRACTION FAILED: "
                f"{resume_url}"
            )

            print(e)

    return {

        "email": email,

        "linkedin": linkedin,

        "scholar": scholar,

        "resume_url": resume_url,

        "personal_website": personal_website,

        "summary": summary,

        "resume_text": resume_text
    }