# 🔥 Elite Exhaust Care – LPG Leakage and Smoke Detection

An IoT-based safety monitoring system designed to detect **LPG gas leakage and smoke/fire-related hazards** and provide an immediate local alert. The system uses **NodeMCU ESP8266** as the main controller and an **MQ-2 gas sensor** to continuously monitor the surrounding environment.

## 📌 Project Overview

Gas leakage in domestic and industrial environments can cause **fire accidents, health hazards, and property damage** if it is not detected at an early stage.

This project provides an automated gas leakage detection system by continuously monitoring the gas level using an **MQ-2 sensor**. The system first establishes a baseline value during sensor calibration and then compares the real-time gas reading with a configured safety threshold.

When the detected gas level exceeds the threshold, the system activates a **red LED and buzzer** to provide an immediate warning. During normal conditions, a **green LED** indicates that the environment is safe.

## 🎯 Objectives

* 🔥 Detect LPG/gas leakage at an early stage
* 🚨 Provide immediate leakage alerts
* 🔊 Activate a buzzer when dangerous gas levels are detected
* 🔴 Indicate danger conditions using a red LED
* 🟢 Indicate safe conditions using a green LED
* 📊 Continuously monitor gas sensor readings
* ⚙️ Establish a baseline through sensor calibration
* 🏠 Improve safety in domestic and industrial environments

## ⚙️ Components Used

| Component            | Purpose                                        |
| -------------------- | ---------------------------------------------- |
| **NodeMCU ESP8266**  | Main controller for processing sensor readings |
| **MQ-2 Gas Sensor**  | Detects LPG and other combustible gases        |
| **Red LED**          | Indicates dangerous gas conditions             |
| **Green LED**        | Indicates safe environmental conditions        |
| **Buzzer**           | Provides an audible leakage alert              |
| **Connecting Wires** | Connects the components                        |
| **Power Supply**     | Provides power to the system                   |

## 🔄 Working Principle

```text
             🔥 MQ-2 Gas Sensor
                    │
                    ▼
            Sensor Calibration
                    │
                    ▼
             Baseline Value
                    │
                    ▼
             NodeMCU ESP8266
                    │
                    ▼
          Compare Gas Level
          with Safety Threshold
                    │
          ┌─────────┴─────────┐
          │                   │
     Gas Level Safe       Gas Level High
          │                   │
          ▼                   ▼
     🟢 Green LED         🔴 Red LED
          │                   │
      Buzzer OFF          🚨 Buzzer ON
          │                   │
          ▼                   ▼
   Normal Monitoring      Gas Leak Alert
```

## 🧠 Working Logic

1. The **MQ-2 gas sensor** is connected to the analog input of the NodeMCU ESP8266.
2. During startup, the sensor is given a **warm-up period** to stabilize.
3. The system collects multiple sensor readings for **calibration**.
4. The average of the calibration readings is calculated as the **baseline environmental value**.
5. The system continuously reads the current gas sensor value.
6. The current reading is compared with the calibrated baseline and configured threshold.
7. The gas condition is classified as **Safe, Low Gas, Moderate Gas, or Danger**.
8. When the gas value exceeds the configured threshold, the system:

   * 🔴 Turns ON the red LED
   * 🟢 Turns OFF the green LED
   * 🔊 Activates the buzzer
   * 🚨 Displays a gas leakage alert
9. When the gas level is within the normal range:

   * 🟢 Green LED remains ON
   * 🔴 Red LED remains OFF
   * 🔇 Buzzer remains OFF
10. The monitoring process continues continuously.

## 📊 Gas Level Status

| Condition              | Status              | Indication       |
| ---------------------- | ------------------- | ---------------- |
| Normal environment     | 🟢 **SAFE**         | Green LED        |
| Slight gas presence    | 🟡 **LOW GAS**      | Monitoring       |
| Possible leakage       | 🟠 **MODERATE GAS** | Monitoring       |
| High gas concentration | 🔴 **DANGER**       | Red LED + Buzzer |

## 🔔 Safety Alert System

The **Safety Engine** continuously compares the real-time MQ-2 sensor reading with the configured detection threshold.

When:

```text
Gas Value > Detection Threshold
```

the system considers the condition as a high-level gas alert and activates the alarm system.

```text
        MQ-2 Sensor Reading
                │
                ▼
       Compare with Threshold
                │
        ┌───────┴───────┐
        │               │
      Normal          Exceeds
      Level           Threshold
        │               │
        ▼               ▼
   🟢 Green LED      🔴 Red LED
   🔇 Buzzer OFF     🔊 Buzzer ON
        │               │
        ▼               ▼
   Safe Status      LPG Leak Alert
```

## 📈 Sensor Calibration

The system performs sensor calibration during startup.

A predefined number of sensor samples are collected and averaged to calculate the environmental baseline.

```text
Calibration Samples
        │
        ▼
   MQ-2 Readings
        │
        ▼
  Calculate Average
        │
        ▼
 Baseline Gas Value
        │
        ▼
 Start Monitoring
```

This baseline helps the system compare subsequent gas readings against the initial environmental condition.

## 🖥️ Serial Monitor

The system provides real-time information through the Arduino IDE Serial Monitor.

The following information is displayed:

* Monitoring cycle ID
* Raw gas sensor value
* Baseline environmental value
* Estimated gas percentage
* Temperature reading
* Humidity reading
* Gas level status
* Alert level
* System safety status

Example:

```text
**************** SENSOR REPORT ****************
Monitoring Cycle ID         : 10
Raw Gas Sensor Value        : 315
Baseline Environment Value  : 250
Estimated Gas Concentration : 8 %
-----------------------------------------------
Temperature Reading         : 27 C
Humidity Reading            : 56 %
-----------------------------------------------
GAS LEVEL STATUS : MODERATE GAS
REMARK           : Possible gas leakage developing
-----------------------------------------------
ALERT LEVEL : NORMAL
STATUS      : Environment Safe
ACTION      : Monitoring Continues
************************************************
```

## 🔌 Pin Configuration

| Component           | NodeMCU Pin |
| ------------------- | ----------- |
| **MQ-2 Gas Sensor** | A0          |
| **Red LED**         | D7          |
| **Green LED**       | D0          |
| **Buzzer**          | D1          |

## 💻 Software

* **Embedded C / Arduino C++**
* **Arduino IDE**
* **ESP8266 Board Package**
* **Serial Monitor**

## 🧰 Technologies Used

* **ESP8266 NodeMCU**
* **MQ-2 Gas Sensor**
* **Embedded C**
* **Arduino IDE**
* **Analog Sensor Reading**
* **Sensor Calibration**
* **Threshold-based Safety Detection**
* **LED and Buzzer Alert System**

## ⚠️ Important Implementation Note

The gas percentage displayed by the current firmware is an **estimated relative percentage based on the ADC reading and calibrated baseline**. It should not be interpreted as a direct LPG concentration measurement in **ppm**.

The current firmware also generates temperature and humidity values for monitoring demonstration; these values are not obtained from a dedicated physical temperature/humidity sensor.

## 👩‍💻 Project Information

**Project Title:** Elite Exhaust Care – LPG Leakage and Smoke Detection Safety System

**Domain:** Internet of Things (IoT)

**Controller:** NodeMCU ESP8266

**Gas Sensor:** MQ-2

**Technology:** Embedded C / Arduino

**Development Environment:** Arduino IDE

**Alert System:** Red LED, Green LED and Buzzer

**Project Duration:** December 2025 – February 2026
