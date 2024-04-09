from aiogram import Router, types, F
from aiogram.client import bot
from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from handlers.keyboards.start_keyboard import get_location_kb, COMBO_get_many_AND_give_wedSite, status_water, \
    status_dump, resize_dump, no_photo

user_router = Router()

#база данных свалок
dumpFile = open("database_springs.db", "r")
dumpdump = set ()
for line in dumpFile:
    dumpdump.add(line.strip())
#база данных родников
joinedFile = open("database_springs.db", "r")
joinedUsers = set ()
for line in joinedFile:
    joinedUsers.add(line.strip())


# Обработчик команды /start
@user_router.message(Command('start')) #Перезагрузить
async def start(message: types.Message, state: FSMContext) -> None:
    text = 'Привет! Этот бот поможет вам добавлять данные о родниках и свалках.'

    Cg = COMBO_get_many_AND_give_wedSite()
    user_id = message.from_user.id

    await message.answer(text, reply_markup=Cg)

@user_router.message(Command('support')) #Поддержка
async def support(message: types.Message, state: FSMContext) -> None:
    await message.answer('Опишите свою проблему: ')
    await state.set_state(Form.support_listener)



@user_router.message(F.text == "Добавить новый родник 🚰")
async def site(message: types.Message, state: FSMContext) -> None:
    if message.text == 'Добавить новый родник 🚰':
        await message.answer('Введите название родника, который хотите добавить\nПример: Святой источник', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(Form.text)

@user_router.message(F.text == "Добавить новую свалку мусора 🗑️")
async def site(message: types.Message, state: FSMContext) -> None:
    if message.text == 'Добавить новую свалку мусора 🗑️':
        await message.answer('Введите название свалки, которую хотите добавить\nПример: Свалка у Азовского моря', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(Form.text_dump)










class Form(StatesGroup):
    text = State()
    photo = State()
    no_photo = State()
    location = State()
    tags = State()
    description = State()
    status = State()
    resize_dump = State()
    text_dump = State()
    description_dump = State()
    photo_dump = State()
    no_photo_dump = State()
    status_dump = State()
    tags_dump = State()
    support_listener = State()

admin_id = 989926239
@user_router.message(Form.support_listener, F.content_type == ContentType.TEXT)
async def send_message(message: types.Message, state: FSMContext) -> None:
    await state.update_data(report_message=message.text)
    report_data = await state.get_data()
    report_message = report_data['report_message']

    print(report_message)





@user_router.message(Form.text_dump, F.content_type == ContentType.TEXT)
async def photo_received(message: types.Message, state: FSMContext):
    await state.update_data(name_dump=message.text)
    user_data = await state.get_data()
    a = user_data['name_dump']
    print(a)
    kb = get_location_kb()
    await message.answer("Теперь отправьте локацию свалки\nили отправьте свою геолокацию, если находитесь рядом с ней.", reply_markup=kb)



    # Set state
    await state.set_state(Form.description_dump)

@user_router.message(Form.description_dump, F.content_type == ContentType.LOCATION)
async def photo_received(message: types.Message, state: FSMContext):
    await state.update_data(location_dump=(message.location.longitude, message.location.latitude))
    user_data = await state.get_data()
    b = user_data['location_dump']
    print(b)
    Cg = COMBO_get_many_AND_give_wedSite()
    await message.answer("Напишите описание найденной свалки.", reply_markup=types.ReplyKeyboardRemove())

    await state.set_state(Form.photo_dump)


@user_router.message(Form.photo_dump, F.content_type == ContentType.TEXT)
async def photo_received(message: types.Message, state: FSMContext):
    await state.update_data(description_dump=message.text)
    user_data = await state.get_data()
    c = user_data['description_dump']
    print(c)

    await message.answer("Теперь отправьте фото свалки.")

    await state.set_state(Form.status_dump)


@user_router.message(Form.status_dump, F.content_type == ContentType.PHOTO)
async def photo_received(message: types.Message, state: FSMContext):
    print(message.photo)
    await state.update_data(photo_dump=message.photo[-1].file_id)

    user_data = await state.get_data()
    d = user_data['photo_dump']
    print(d)
    SD = status_dump()
    await message.answer("Выберете тип мусора.", reply_markup=SD)
    # Set state
    await state.set_state(Form.tags_dump)




@user_router.message(Form.tags_dump, F.content_type == ContentType.TEXT)
async def tags_received(message: types.Message, state: FSMContext):
    await state.update_data(status_dump=message.text)
    RD = resize_dump()
    user_data = await state.get_data()
    e = user_data['status_dump']
    await message.answer('Выберете размер свалки.', reply_markup=RD)
    await state.set_state(Form.resize_dump)

@user_router.message(Form.resize_dump, F.content_type == ContentType.TEXT)
async def tags_received(message: types.Message, state: FSMContext):
    await state.update_data(resize_dump=message.text)

    user_data = await state.get_data()
    e = user_data['resize_dump']
    print(e)
    Cg = COMBO_get_many_AND_give_wedSite()

    print(user_data)
    a = user_data['name_dump']
    b = user_data['location_dump']
    c = user_data['description_dump']
    d = user_data['photo_dump']
    e = user_data['status_dump']
    f = user_data['resize_dump']

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)

    if f == 'Очень большая (> 16га) 🟣':
        f = 'Больше 16га'
    else:
        if f == 'Большая (12-16га) 🔴':
            f = '12-16га'
        else:
            if f == 'Средняя (8-12га) 🟡':
                f = '8-12га'
            else:
                if f == 'Небольшая (4-8га) 🟢':
                    f = '4-8га'
                else:
                    if f == 'Мелкая (< 4га) ✅':
                        f = 'Меньше 4га'
                    else:
                        f = f
    photo = user_data['photo_dump']
    full_dump_report = 'dump[1] = ' + str(a) + '\ndump[2] ' + str(b) + '\ndump[3] = ' + str(c) + '\ndump[4] =  ' + str(e) + '\ndump[5] =  ' + str(f)

    await message.answer('<b>Информация о свалке:</b>\nНазвание: ' + str(a) + '\nЛокация: ' + str(b) + '\nОписание: ' + str(c) + '\nТип мусора: ' + str(e) + '\nРазмер: ' + str(f), parse_mode='html')
    print(full_dump_report)
    if not str(full_dump_report) in dumpdump:
        dumpFile = open("database_dumps.db", "w+")
    dumpFile.write(str(full_dump_report) + "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n")
    dumpdump.add(full_dump_report)
    await message.answer(f"Свалка отправлена на верификацию ✅\nпока ждёшь верификацию свалки загляни на сайт проекта нажав на кнопку ниже", reply_markup=Cg)

    await message.answer("И кстати поддержи нас денюжкой нажав на кнопку ниже")

    print(user_data)
    a = user_data['name_dump']
    b = user_data['location_dump']
    c = user_data['description_dump']
    d = user_data['photo_dump']
    e = user_data['status_dump']

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    # Reset state
    user_data.clear()
    await state.clear()


@user_router.message(Form.text, F.content_type == ContentType.TEXT)
async def photo_received(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    user_data = await state.get_data()
    kb = get_location_kb()

    await message.answer("Теперь отправьте локацию родника\nили отправьте свою геолокацию, если находитесь рядом с ним.", reply_markup=kb)



    # Set state
    await state.set_state(Form.description)




@user_router.message(Form.description, F.content_type == ContentType.LOCATION)
async def photo_received(message: types.Message, state: FSMContext):
    await state.update_data(location=(message.location.longitude, message.location.latitude))
    user_data = await state.get_data()
    Cg = COMBO_get_many_AND_give_wedSite()
    await message.answer("Напишите описание найденного родника.", reply_markup=types.ReplyKeyboardRemove())

    await state.set_state(Form.photo)

@user_router.message(Form.photo, F.content_type == ContentType.TEXT)
async def photo_received(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    user_data = await state.get_data()
    c = user_data['description']
    print(c)
    NP = no_photo()
    await message.answer("Теперь отправьте фото родника.")
    await state.set_state(Form.status)

@user_router.message(Form.status, F.content_type == ContentType.PHOTO)
async def photo_received(message: types.Message, state: FSMContext):
    print(message.photo)
    await state.update_data(photo=message.photo[-1].file_id)

    user_data = await state.get_data()
    d = user_data['photo']
    print(d)
    SW = status_water()
    await message.answer("Выберете статус ухоженности родника.", reply_markup=SW)
    # Set state
    await state.set_state(Form.tags)


@user_router.message(Form.tags, F.content_type == ContentType.TEXT)
async def tags_received(message: types.Message, state: FSMContext):
    await state.update_data(status=message.text)

    user_data = await state.get_data()
    Cg = COMBO_get_many_AND_give_wedSite()





    print(user_data)
    a = user_data['name']
    b = user_data['location']
    c = user_data['description']
    d = user_data['photo']
    e = user_data['status']

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


    full_spring_report = 'spring[1] = ' + str(a) + '\nspring[2] = ' + str(b) + '\nspring[3] = ' + str(c) + '\nspring[4] = ' + str(d) + '\nspring[5] = ' + str(e)

    await message.answer('<b>Информация о роднике:</b>\nНазвание: ' + str(a) + '\nЛокация: ' + str(b) + '\nОписание: ' + str(c) + '\nСтатус: ' + str(e), parse_mode='html')
    print(full_spring_report)
    if not str(full_spring_report) in joinedUsers:
        joinedFile = open("database_springs.db", "w+")
    joinedFile.write(str(full_spring_report) + "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n")
    joinedUsers.add(full_spring_report)
    await message.answer(f"Родник отправлен на верификацию ✅\nпока ждёшь верификацию родника загляни на сайт проекта нажав на кнопку ниже", reply_markup=Cg)

    await message.answer("И кстати поддержи нас денюжкой нажав на кнопку ниже")

    print(user_data)
    a = user_data['name']
    b = user_data['location']
    c = user_data['description']
    d = user_data['photo']
    e = user_data['status']

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    # Reset state
    user_data.clear()
    await state.clear()


