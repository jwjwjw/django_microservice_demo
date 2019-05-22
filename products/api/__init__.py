import py_eureka_client.eureka_client as eureka_client

name="PRODUCTS"
your_rest_server_port = 8001
# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
eureka_client.init(eureka_server="http://127.0.0.1:8761/eureka",
                   app_name="products",
                    instance_host='http://127.0.0.1',
                   instance_port=8001)

#eureka_server_list = "http://127.0.0.1:8761/eureka"
# you can reuse the eureka_server_list which you used in registry client
#eureka_client.init_discovery_client(eureka_server_list)