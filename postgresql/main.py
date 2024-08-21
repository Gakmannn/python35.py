import asyncio
from prisma import Prisma

async def main() -> None:
    prisma = Prisma()
    await prisma.connect()

    # write your queries here
    # users = await prisma.query_raw('SELECT * FROM User WHERE id = ?', 836760821,)
    # users = await prisma.query_raw('INSERT INTO user(email, name) VALUES (?,?)', 'dsfsd1@dfs.ru', 'user1',)
    # users = await prisma.query_raw('INSERT INTO user(email, name) VALUES (?,?)', 'dsfsd2@dfs.ru', 'user2',)
    # users = await prisma.query_raw('INSERT INTO user(email, name) VALUES (?,?)', 'dsfsd3@dfs.ru', 'user3',)
    # users = await prisma.query_raw('INSERT INTO user(email, name) VALUES (?,?)', 'dsfsd4@dfs.ru', 'user4',)
    # users = await prisma.query_raw('INSERT INTO user(email, name) VALUES (?,?)', 'dsfsd41@dfs.ru', 'user4',)
    
    
    # users = await prisma.query_raw("SELECT * FROM user WHERE NOT name='user4' ORDER BY id desc;")
    users = await prisma.query_raw("SELECT * FROM user WHERE name LIKE '%er3%';")

    print(users)
    
    await prisma.disconnect()

if __name__ == '__main__':
    asyncio.run(main())