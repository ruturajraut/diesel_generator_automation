import json
import pyads

client_id = 15
location_id=7
zone_id=11
zone_name=''

controller_net_id="5.103.233.84.1.1"
controller_port = 851 # use 801 for tc2, use 851 for tc3
plc_val_prefix = '.' # use . for tc2, use .GVL for tc3

mqtt_broker_details = {
    'server_url' : 'mqtt://fortuitous-optician.cloudmqtt.com',
    'user' : 'geopcxoy',
    'pass' : 'osn07Rx4Eu-C',
    'port' : 1883,
    'ssl_port' : 8883,
    'websockets_port' : 443
}

email_details = {
    'url' : 'https://l94nyfvaf3.execute-api.ap-south-1.amazonaws.com/v1/device_update_status',
    'username' : 'quantum_email_alerts_username',
    'password' : 'pwd_email_alerts_user'
}


parameter_list = [
    {
        "device_type" : "dieselGenerator",
        "mqtt_topic" : "theWalkDG1",
        "table" : "quantum_dg",
        "frequency" : 36000,
        "counter" : 0,
        "items" : [
            {
                "id" : "theWalkDG1",
                "name" : "The Walk Diesel Generator 1",
                "parameters" : [
                    {
                        "PLCVariableName" : "actualRunStatus",
                        "PLCVariableDataType" : pyads.PLCTYPE_INT,
                        "MQTTVariableName" : "runStatus",
                        "lastStatus" : None,
                        "columnName" : "run_status"
                    },
                    {
                        "PLCVariableName" : "coolantTemperature",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "coolantTemperature",
                        "columnName" : "coolant_temperature"
                    },
                    {
                        "PLCVariableName" : "batteryVoltage",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "batteryVoltage",
                        "columnName" : "battery_voltage"
                    },
                    {
                        "PLCVariableName" : "actualFuelLevel",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "fuelLevel",
                        "columnName" : "fuel_level"
                    },
                    {
                        "PLCVariableName" : "avgPowerFactor",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "avgPowerFactor"
                    },
                    {
                        "PLCVariableName" : "oilPressure",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "oilPressure"
                    },
                    {
                        "PLCVariableName" : "engineSpeedRPM",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "engineSpeedRPM",
                        "columnName" : "engine_speed"
                    },
                    {
                        "PLCVariableName" : "frequency",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "frequency",
                        "columnName" : "frequency"
                    },
                    {
                        "PLCVariableName" : "l1_l2Voltage",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "l1_l2Voltage",
                        "columnName" : "l1_l2_voltage"
                    },
                    {
                        "PLCVariableName" : "l2_l3Voltage",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "l2_l3Voltage",
                        "columnName" : "l2_l3_voltage"
                    },
                    {
                        "PLCVariableName" : "l3_l1Voltage",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "l3_l1Voltage",
                        "columnName" : "l3_l1_voltage"
                    },
                    {
                        "PLCVariableName" : "l1Current",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "l1Current",
                        "columnName" : "l1_current"
                    },
                    {
                        "PLCVariableName" : "l2Current",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "l2Current",
                        "columnName" : "l2_current"
                    },
                    {
                        "PLCVariableName" : "l3Current",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "l3Current",
                        "columnName" : "l3_current"
                    },
                    # {
                    #     "PLCVariableName" : "utilityL1N_voltage",
                    #     "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                    #     "MQTTVariableName" : "l1_NVoltage"
                    # },
                    # {
                    #     "PLCVariableName" : "utilityL2N_voltage",
                    #     "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                    #     "MQTTVariableName" : "l2_NVoltage"
                    # },
                    # {
                    #     "PLCVariableName" : "utilityL3N_voltage",
                    #     "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                    #     "MQTTVariableName" : "l3_NVoltage"
                    # },
                    {
                        "PLCVariableName" : "autoManual",
                        "PLCVariableDataType" : pyads.PLCTYPE_INT,
                        "MQTTVariableName" : "autoManual",
                        "columnName" : "auto_manual"
                    },
                    {
                        "PLCVariableName" : "runHours",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "runHours",
                        "columnName" : "run_hours"
                    },
                    {
                        "PLCVariableName" : "runMinutes",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "runMinutes",
                        "columnName" : "run_minutes"
                    },
                    {
                        "PLCVariableName" : "KWH",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "kwh",
                        "columnName" : "kwh"
                    },
                    {
                        "PLCVariableName" : "isDGCommandable",
                        "PLCVariableDataType" : pyads.PLCTYPE_BOOL,
                        "MQTTVariableName" : "isDGCommandable"
                    },
                    {
                        "PLCVariableName" : "testRun",
                        "PLCVariableDataType" : pyads.PLCTYPE_BOOL,
                        "MQTTVariableName" : "testRun"
                    },
                    {
                        "PLCVariableName" : "testRunRemainingSeconds",
                        "PLCVariableDataType" : pyads.PLCTYPE_DWORD,
                        "MQTTVariableName" : "testRunRemainingSeconds"
                    },
# new variables---------------------------------------------------------------------------------
                    # {
                    #     "PLCVariableName" : "oilTemperature",
                    #     "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                    #     "MQTTVariableName" : "oilTemperature",
                    # },
                    # {
                    #     "PLCVariableName" : "chargeAlternatorVoltage",
                    #     "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                    #     "MQTTVariableName" : "chargeAlternatorVoltage",
                    # },
                    {
                        "PLCVariableName" : "utilityL1N_voltage",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "mains_L1NVvoltage",
                    },
                    {
                        "PLCVariableName" : "utilityL2N_voltage",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "mains_L2NVvoltage",
                    },
                    {
                        "PLCVariableName" : "utilityL3N_voltage",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "mains_L3NVvoltage",
                    },
                    {
                        "PLCVariableName" : "utilityL1_L2_voltage",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "mains_L1_L2_voltage",
                    },
                    {
                        "PLCVariableName" : "utilityL2_L3_voltage",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "mains_L2_L3_voltage",
                    },
                    {
                        "PLCVariableName" : "utilityL3_L1_voltage",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "mains_L3_L1_voltage",
                    },
                    {
                        "PLCVariableName" : "utilityL1Current",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "mainsL1Current",
                    },
                    {
                        "PLCVariableName" : "utilityL2Current",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "mainsL2Current",
                    },
                    {
                        "PLCVariableName" : "utilityL3Current",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "mainsL3Current",
                    },
                    {
                        "PLCVariableName" : "busL1N_voltage",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "bus_L1NVvoltage",
                    },
                    {
                        "PLCVariableName" : "busL2N_voltage",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "bus_L2NVvoltage",
                    },
                    {
                        "PLCVariableName" : "busL3N_voltage",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "bus_L3NVvoltage",
                    },
                    {
                        "PLCVariableName" : "busL1_L2_voltage",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "bus_L1_L2_voltage",
                    },
                    {
                        "PLCVariableName" : "busL2_L3_voltage",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "bus_L2_L3_voltage",
                    },
                    {
                        "PLCVariableName" : "busL3_L1_voltage",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "bus_L3_L1_voltage",
                    },
                    {
                        "PLCVariableName" : "busL1Current",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "bus_L1Current",
                    },
                    {
                        "PLCVariableName" : "busL2Current",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "bus_L1Current",
                    },
                    {
                        "PLCVariableName" : "busL3Current",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "bus_L3Current",
                    },
                    {
                        "PLCVariableName" : "coolant_pressure_1",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "coolant_pressure_1",
                    },
                    {
                        "PLCVariableName" : "coolant_pressure_2",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "coolant_pressure_2",
                    },
                    {
                        "PLCVariableName" : "fuelPressure",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "fuel_pressure_1",
                    },
                    # {
                    #     "PLCVariableName" : "fuel_pressure_2",
                    #     "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                    #     "MQTTVariableName" : "fuel_pressure_2",
                    # },
                    # {
                    #     "PLCVariableName" : "turbo_pressure_1",
                    #     "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                    #     "MQTTVariableName" : "turbo_pressure_1",
                    # },
                    # {
                    #     "PLCVariableName" : "turbo_pressure_2",
                    #     "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                    #     "MQTTVariableName" : "turbo_pressure_2",
                    # },
                    # {
                    #     "PLCVariableName" : "inlet_manifold_temperature_1",
                    #     "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                    #     "MQTTVariableName" : "inlet_manifold_temperature_1",
                    # },
                    # {
                    #     "PLCVariableName" : "inlet_manifold_temperature_2",
                    #     "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                    #     "MQTTVariableName" : "inlet_manifold_temperature_2",
                    # },
                    {
                        "PLCVariableName" : "exhaustStack_temperature_1",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "exhaust_temperature_1",
                    },
                    {
                        "PLCVariableName" : "exhaustStack_temperature_2",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "exhaust_temperature_2",
                    },
                    {
                        "PLCVariableName" : "water_In_Fuel_indicator",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "water_in_fuel",
                    },
                    {
                        "PLCVariableName" : "fuelTemperature",
                        "PLCVariableDataType" : pyads.PLCTYPE_REAL,
                        "MQTTVariableName" : "fuel_temperature",
                    },
                    {
                        "PLCVariableName" : "ats_alarm_1",
                        "PLCVariableDataType" : pyads.PLCTYPE_BOOL,
                        "MQTTVariableName" : "ATS1Status",
                    },
                    {
                        "PLCVariableName" : "ats_alarm_2",
                        "PLCVariableDataType" : pyads.PLCTYPE_BOOL,
                        "MQTTVariableName" : "ATS2Status",
                    },
                ]
            }
        ]
    }
]


