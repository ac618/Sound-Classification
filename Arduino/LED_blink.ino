#define LED1 4
#define LED2 3
#define LED3 2
#define LED4 A4
#define LED5 A5

void setup()
{
    // Initialize serial communication
    Serial.begin(9600);

    // Set the LED pins as outputs
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);
    pinMode(LED3, OUTPUT);
    pinMode(LED4, OUTPUT);
    pinMode(LED5, OUTPUT);

    // Turn off all LEDs initially
    digitalWrite(LED1, LOW);
    digitalWrite(LED2, LOW);
    digitalWrite(LED3, LOW);
    digitalWrite(LED4, LOW);
    digitalWrite(LED5, LOW);
}

void blinkLED(int ledPin)
{
    for (int i = 0; i < 10; i++)
    {
        digitalWrite(ledPin, HIGH); // Turn the LED on
        delay(50);                  // Wait for 50 milliseconds
        digitalWrite(ledPin, LOW);  // Turn the LED off
        delay(50);                  // Wait for 50 milliseconds
    }
}

void loop()
{
    // Check if data is available to read
    if (Serial.available() > 0)
    {
        // Read the incoming byte
        int incomingByte = Serial.read() - '0'; // Convert ASCII to integer

        // Turn off all LEDs
        digitalWrite(LED1, LOW);
        digitalWrite(LED2, LOW);
        digitalWrite(LED3, LOW);
        digitalWrite(LED4, LOW);
        digitalWrite(LED5, LOW);

        // Blink the corresponding LED
        switch (incomingByte)
        {
        case 1:
            blinkLED(LED1);
            break;
        case 2:
            blinkLED(LED2);
            break;
        case 3:
            blinkLED(LED3);
            break;
        case 4:
            blinkLED(LED4);
            break;
        case 5:
            blinkLED(LED5);
            break;
        default:
            // Do nothing if the input is not between 1 and 5
            break;
        }
    }
}
