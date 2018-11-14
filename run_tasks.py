from tasks import add
import time
from celery.result import AsyncResult

if __name__ == '__main__':
    n1 = 10

    result_list = []

    for n2 in range(0,10):
        result = add.delay(n1,n2)
        # time.sleep(1)
        print (n2, result.id)
        result_list.append(result.id)
        # time.sleep(1)
        # if result.ready():
        #     print (result.result)


    # time.sleep(1)
    # for r in result_list:
    #     print ("for loop, ", r)
        
    #     # print (r, AsyncResult(r).ready())
    #     if AsyncResult(r).ready():
    #         # print (r, AsyncResult(r).result)
    #          print (r, AsyncResult(r).get())
    #     else:
    #         print (r, AsyncResult(r).ready())
    #         # print (r, AsyncResult(r).get())
    #         time.sleep(1)
    
                
                
               
            

        # while not result.ready():            
        #     print ("waiting for result...")
        
        # print (result.result)

            




    