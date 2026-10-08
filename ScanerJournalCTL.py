import json
import re

file_path = "C:/Users/1/Downloads/journal.jsonl"

# Список для хранения связанных пар (IP, Логин)
connections = []
a = 0

# Регулярные выражения
ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
user_pattern = r"Failed password for (?:invalid user )?(\S+)"

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        if not line.strip():
            continue

        try:
            log_entry = json.loads(line)
            content = log_entry.get("MESSAGE", "")

            if "Failed password" in content:
                a += 1

                # Ищем IP и логин в текущей строке
                ip_match = re.search(ip_pattern, content)
                user_match = re.search(user_pattern, content)

                # Если нашли и то, и другое — связываем их
                if ip_match and user_match:
                    ip = ip_match.group(0)
                    login = user_match.group(1)
                    
                    # Добавляем кортеж (ip, login) в общий список
                    connections.append((ip, login))
                    
                    # Красивый сопоставленный вывод
                    print(f"Попытка входа: IP {ip:<15} ---> Логин: {login}")

        except json.JSONDecodeError:
            continue

print("\n--- ИТОГО ---")
print(f"Всего зафиксировано строк с ошибками: {a}")
print(f"Успешно сопоставлено пар (IP - Логин): {len(connections)}")
