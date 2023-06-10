import json
import os
import datetime

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            notes = json.load(file)
            return notes
    else:
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    
    notes.append(note)
    save_notes(notes)
    
    print("Заметка успешно сохранена.")

def read_note():
    note_id = int(input("Введите ID заметки: "))
    
    for note in notes:
        if note["id"] == note_id:
            print("ID: ", note["id"])
            print("Заголовок: ", note["title"])
            print("Тело: ", note["body"])
            print("Дата/время: ", note["timestamp"])
            return
    
    print("Заметка с указанным ID не найдена.")

def update_note():
    note_id = int(input("Введите ID заметки, которую нужно обновить: "))
    
    for note in notes:
        if note["id"] == note_id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новое тело заметки: ")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            note["title"] = title
            note["body"] = body
            note["timestamp"] = timestamp
            
            save_notes(notes)
            
            print("Заметка успешно обновлена.")
            return
    
    print("Заметка с указанным ID не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки, которую нужно удалить: "))
    
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            
            print("Заметка успешно удалена.")
            return
    
    print("Заметка с указанным ID не найдена.")

notes = load_notes()

while True:
    print("Введите команду (add, read, update, delete, exit):")
    command = input()
    
    if command == "add":
        add_note()
    elif command == "read":
        read_note()
    elif command == "update":
        update_note()
    elif command == "delete":
        delete_note()
    elif command == "exit":
        print("Программа завершена.")
        break
    else:
        print("Неверная команда. Попробуйте снова.")