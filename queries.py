import data_manager



def ttt():
    return(data_manager.execute_select("""
    select * from CounterCapri
        """,
   

    ))

    

# def update_DB(cododac, id):
#     return(data_manager.execute_insert("""
#     update test set status=%(cododac)s where id = %(id)s
#                                         """,variables={
#             'cododac': cododac,
#             'id': id
           
#         }

# ))


# def insert_DB(cododac):
#     return(data_manager.execute_insert("""
#     INSERT INTO TEST (STATUS) VALUES(%(cododac)s)    
#     """, variables={
#         'cododac': cododac
     
#     }
           
       

# ))

# def getbyid(id):
#     return(data_manager.execute_select("""
#         SELECT * FROM test where id=%(id)s
#         """, variables={
#             'id' : id
          
#         }

#     ))