# parameter_list = [
#     {
#         "device_type_name" : "energy meters",
#         "mqtt_topic" : "octopus_np_em",
#         "devices" : [
#             {
#                 "device_name" : "Ground Floor LT Panel",
#                 "parameter_map" : [
#                     {"mqtt":"avg_amp","plc" : "energy_meter_gnd_floor_amp_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_power_factor","plc" : "energy_meter_gnd_floor_pf_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_total_voltage","plc" : "energy_meter_gnd_floor_vll_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_voltage","plc" : "energy_meter_gnd_floor_vln_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"total_watts","plc" : "energy_meter_gnd_floor_watt_total","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"kwh","plc" : "energy_meter_gnd_floor_kwh","plc_data_type" : pyads.PLCTYPE_REAL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "1st Floor LT Panel",
#                 "parameter_map" : [
#                     {"mqtt":"avg_amp","plc" : "energy_meter_1_floor_amp_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_power_factor","plc" : "energy_meter_1_floor_pf_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_total_voltage","plc" : "energy_meter_1_floor_vll_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_voltage","plc" : "energy_meter_1_floor_vln_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"total_watts","plc" : "energy_meter_1_floor_watt_total","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"kwh","plc" : "energy_meter_1_floor_kwh","plc_data_type" : pyads.PLCTYPE_REAL,"value":None}
#                 ]
#             },

