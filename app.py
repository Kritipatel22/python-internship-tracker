# app.py
# Main entry point for Internship & Job Application Tracker
import csv

from datetime import datetime

import logging

logging.basicConfig(
    filename="tracker.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

from colorama import Fore, Style, init
init(autoreset=True)

import db
from db import get_connection
from tabulate import tabulate

def add_application():
    while True:
        title = input("Enter internship/job title: ").strip()
        if title:
            break
        print(Fore.RED + "❌ Title cannot be empty.")

    while True:
        company = input("Enter company name: ").strip()
        if company:
            break
        print(Fore.RED + "❌ Company cannot be empty.")

    status = input("Enter status (Applied/Interview/Rejected/Selected): ")
    valid_status = ["Applied", "Interview", "Selected", "Rejected"]

    while True:
        status = input("Enter status (Applied/Interview/Rejected/Selected): ").strip()
        if status in valid_status:
            break
        print(Fore.RED + "❌ Invalid status. Choose from: Applied, Interview, Selected, Rejected")

    while True:
        deadline = input("Enter deadline (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
            break
        except ValueError:
            print(Fore.RED + "❌ Invalid date format. Use YYYY-MM-DD.")

    link = input("Enter application link: ")
    notes = input("Enter notes: ")
    

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO applications (title, company, status, deadline, link, notes)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    
    cursor.execute(query, (title, company, status, deadline, link, notes))
    conn.commit()
    logging.info(f"Added application: {title} at {company}")
    
    print(Fore.GREEN + "✔ Application added successfully!")


def view_applications():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM applications")
    results = cursor.fetchall()

    if results:
        print("\n📌 All Applications:\n")
        print(tabulate(results, headers=[
            "ID", "Title", "Company", "Status", "Deadline", "Link", "Notes"
        ], tablefmt="grid"))
    else:
       print(Fore.YELLOW + "⚠ No results found.")


def update_status():
    while True:
        app_id = input("Enter application ID to update: ").strip()
        if app_id.isdigit():
            app_id = int(app_id)
            break
        print(Fore.RED + "❌ ID must be a number.")

    new_status = input("Enter new status: ")

    conn = get_connection()
    cursor = conn.cursor()

    query = "UPDATE applications SET status = %s WHERE id = %s"
    cursor.execute(query, (new_status, app_id))
    conn.commit()
    logging.info(f"Updated application ID {app_id} to status: {new_status}")


    print(Fore.GREEN + "\n🔄 Status updated successfully!\n")

def delete_application():
    while True:
        app_id = input("Enter application ID to delete: ").strip()
        if app_id.isdigit():
            app_id = int(app_id)
            break
        print(Fore.RED + "❌ ID must be a number.")


    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM applications WHERE id = %s"
    cursor.execute(query, (app_id,))
    conn.commit()
    logging.info(f"Deleted application ID {app_id}")


    print(Fore.GREEN + "\n🗑 Application deleted successfully!\n")

def print_table(data):
    if not data:
        print(Fore.YELLOW + "\n⚠ No results found.\n")
        return

    headers = [
        Fore.CYAN + "ID" + Style.RESET_ALL,
        Fore.CYAN + "Title" + Style.RESET_ALL,
        Fore.CYAN + "Company" + Style.RESET_ALL,
        Fore.CYAN + "Status" + Style.RESET_ALL,
        Fore.CYAN + "Deadline" + Style.RESET_ALL,
        Fore.CYAN + "Link" + Style.RESET_ALL,
        Fore.CYAN + "Notes" + Style.RESET_ALL,
    ]

    print("\n" + tabulate(data, headers=headers, tablefmt="grid") + "\n")

def show_summary():
    total, applied, interview, selected, rejected = db.get_summary()

    print("\n📊 APPLICATION SUMMARY\n")
    print(f"Total Applications:   {total}")
    print(f"Applied:              {applied}")
    print(f"Interview:            {interview}")
    print(f"Selected:             {selected}")
    print(f"Rejected:             {rejected}\n")

def export_to_csv():
    data = db.get_all_applications()
    
    if not data:
        print(Fore.YELLOW + "⚠ No data available to export.")
        return

    headers = ["ID", "Title", "Company", "Status", "Deadline", "Link", "Notes"]

    with open("applications_export.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

    print(Fore.GREEN + "✔ Data exported successfully to 'applications_export.csv'")

    logging.info("Exported all applications to CSV.")


def menu():
    while True:
        print(Fore.CYAN + "\n🎯 Internship & Job Application Tracker\n" + Style.RESET_ALL)
        print("1. Add new application")
        print("2. View all applications")
        print("3. Update application status")
        print("4. Delete application")
        print("5. Search applications by company")
        print("6. Search applications by status")
        print("7. Search applications by title keyword")
        print("8. Sort applications by deadline")
        print("9. Sort applications by company")
        print("10. Sort applications by status")
        print("11. View dashboard summary")
        print("12. Export all applications to CSV")
        print("13. Exit")


        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_application()
        elif choice == "2":
            view_applications()
        elif choice == "3":
            update_status()
        elif choice == "4":
            delete_application()
        elif choice == "5":
            company = input("Enter company name to search: ")
            results = db.search_by_company(company)
            print_table(results)

        elif choice == "6":
            status = input("Enter status to search (Applied/Interview/Rejected/etc): ")
            results = db.search_by_status(status)
            print_table(results)

        elif choice == "7":
            keyword = input("Enter title keyword (e.g., Python, Developer, Intern): ")
            results = db.search_by_title(keyword)
            print_table(results)
        elif choice == "8":
            results = db.sort_by_deadline()
            print_table(results)

        elif choice == "9":
            results = db.sort_by_company()
            print_table(results)

        elif choice == "10":
            results = db.sort_by_status()
            print_table(results)
        elif choice == "11":
            show_summary()
        elif choice == "12":
            export_to_csv()
        elif choice == "13":
            print(Fore.GREEN + "Goodbye!")
            break
        else:
           print(Fore.RED + "✘ Invalid choice.")


if __name__ == "__main__":
    menu()
