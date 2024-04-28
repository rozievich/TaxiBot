from aiogram.fsm.state import StatesGroup, State


class SendMessageState(StatesGroup):
    text = State()
