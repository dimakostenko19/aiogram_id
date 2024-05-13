import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import CommandStart

from telethon import errors
from telethon import TelegramClient

from api import api_id, api_hash, TOKEN

client = TelegramClient('anon', api_id, api_hash)


dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_help(message: types.Message):
    await message.answer('Enter @username to get ID')

async def get_user(username):
    user_id = await client.get_entity(username)
    return user_id

@dp.message()
async def get_msg(message: types.Message):
    msg = message.text
    try:
        if(msg.startswith('@') and len(msg)>=6):
            user = await get_user(msg)
            await message.answer(f'User ID {msg}: {str(user.id)}')
   
        elif(msg.startswith('@') and len(msg)<6):
            await message.answer('The length must be more than 5 characters')
        elif(not msg.startswith('@')):
            await message.answer('Username must begin with @')

    except ValueError:
       await message.answer('User not found')

    except UnboundLocalError:
        await message.answer('User not found')
    
    except errors.rpcerrorlist.UsernameInvalidError:
       await message.answer('User not found')



async def main():
    await client.start()
    bot = Bot(token=TOKEN)
    
    await dp.start_polling(bot)


if __name__=='__main__':
    asyncio.run(main())