#             {
#                 "device_name" : "4th Floor LT Panel",
#                 "parameter_map" : [
#                     {"mqtt":"avg_amp","plc" : "energy_meter_4_floor_amp_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_power_factor","plc" : "energy_meter_4_floor_pf_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_total_voltage","plc" : "energy_meter_4_floor_vll_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_voltage","plc" : "energy_meter_4_floor_vln_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"total_watts","plc" : "energy_meter_4_floor_watt_total","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"kwh","plc" : "energy_meter_4_floor_kwh","plc_data_type" : pyads.PLCTYPE_REAL,"value":None}
#                 ]
#             },

#             {
#                 "device_name" : "5th Floor LT Panel",
#                 "parameter_map" : [
#                     {"mqtt":"avg_amp","plc" : "energy_meter_5_floor_amp_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_power_factor","plc" : "energy_meter_5_floor_pf_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_total_voltage","plc" : "energy_meter_5_floor_vll_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_voltage","plc" : "energy_meter_5_floor_vln_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"total_watts","plc" : "energy_meter_5_floor_watt_total","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"kwh","plc" : "energy_meter_5_floor_kwh","plc_data_type" : pyads.PLCTYPE_REAL,"value":None}
#                 ]
#             },

#             {
#                 "device_name" : "6th Floor LT Panel",
#                 "parameter_map" : [
#                     {"mqtt":"avg_amp","plc" : "energy_meter_6_floor_amp_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_power_factor","plc" : "energy_meter_6_floor_pf_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_total_voltage","plc" : "energy_meter_6_floor_vll_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_voltage","plc" : "energy_meter_6_floor_vln_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"total_watts","plc" : "energy_meter_6_floor_watt_total","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"kwh","plc" : "energy_meter_6_floor_kwh","plc_data_type" : pyads.PLCTYPE_REAL,"value":None}
#                 ]
#             },

            
#         ]
#     },
#     {
#         "device_type_name" : "air handling units",
#         "mqtt_topic" : "octopus_np_ahu",
#         "devices" : [
#             {
#                 "device_name" : "ground_floor_ahu",
#                 "parameter_map" : [
#                     {"mqtt":"return_air_temperature","plc" : "ahu_gnd_floor_return_air_temperature","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"run_status","plc" : "ahu_gnd_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"filter_status","plc" : "ahu_gnd_floor_filter_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"auto_manual_status","plc" : "ahu_gnd_floor_auto_manual_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"trip_status","plc" : "ahu_gnd_floor_trip_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"tfa_run_status","plc" : "tfa_gnd_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "1_floor_ahu",
#                 "parameter_map" : [
#                     {"mqtt":"return_air_temperature","plc" : "ahu_1_floor_return_air_temperature","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"run_status","plc" : "ahu_1_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"filter_status","plc" : "ahu_1_floor_filter_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"auto_manual_status","plc" : "ahu_1_floor_auto_manual_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"trip_status","plc" : "ahu_1_floor_trip_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"tfa_run_status","plc" : "tfa_1_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "4_floor_ahu",
#                 "parameter_map" : [
#                     {"mqtt":"return_air_temperature","plc" : "ahu_4_floor_return_air_temperature","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"run_status","plc" : "ahu_4_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"filter_status","plc" : "ahu_4_floor_filter_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"auto_manual_status","plc" : "ahu_4_floor_auto_manual_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"trip_status","plc" : "ahu_4_floor_trip_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"tfa_run_status","plc" : "tfa_4_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "5_floor_ahu",
#                 "parameter_map" : [
#                     {"mqtt":"return_air_temperature","plc" : "ahu_5_floor_return_air_temperature","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"run_status","plc" : "ahu_5_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"filter_status","plc" : "ahu_5_floor_filter_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"auto_manual_status","plc" : "ahu_5_floor_auto_manual_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"trip_status","plc" : "ahu_5_floor_trip_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"tfa_run_status","plc" : "tfa_5_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "6_floor_ahu",
#                 "parameter_map" : [
#                     {"mqtt":"return_air_temperature","plc" : "ahu_6_floor_return_air_temperature","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"run_status","plc" : "ahu_6_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"filter_status","plc" : "ahu_6_floor_filter_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"auto_manual_status","plc" : "ahu_6_floor_auto_manual_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"trip_status","plc" : "ahu_6_floor_trip_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"tfa_run_status","plc" : "tfa_6_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             }
#         ]
#     },
#     {
#         "device_type_name" : "temperature and humidity",
#         "mqtt_topic" : "octopus_np_temp_rh",
#         "devices" : [
#             {
#                 "device_name" : "terrace_floor_sensor",
#                 "parameter_map" : [
#                     {"mqtt":"temperature","plc" : "terrace_floor_temperature","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"humidity","plc" : "terrace_floor_humidity","plc_data_type" : pyads.PLCTYPE_REAL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "server_room_sensor",
#                 "parameter_map" : [
#                     {"mqtt":"temperature","plc" : "server_room_temperature","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"humidity","plc" : "server_room_humidity","plc_data_type" : pyads.PLCTYPE_REAL,"value":None}
#                 ]
#             }
#         ]
#     },
#     {
#         "device_type_name" : "hydrogen sensor",
#         "mqtt_topic" : "octopus_np_temp_hydro",
#         "devices" : [
#             {
#                 "device_name" : "ups_room_sensor",
#                 "parameter_map" : [
#                     {"mqtt":"level","plc" : "ups_room_h2","plc_data_type" : pyads.PLCTYPE_REAL,"value":None}
#                 ]
#             }
#         ]
#     },
#     {
#         "device_type_name" : "pumps",
#         "mqtt_topic" : "octopus_np_pumps",
#         "devices" : [
#             {
#                 "device_name" : "domestic_pump_1",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "domestic_pump_1_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "domestic_pump_2",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "domestic_pump_2_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "flush_pump_1",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "flush_pump_1_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "flush_pump_2",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "flush_pump_2_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "fire_pump_1",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "fire_pump_1_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "fire_pump_2",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "fire_pump_2_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "jockey_pump_1",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "jockey_pump_1_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "jockey_pump_2",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "jockey_pump_2_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "booster_pump_1",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "booster_pump_1_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "booster_pump_2",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "booster_pump_2_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             }
#         ]
#     },
#     {
#         "device_type_name" : "tanks",
#         "mqtt_topic" : "octopus_np_tanks",
#         "devices" : [
#             {
#                 "device_name" : "domestic_tank",
#                 "parameter_map" : [
#                     {"mqtt":"high_status","plc" : "domestic_tank_high_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"low_status","plc" : "domestic_tank_low_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "flush_tank",
#                 "parameter_map" : [
#                     {"mqtt":"high_status","plc" : "flush_tank_high_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"low_status","plc" : "flush_tank_low_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "fire_tank_1",
#                 "parameter_map" : [
#                     {"mqtt":"high_status","plc" : "fire_tank_1_high_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"low_status","plc" : "fire_tank_1_low_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "fire_tank_2",
#                 "parameter_map" : [
#                     {"mqtt":"high_status","plc" : "fire_tank_2_high_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"low_status","plc" : "fire_tank_2_low_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#         ]
#     }
# ]

pyads_datatype_map = {
    'REAL' : pyads.PLCTYPE_REAL,
    'BOOL' : pyads.PLCTYPE_BOOL
}

previous_temperature_reading = 0
temperature_difference_trigger = 0.005
fan_trigger_temperature = 30
fan_mode = 0 #0- auto,1-manual
fan_status=0