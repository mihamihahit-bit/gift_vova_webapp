import random


START_BALANCE = 1000
BET = 10


def play_game(game: str, balance: int) -> int:
    if balance < BET:
        print(f"\nНедостаточно монет. Баланс: {balance} 🪙")
        return balance

    balance -= BET

    if game == "plane":
        multiplier = round(random.uniform(0, 3), 2)

        if multiplier >= 1.5:
            payout = int(BET * multiplier)
            balance += payout
            result = f"✈️ Самолёт улетел на x{multiplier}. Выплата: {payout} 🪙"
        else:
            result = f"✈️ Самолёт улетел на x{multiplier}. Ставка потеряна."

    elif game == "plinko":
        multiplier = random.choice([0, 0.5, 1, 2, 5])
        payout = int(BET * multiplier)
        balance += payout
        result = f"🔵 Выпал коэффициент x{multiplier}. Выплата: {payout} 🪙"

    elif game == "upgrade":
        if random.random() < 0.45:
            payout = BET * 2
            balance += payout
            result = f"⬆️ Апгрейд успешен! Выплата: {payout} 🪙"
        else:
            result = "⬆️ Апгрейд не удался. Ставка потеряна."

    elif game == "contract":
        if random.random() < 0.5:
            payout = BET * 2
            balance += payout
            result = f"📜 Контракт выполнен! Выплата: {payout} 🪙"
        else:
            result = "📜 Контракт провален. Ставка потеряна."

    elif game == "pvp":
        if random.random() < 0.5:
            payout = BET * 2
            balance += payout
            result = f"⚔️ Ты победил бота! Выплата: {payout} 🪙"
        else:
            result = "⚔️ Бот победил. Ставка потеряна."

    else:
        print("Неизвестная игра.")
        return balance

    print(f"\n{result}")
    print(f"Баланс: {balance} 🪙")
    return balance


def main() -> None:
    balance = START_BALANCE

    print("🎁 Gift Vova")
    print("Демо-игра на виртуальные монеты — без пополнения и вывода денег.")

    while True:
        print(
            "\nВыберите действие:\n"
            "1 — ✈️ Plane\n"
            "2 — 🔵 Plinko\n"
            "3 — ⬆️ Апгрейд\n"
            "4 — 📜 Контракт\n"
            "5 — ⚔️ PvP против бота\n"
            "6 — 💰 Баланс\n"
            "0 — Выход"
        )

        choice = input("Ваш выбор: ").strip()

        games = {
            "1": "plane",
            "2": "plinko",
            "3": "upgrade",
            "4": "contract",
            "5": "pvp",
        }

        if choice in games:
            balance = play_game(games[choice], balance)
        elif choice == "6":
            print(f"\nТвой баланс: {balance} 🪙")
        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("Введите число от 0 до 6.")


if __name__ == "__main__":
    main()
