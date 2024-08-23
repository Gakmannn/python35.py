import asyncio
from prisma import Prisma

async def main() -> None:
    prisma = Prisma()
    await prisma.connect()

    # write your queries here
    # users = await prisma.query_raw('SELECT * FROM User WHERE id = ?', 836760821,)
    # users = await prisma.query_raw('INSERT INTO user(name, email) VALUES (?,?)', 'user1', 'dsfsd1@dfs.ru',)
    # users = await prisma.query_raw('INSERT INTO user(email, name) VALUES (?,?)', 'dsfsd2@dfs.ru', 'user2',)
    # users = await prisma.query_raw('INSERT INTO user(email, name) VALUES (?,?)', 'dsfsd3@dfs.ru', 'user3',)
    # users = await prisma.query_raw('INSERT INTO user(email, name) VALUES (?,?)', 'dsfsd4@dfs.ru', 'user4',)
    # users = await prisma.query_raw('INSERT INTO user VALUES (?,?)', 'dsfsd41@dfs.ru', 'user4',)
    
    
    # users = await prisma.query_raw('''
    #                                 UPDATE user
    #                                 SET name='user41'
    #                                 WHERE id=5
    #                                 ''')
    # users = await prisma.query_raw('''
    #                                 DELETE FROM user
    #                                 WHERE id=5
    #                                 ''')
    
    # users = await prisma.query_raw("SELECT * FROM user WHERE NOT name='user4' ORDER BY id desc LIMIT 1,3;")
    # users = await prisma.query_raw("SELECT * FROM user WHERE name LIKE '%er3%';")
    users = await prisma.query_raw('''SELECT *
                                   FROM user 
                                   ORDER BY name desc 
                                   ''')

    # u = await prisma.user.find_many(
    #     include={
    #         'posts':True
    #     }
    # )

    print(users)
    
    await prisma.disconnect()

if __name__ == '__main__':
    asyncio.run(main())