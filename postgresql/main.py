import asyncio
from prisma import Prisma

async def main() -> None:
    prisma = Prisma()
    await prisma.connect()

    # write your queries here
    # users = await prisma.query_raw('SELECT * FROM User WHERE id = ?', 836760821,)
    users = await prisma.query_raw('SELECT * FROM public.user')

    print(users)
    
    await prisma.disconnect()

if __name__ == '__main__':
    asyncio.run(main())