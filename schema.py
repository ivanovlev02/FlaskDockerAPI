import pydantic
from typing import Optional, Type  # возможность опционального выбора поля при обновлении данных.
from errors import HttpError
from typing import Type, Union


# проверяет значения словаря json, полученного из запроса.
def validate(
        json_data: dict,
        model_class: Type[Union['CreateUser', 'UpdateUser', 'CreateAdvertisement', 'UpdateAdvertisement']]
            ):

    try:
        model_item = model_class(**json_data)  # создаем экземпляр принимаемого класса.
        return model_item.dict(exclude_none=True)  # возвращаем словарь с параметрами созданного класса
    except pydantic.ValidationError as error:
        raise HttpError(400, error.errors())  # т.к. на вход требуется словарь, то error.errors() - метод pydantic,
        # который создает словарь с описанием ошибок самостоятельно.


# Валидация данных при создании пользователя. Проверки на тип данных и длину значения
class CreateUser(pydantic.BaseModel):
    name: str
    user_pass: str

# Проверка на длину пароля.
    @pydantic.validator('name')
    def validate_name(cls, value):
        if len(value) > 50:
            raise ValueError('Name is too big')
        return value

# Проверка на длину пароля.
    @pydantic.validator('user_pass')
    def validate_password(cls, value):

        if len(value) < 8:
            raise ValueError('password is too short')
        if len(value) > 100:
            raise ValueError('password is too big')
        return value


# Валидация данных при обновлении пользователя. Проверки на тип данных и длину значения
class UpdateUser(pydantic.BaseModel):
    name: Optional[str]
    user_pass: Optional[str]

# Проверка на длину пароля.
    @pydantic.validator('user_pass')
    def validate_password(cls, value):

        if len(value) < 8:
            raise ValueError('password is too short')
        if len(value) > 100:
            raise ValueError('password is too big')
        return value


# Валидация данных при создании объявления.
class CreateAdvertisement(pydantic.BaseModel):
    header: str
    desc: Optional[str]
    owner_id: int


# Валидация данных при обновлении объявления.
class UpdateAdvertisement(pydantic.BaseModel):
    header: str
    desc: Optional[str]
