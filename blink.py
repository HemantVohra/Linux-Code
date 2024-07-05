#include <wiringPi.h>
#include <signal.h>

#define AMBER 13
#define GREEN 19
#define RED 26

int blink = 1;

void cleanup(int signo) {
    blink = 0;
}
int main(void) {
    signal(SIGINT, cleanup);
    signal(SIGTERM, cleanup);
    signal(SIGHUP, cleanup);

    wiringPiSetupGpio();
    pinMode(AMBER, OUTPUT);
    pinMode(GREEN, OUTPUT);
    pinMode(RED, OUTPUT);

    while (blink) {
        // Forward sequence
        digitalWrite(AMBER, HIGH);
        delay(500);
        digitalWrite(AMBER, LOW);

        digitalWrite(GREEN, HIGH);
        delay(500);
        digitalWrite(GREEN, LOW);

        digitalWrite(RED, HIGH);
        delay(500);
        digitalWrite(RED, LOW);

        // Reverse sequence
        digitalWrite(GREEN, HIGH);
        delay(500);
        digitalWrite(GREEN, LOW);

        digitalWrite(AMBER, HIGH);
        delay(500);
        digitalWrite(AMBER, LOW);
    }

    digitalWrite(AMBER, LOW);
    digitalWrite(GREEN, LOW);
    digitalWrite(RED, LOW);
    pinMode(AMBER, INPUT);
    pinMode(GREEN, INPUT);
    pinMode(RED, INPUT);

    return 0;
}

