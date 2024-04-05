from xmlrpc.client import TRANSPORT_ERROR
import pyads
import threading
# import local_db as db
# import web_service as ws
import mqtt_service as mqtt
import json
import gvl
import plc
import random
import web_service as ws
import requests
import database as db
from datetime import datetime
import time

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'telegram'))
# print(sys.path)
try:
    print("will try to import telegram")
    import telegram_send_message
    # print("telegram imported and connected")
except Exception as e:
    print("Telegram Exception:")
    print(e)
    print("telegram exception ended")

# import local_to_aws_data_sync as syncer

web_send_counter=300
web_send_threshold = 300
dbWritten = False

dbLastWriteYear = None
dbLastWriteMonth = None
dbLastWriteDay = None
dbLastWriteHour = None
dbLastWriteMinute = None

def data_retrieval_repeater():
    global dbWritten
    global dbLastWriteYear
    global dbLastWriteMonth
    global dbLastWriteDay
    global dbLastWriteHour
    global dbLastWriteMinute

    global web_send_counter
    global web_send_threshold

    while True:
        dt = datetime.now()

        # print(web_send_counter)

        for device_type in gvl.parameter_list:
            data_sendable = {
                "device_type" : device_type["device_type"],
                "data" : {}
                }

            complete_database_data = []

            if('items' in device_type):
                parameter_data = {}
                for item in device_type['items']:
                    item_table_data = {"id" : item["id"],"name" : item["name"]}
                    hasDGRunStatusChanged = False
                    parameter_data["id"] = item["id"]
                    parameter_data["name"] = item["name"]
                    for param in item["parameters"]:
                        # print("GVL." + param["PLCVariableName"])
                        try:
                            x = plc.plc_in.read_by_name("GVL." + param["PLCVariableName"], param["PLCVariableDataType"])
                            parameter_data[param["MQTTVariableName"]] = x
                            
                            if(device_type["device_type"] == "dieselGenerator"):
                                #check if any parameter has changed
                                if("columnName" in param and param["columnName"] == "run_status"):
                                    
                                    if(x != param['lastStatus'] and param['lastStatus'] != None):
                                        rStatus = ''
                                        
                                        if(x == 3):
                                            rStatus += "ON"
                                        else:
                                            rStatus += "OFF"
                                
                                        print("sending mail")
                                        ws.sendMail("The Walk Diesel Generator - " + item["name"] + " switched " + rStatus, item["name"] + " switched " + rStatus + " at " +  time.ctime(),"gautam@claypot.in,chauhan@claypot.in,abhilash@claypot.in")
                                        telegram_send_message.send_to_telegram("<b>The Walk Diesel Generator</b>\n" + item["name"] + " switched " + rStatus,"dg.jpg","-1002045206509")
                                        # telegram.send_msg("Diesel Generator @ The Walk has been switched " + rStatus,["gautam","gautam2","chauhan","abhilash"])
                                        # telegram.send_msg("Diesel Generator @ The Walk has been switched " + rStatus,["gautam"])
                                        hasDGRunStatusChanged = True
                                        # db.insert_alert(item["name"] + " switched " + rStatus)
                                        # mqtt.publish("quantum_alerts", "new-alert-notification")

                                    param['lastStatus'] = x

                            if("columnName" in param):
                                if(device_type["device_type"] == "dieselGenerator" or device_type["device_type"] == "undergroundWaterTanks"):
                                    item_table_data[param["columnName"]] = x
                                    
                        except pyads.ADSError:
                            print(f"unable to find PLC variable GVL.{param['PLCVariableName']}")
                        # val = 0
                        # if "value" in param.keys():
                        #     val = param["value"]
                        # parameter_data[param["MQTTVariableName"]] = val

                    # sending email if run status of pump has changed
                        
                        
                    data_sendable["data"] = parameter_data
                    complete_database_data.append(item_table_data)

                    if hasDGRunStatusChanged:
                        db.insert_dg_record(item_table_data)
                        hasDGRunStatusChanged = False

            try:
                if(device_type["device_type"] == "dieselGenerator"):
                    # print(dt)
                    # print(dt.minute)
                    for dg in complete_database_data:
                        print(dg)
                        if(dg["run_status"] == 0):
                            if(dbLastWriteYear == dt.year and dbLastWriteMonth == dt.month and dbLastWriteDay == dt.day and  dbLastWriteHour == dt.hour):
                                print("Data already saved in database for this hour")
                            else:          
                                if db.insert_dg_record(dg):
                                    dbLastWriteYear = dt.year
                                    dbLastWriteMonth = dt.month
                                    dbLastWriteDay = dt.day
                                    dbLastWriteHour = dt.hour
                                    dbLastWriteMinute = dt.minute
                                    printLastWrite()

                        elif(dg["run_status"] == 3):
                            if(dbLastWriteYear == dt.year and dbLastWriteMonth == dt.month and dbLastWriteDay == dt.day and  dbLastWriteHour == dt.hour and dbLastWriteMinute == dt.minute):
                                print("Data already saved in database for this minute")
                            else:
                                if db.insert_dg_record(dg):
                                    dbLastWriteYear = dt.year
                                    dbLastWriteMonth = dt.month
                                    dbLastWriteDay = dt.day
                                    dbLastWriteHour = dt.hour
                                    dbLastWriteMinute = dt.minute
                                    printLastWrite()
            except:
                print('unable to process deisel generator data for database')

                    
            
            
            

            
            mqtt.publish(device_type['mqtt_topic'],json.dumps(data_sendable))
            # print(data_sendable)
            # print("THE WALK DG CONTROLLER")

            

        

        time.sleep(2)
        # threading.Timer(2, data_retrieval_repeater).start()

def printLastWrite():
    global dbLastWriteYear
    global dbLastWriteMonth
    global dbLastWriteDay
    global dbLastWriteHour
    global dbLastWriteMinute

    print(dbLastWriteYear)
    print(dbLastWriteMonth)
    print(dbLastWriteDay)
    print(dbLastWriteHour)
    print(dbLastWriteMinute)

# if ws.get_zone_data():
plc.check_controller_availability()
mqtt.connect()

data_retrieval_repeater()
input("")


