from aiogram import types, Router
from aiogram.filters import and_f

from . import add_taxi_func

admin_router = Router()


# Add Taxi functions register to router
admin_router.message.register(add_taxi_func.add_taxi_function, TextFilter("Taxi Qo'shish 🚕"))
admin_router.message.register(add_taxi_func.add_taxi_function_phone, AddTaxiState.fullname)
admin_router.message.register(add_taxi_func.add_taxi_function_photo, AddTaxiState.phone)
admin_router.message.register(add_taxi_func.add_taxi_function_username, and_f(AddTaxiState.photo, types.ContentType.PHOTO))
admin_router.message.register(add_taxi_func.add_taxi_function_description, AddTaxiState.username)
admin_router.message.register(add_taxi_func.add_taxi_function_finish, AddTaxiState.description)


# Delete Taxi functions register to router

