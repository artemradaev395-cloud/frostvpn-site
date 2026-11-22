from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()
SUPPORT_URL = "https://t.me/frost3920201"

PLANS = [
    ("1 месяц", "149 ₽"),
    ("3 месяца", "399 ₽"),
    ("6 месяцев", "699 ₽"),
    ("12 месяцев", "1 190 ₽"),
]

def main_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text="❄️ Купить VPN", callback_data="buy")
    kb.button(text="📦 Моя подписка", callback_data="subscription")
    kb.button(text="💬 Поддержка", url=SUPPORT_URL)
    kb.button(text="ℹ️ О проекте", callback_data="about")
    kb.adjust(1)
    return kb.as_markup()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "❄️ <b>BEW FROSTVPN</b>\nТвой VPN. Твой выбор.\n\n"
        "Выбери нужный раздел в меню ниже.",
        reply_markup=main_keyboard(),
        parse_mode="HTML",
    )

@router.callback_query(F.data == "buy")
async def buy(callback: CallbackQuery):
    lines = ["<b>Тарифы BEW FROSTVPN</b>"]
    lines.extend(f"• {name} — <b>{price}</b>" for name, price in PLANS)
    lines.append("\nПокупка пока отключена: это демонстрационный прототип.")
    await callback.message.answer("\n".join(lines), parse_mode="HTML")
    await callback.answer()

@router.callback_query(F.data == "subscription")
async def subscription(callback: CallbackQuery):
    await callback.message.answer("Проверка подписки пока не подключена — это демо-версия.")
    await callback.answer()

@router.callback_query(F.data == "about")
async def about(callback: CallbackQuery):
    await callback.message.answer(
        "BEW FROSTVPN — демонстрационный интерфейс VPN-магазина.\n"
        "Тёмный ледяной стиль, синие акценты и слоган «Твой VPN. Твой выбор.»"
    )
    await callback.answer()
