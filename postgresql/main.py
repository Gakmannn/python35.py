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
    # users = await prisma.query_raw('''SELECT *
    #                                FROM user 
    #                                ORDER BY name desc 
    #                                ''')

    # u = await prisma.user.find_many(
    #     include={
    #         'posts':True
    #     }
    # )
    
    
    # users = await prisma.query_raw('''
    #                                SELECT *
    #                                FROM teachers as t
    #                                INNER JOIN kafedra as k
    #                                ON k.id=t.kafedra_id
    #                                ORDER BY name asc 
    #                                ''')
                                #    WHERE k.name=?
    
    # users = await prisma.query_raw('''
    #                                SELECT t.id, u.name as univer, k.name as kafedra, k.tel, t.first_name, t.last_name
    #                                FROM univer as u, kafedra as k, teachers as t 
    #                                WHERE k.univer_id=u.id AND t.kafedra_id=k.id
    #                                ''')

    # users = await prisma.query_raw('''
    #                                SELECT AVG(id) as avg, COUNT(*) as num, MIN(first_name), MAX(first_name), SUM(id)
    #                                FROM teachers
    #                                WHERE kafedra_id=1
    #                                ''')
    
    # users = await prisma.query_raw('''
    #                                SELECT COUNT(*) as num_of_pair, first_name
    #                                FROM teachers as t, shedule as s 
    #                                WHERE t.id=s.teacher_id
    #                                GROUP BY first_name
    #                                ''')
    
    users = await prisma.query_raw('''
                                   SELECT datetime('2022-01-01')>start_date as flag FROM teachers
                                   ''')

    await prisma.kafedra.find_many({
        "where":{
            "id":1
        }
    })

    print(users)
    
    await prisma.disconnect()

if __name__ == '__main__':
    asyncio.run(main())