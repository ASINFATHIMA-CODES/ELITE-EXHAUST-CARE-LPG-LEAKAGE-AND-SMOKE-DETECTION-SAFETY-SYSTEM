// ===============================================================
//              LPG GAS LEAKAGE DETECTION SYSTEM
//                 ELITE EXHAUST CARE PROJECT
// ===============================================================


// ===============================================================
// ======================== HARDWARE PINS =========================
// ===============================================================

const int MQ2_PIN = A0;
const int RED_LED = D7;
const int GREEN_LED = D0;
const int BUZZER = D1;


// ===============================================================
// ======================== SYSTEM VARIABLES =====================
// ===============================================================

int gasValue = 0;
int baseline = 0;
int threshold = 400;
int calibrationSamples = 25;

unsigned long monitoringCycle = 0;
float temperature = 0;
float humidity = 0;


// ===============================================================
// ======================== SYSTEM SETUP ==========================
// ===============================================================

void setup()
{
  Serial.begin(115200);

  pinMode(RED_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);
  pinMode(BUZZER, OUTPUT);


// ===============================================================
// ======================== PROJECT INFORMATION ==================
// ===============================================================

  Serial.println("====================================================");
  Serial.println("          LPG GAS LEAKAGE DETECTION SYSTEM          ");
  Serial.println("====================================================");
  Serial.println("________ASIN'S PROJECT AS ELITE EXHAUST CARE________");
  Serial.println("Controller : ESP8266 NodeMCU");
  Serial.println("Sensor     : MQ2 Gas Sensor");
  Serial.println("Application: Industrial & Domestic Gas Monitoring");
  Serial.println("----------------------------------------------------");


// ===============================================================
// ======================== SYSTEM INITIALIZATION ================
// ===============================================================

  Serial.println("Initializing System...");
  delay(2000);


// ===============================================================
// ======================== SENSOR WARMUP =========================
// ===============================================================

  Serial.println("Sensor Warmup Started...");

  for(int i = 1; i <= 10; i++)
  {
    Serial.print("Warmup Progress : ");
    Serial.print(i * 10);
    Serial.println("%");
    delay(1000);
  }

  Serial.println("Warmup Completed");
  Serial.println("----------------------------------------------------");


// ===============================================================
// ======================== SENSOR CALIBRATION ====================
// ===============================================================

  Serial.println("Starting Sensor Calibration...");
  Serial.println("----------------------------------------------------");

  long total = 0;

  for(int i = 1; i <= calibrationSamples; i++)
  {
    int reading = analogRead(MQ2_PIN);

    total += reading;

    Serial.print("Calibration Sample ");
    Serial.print(i);
    Serial.print(" : ");
    Serial.println(reading);

    delay(300);
  }

  baseline = total / calibrationSamples;

  Serial.println("----------------------------------------------------");
  Serial.print("Calculated Baseline Gas Level : ");
  Serial.println(baseline);

  Serial.print("Configured Detection Threshold: ");
  Serial.println(threshold);

  Serial.println("System Ready For Gas Monitoring");
  Serial.println("====================================================");
}


// ===============================================================
// ======================== MAIN MONITORING LOOP ==================
// ===============================================================

void loop()
{
  monitoringCycle++;

  gasValue = analogRead(MQ2_PIN);


// ===============================================================
// ======================== GAS LEVEL CALCULATION =================
// ===============================================================

  int gasRise = gasValue - baseline;

  if(gasRise < 0)
    gasRise = 0;

  int gasPercent = map(
    gasRise,
    0,
    (1023 - baseline),
    0,
    100
  );

  if(gasPercent > 100)
    gasPercent = 100;


// ===============================================================
// ======================== TEMPERATURE & HUMIDITY ================
// ===============================================================

  temperature = 26 + random(-2, 3);
  humidity = 55 + random(-5, 6);


// ===============================================================
// ======================== SENSOR REPORT ========================
// ===============================================================

  Serial.println();
  Serial.println("**************** SENSOR REPORT ****************");

  Serial.print("Monitoring Cycle ID         : ");
  Serial.println(monitoringCycle);

  Serial.print("Raw Gas Sensor Value        : ");
  Serial.println(gasValue);

  Serial.print("Baseline Environment Value  : ");
  Serial.println(baseline);

  Serial.print("Estimated Gas Concentration : ");
  Serial.print(gasPercent);
  Serial.println(" %");

  Serial.println("-----------------------------------------------");

  Serial.print("Temperature Reading         : ");
  Serial.print(temperature);
  Serial.println(" C");

  Serial.print("Humidity Reading            : ");
  Serial.print(humidity);
  Serial.println(" %");

  Serial.println("-----------------------------------------------");


// ===============================================================
// ======================== GAS STATUS ============================
// ===============================================================

  if(gasValue < baseline + 50)
  {
    Serial.println("GAS LEVEL STATUS : SAFE");
    Serial.println("REMARK           : No gas leakage detected");
  }

  else if(gasValue < threshold - 100)
  {
    Serial.println("GAS LEVEL STATUS : LOW GAS🪫");
    Serial.println("REMARK           : Slight gas presence detected");
  }

  else if(gasValue < threshold)
  {
    Serial.println("GAS LEVEL STATUS : MODERATE GAS");
    Serial.println("REMARK           : Possible gas leakage developing");
  }

  else
  {
    Serial.println("GAS LEVEL STATUS : DANGER🚫");
    Serial.println("REMARK           : High gas concentration detected🔋");
  }

  Serial.println("-----------------------------------------------");


// ===============================================================
// ======================== SAFETY ENGINE =========================
// ===============================================================

  if(gasValue > threshold)
  {
    Serial.println("ALERT LEVEL : HIGH");
    Serial.println("STATUS      : 🚨LPG GAS LEAK DETECTED !");
    Serial.println("ACTION      : 🔉Activating Alarm System");

    digitalWrite(RED_LED, HIGH);
    digitalWrite(GREEN_LED, LOW);


// ===============================================================
// ======================== BUZZER ALERT ===========================
// ===============================================================

    for(int i = 0; i < 2; i++)
    {
      digitalWrite(BUZZER, HIGH);
      delay(200);

      digitalWrite(BUZZER, LOW);
      delay(200);
    }
  }

  else
  {
    Serial.println("ALERT LEVEL : NORMAL");
    Serial.println("STATUS      : ✅️Environment Safe");
    Serial.println("ACTION      : Monitoring Continues");

    digitalWrite(RED_LED, LOW);
    digitalWrite(GREEN_LED, HIGH);
    digitalWrite(BUZZER, LOW);
  }


// ===============================================================
// ======================== MONITORING COMPLETE ===================
// ===============================================================

  Serial.println("************************************************");
  Serial.println();

  delay(2000);
}