from aiogram.fsm.state import State, StatesGroup



class AddTaxiState(StatesGroup):
    fullname = State()
    phone = State()
    photo = State()
    username = State()
    description = State()


class DeleteTaxiState(StatesGroup):
    fullname = State()


class UpdateTopState(StatesGroup):
    fullname = State()


class UpdateBackTopState(StatesGroup):
    fullname = State()
