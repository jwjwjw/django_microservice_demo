import py_eureka_client.eureka_client as eureka_client


name="ORDERS"
# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
eureka_client.init(eureka_server="http://127.0.0.1:8761/eureka",
                   app_name="orders",
                   instance_host='http://127.0.0.1',
                   instance_port=8002)

#eureka_server_list = "http://127.0.0.1:8761/eureka"
# you can reuse the eureka_server_list which you used in registry client
#eureka_client.init_discovery_client(eureka_server_list)