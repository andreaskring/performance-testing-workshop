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

## Øvelser

[Ex 1](exercises/ex1.md)<br />
[Ex 2](exercises/ex2.md)