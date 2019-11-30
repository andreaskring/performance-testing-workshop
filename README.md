# Performance Testing Workshop

## Installering af JMeter
Kræver Java 8+... så installér først Java, hvis du ikke allerede har denne installeret (på Ubuntu 18.04 LTS køres eksempelvis):
```
$ sudo apt install openjdk-11-jdk
```
Derefter kan JMeter hentes på [https://jmeter.apache.org/download_jmeter.cgi](https://jmeter.apache.org/download_jmeter.cgi). Hent `.tgz` filen og udpak denne - derefter burde JMeter være klar til kørsel fra mappen `bin/jmeter`.

For at få en lidt højere tidsopløsning på de grafer, som JMeter genererer, skal vi lige 
skrue lidt på en enkelt konfiguration. I filen `bin/reportgenerator.properties` ændres 
nedenstående property til 5000 i stedet for 60000:
```
jmeter.reportgenerator.overall_granularity=5000
```

## Installering af Docker
Nedenstående applikationer kører i Docker, så hvis du ikke allerede har Docker installeret, så gør 
dette vha. instruktionerne [her](https://docs.docker.com/install/linux/docker-ce/ubuntu/).


## Ex 1
Dette er en JMeter "Hello world" øvelse, hvor vi skal lave en _Test Plan_ indeholdende en 
_Thread Group_, som indeholder en _Simple Controller_, der indeholder et enkelt request.

Formålet er at undersøge to funktionelt identiske REST services, hvor den ene er udviklet 
i Python, mens den anden er skrevet i Java. De to REST services startes op på følgende måde:

### Python

En Flask-applikation, som kan deployes med Docker:
```
$ cd docker/flask
$ docker build -t flask-app .
$ docker run --name flask-app -p 5000:5000 flask-app
```
Der skulle nu køre en Flask app på port 5000. App'en returnerer det n'te Fibonacci-tal 
vha. en rekursiv funktion (valgt bevidst, da dette går langsomt for store værdier af n). 
Test, at app'en fungerer ved at kalde fx:
```
$ curl http://localhost:5000/fib?n=7
```
som vil returnere det 7. Fibonacci-tal.

### Java
En Spring Boot applikation, som enten kan deployes direkte med Java eller også via en 
Docker container på samme måde som ovenfor. Deployment direkte med Java foretages således:
```
$ cd docker/spring-boot
$ java -jar target/performance-testing-workshop-0.0.1-SNAPSHOT.jar
```
Med Docker klares det ved:
```
$ cd docker/spring-boot
$ docker build -t spring-boot-app .
$ docker run --name spring-boot-app -p 8080:8080 spring-boot-app
```

App'en kan testes ved at kalde fx:
```
$ curl http://localhost:8080/fib?n=7
```

### JMeter

Start JMeter og gør følgende:

1. Tilføj en _Thread Group_ til testplanen.
2. Tilføj en _Simple Controller_ til trådgruppen.
3. Tilføj et _HTTP Request_ til controlleren og udfyld felterne efter behov.
4. Tilføj et _View Results Tree_ til trådgruppen.
5. Klik på _View Results Tree_ til højre og kør testplanen (vha. den grønne play-knap).
6. Verificér, at kaldet gik godt og at de forventede data blev returneret.
7. Tilføj en _Timer_ til requestet og vælg en passende "think time".
8. Tryk på _Thread Group_ og øg antallet af brugere. Vælg også en passende Ramp-up periode.
9. Sæt Loop-Count til uendelig og sæt en Duration på fx 200 s.
10. Gem testplanen og kør denne fra kommandolinjen med

    ```
    $ jmeter -n -t sti/til/testplan.jmx -l log.jtl
    ```
    
11. Generér en testrapport med

    ```
    $ jmeter -g log.jtl -o report
    ```

    og kig på resultatet i en browser.
    
12. Undersøg, hvilken af de to REST applikationer, som performer bedst (definér selv 
    passende parametre for at afgøre dette - inkl. værdien af n, som fodres ind i 
    Fibonacci-funktionen).

Et eksempel på en testplan, som kan bruges sammenligning, kan findes i mappen [jmeter/ex1.jmx](jmeter/ex1.jmx).


## Ex 2

setUp thread group for making users

make random file name - upload file to Shared

download file

delete file again

## Ex 3
Recording - se JMeter tutorial